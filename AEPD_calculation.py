import pandas as pd
import numpy as np

# --- Read Excel file ---
df = pd.read_excel('Your_excel_file.xlsx', sheet_name='Sheet 1')

# --- Define column positions (0-indexed) ---
ct_idx       = 0  # Column A: Conversational turn No.
gen_idx      = 2  # Column C: Aspects in general
personal_idx = 3  # Column D: Related Personal Profile statement No.
content_idx  = 5  # Column F: Aspect content in the conversational turn

# --- Retrieve column names based on positions ---
ct_col       = df.columns[ct_idx]
gen_col      = df.columns[gen_idx]
personal_col = df.columns[personal_idx]
content_col  = df.columns[content_idx]

# --- Count words in column F and add as 'word_count' column ---
df['word_count'] = (
    df[content_col]
      .fillna('')
      .astype(str)
      .apply(lambda txt: len(txt.split()))
)

def compute_scores(group):
    # Create boolean arrays to check
    m_personal = group[personal_col].notna()  # Check if aspect is personalized
    m_turn = (
        group[content_col].notna() & 
        group[content_col].astype(str).str.strip().ne('')
        )   # Check if aspect appeared in the conversational turn (non-empty)
    m_both   = m_personal & m_turn    # Check if appeared aspect is personalized

    # Count metrics
    Gen_all   = len(group)
    Gen_per   = m_personal.sum()
    Turn_all  = m_turn.sum()
    Turn_per  = m_both.sum()

    # Personalization Score
    Turn = Turn_per / Turn_all if Turn_all else 0
    Gen  = Gen_per  / Gen_all  if Gen_all  else 0
    PAP       = 0 if Gen == 1 else max(0, Turn - Gen) / (1 - Gen)

    # Use 'word_count' column for text length metrics
    l_prime      = group.loc[m_turn, 'word_count']
    L_all        = l_prime.sum()
    L_per_avg    = l_prime[m_both].sum() / Turn_per if Turn_per else 0
    nonper_count = (m_turn & ~m_personal).sum()
    L_nonper_avg = l_prime[~m_personal & m_turn].sum() / nonper_count if nonper_count else 0
    PCL          = 0 if L_all == L_nonper_avg else max(0, L_per_avg - L_nonper_avg) / (L_all - L_nonper_avg)

    P_score = PAP * PCL

    # Diversification Score
    AR     = Turn_all / Gen_all if Gen_all else 0
    l      = l_prime / l_prime.sum() if l_prime.sum() else pd.Series(dtype=float)
    l_star = 1 / Turn_all if Turn_all else 0
    SS     = ((l - l_star) ** 2).sum()
    RNSS   = np.sqrt(SS / 2)
    CLU    = 1 - RNSS
    D_score = AR * CLU

    return pd.Series({
        'Gen_all'  : Gen_all,
        'Gen_per'  : Gen_per,
        'Turn_all' : Turn_all,
        'Turn_per' : Turn_per,
        'PAP'      : PAP,
        'PCL'      : PCL,
        'P_score'  : P_score,
        'AR'       : AR,
        'SS'       : SS,
        'RNSS'     : RNSS,
        'CLU'      : CLU,
        'D_score'  : D_score
    })

# output
summary = (
    df
    .groupby(ct_col, dropna=False)  # group by conversational turn No.
    .apply(compute_scores, include_groups=False)
    .reset_index()
)

# Print the summary or save to Excel
print(summary)
# summary.to_excel('AEPD_scores.xlsx', index=False)
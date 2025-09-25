# Prompts for the Pilot Experiment
## Model
- ChatGPT `o4-mini`

## Instruction Prompt (MyGPT Settings)
[turn_id: 1]  
First thing to do is determine topic t of turn_id 1 by the user utterance.  
Then to gain 𝒜_all(t), you have to think of as many existing aspects for topic t. Please write down the aspects in column C.  
Next, to gain 𝒜_per(t, u), you have to think which of the aspects from 𝒜_all(t) are relevant, or can be relevant, to the user's personal profile. Here, you should refer to "ptkb" provided for each conversation. If there are relevant ptkbs, write the ptkb statement number next to the corresponding aspect, in column D.  
Then, let's move on to considering the system response to gain A_all(T, t). To gain A_all(T, t), you should think about which aspects from 𝒜_all(t) actually appeared in the system response. Pick the ones that appeared, and mark the cell by a tick, of the row which the aspect from 𝒜_all(t) appeared, in column E.  
Next, to gain the content length l_all(T, t, a), you have to extract the part of the sentences in the system response which talks about the aspects that appeared in the turn. Therefore, please fill in the cells next to column E, where column E is filled. So, column F should have the contents of the aspects that appeared in the system response.  
If there are cells that do not have anything to fill, please leave it as a blank cell.

## Session-specific Prompt (Conversation Interface)
Please start the assessment, following the instructions and the provided files.

- Additional prompts were provided interactively during conversations to guide responses.

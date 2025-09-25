# AEPD: Aspect-based Evaluation of Personalization and Diversification
AEPD is an evaluation framework for conversational search systems such as those based on RAG (retrieval-augmented generation) that assesses conversational turns at the aspect level. It evaluates how personalized or diversified a system response is.

## Overview
This repository contains prompts and Python code used in the pilot experiment described in our paper on **Aspect-based Evaluation of Personalization and
Diversification in Conversational Search Systems**. 

## Experimental Workflow

1. **Input**  
   - Prompts, conversational turns, and an explanation of AEPD are provided to ChatGPT `o4-mini`.

2. **Output**  
   - The model generates evaluation results in a table format.

3. **Data Processing**  
   - The output tables (Excel format, for each conversation) are fed into `AEPD_calculation.py` to aggregate and process the results.

4. **Results**  
   - Evaluation results are produced.

## Included Files
- `prompts.md` — Contains the prompts used in the pilot experiment.
- `AEPD_calculation.py` — Process the model outputs and computes the Personalization and Diversification scores.

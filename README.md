# TOPSIS Analysis of Pre-Trained Sentence Similarity Models

## Project Overview
This project uses the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS) to evaluate and rank various pre-trained sentence embedding models. The objective is to determine the best model by balancing similarity performance, speed, and model efficiency.

## User Details
Name: Saniya Jindal  
Roll Number: 102303183  
Assignment Domain: Sentence Similarity using NLP  

## Project Structure
sentence_similarity_models.csv: Raw performance metrics of all models  
topsis_result.csv: Final TOPSIS scores and rankings  
model_compare.png: Bar graph visualization of model comparison  
assignment_5.ipynb: Jupyter Notebook with full implementation  
README.md: Project documentation  

## Models Evaluated
- all-MiniLM-L6-v2  
- all-mpnet-base-v2  
- paraphrase-MiniLM-L6-v2  
- sentence-t5-base  
- stsb-roberta-large  

## Criteria for Comparison

Parameter | Impact | Description  
---|---|---  
Average Similarity Score | (+) Benefit | Higher similarity indicates better semantic understanding  
Inference Time | (–) Cost | Lower time indicates faster model performance  
Model Size | (–) Cost | Smaller size means lower memory usage  
Embedding Dimension | (+) Benefit | Higher dimension captures richer semantic features  

## Method Used

Custom Python package used:

Topsis-Saniya-102303183

Command:

topsis sentence_similarity_models.csv "1,1,1,1" "+,-,-,+" topsis_result.csv

## Conclusion

TOPSIS effectively ranked the sentence similarity models by considering both performance and efficiency metrics. The highest-ranked model provides the best overall trade-off.

## Author
Saniya Jindal  
B.E. Computer Engineering  
Roll No: 102303183

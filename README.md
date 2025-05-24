# Resume Matcher AI

This project implements an AI-powered resume matching tool that compares multiple resumes to a job description using BERT-based semantic similarity. It helps identify which resume best fits the job.

## Features

- Loads a job description and multiple resumes from `.txt` files
- Uses a pre-trained BERT model (`all-MiniLM-L6-v2`) from `sentence-transformers`
- Computes semantic similarity using cosine similarity
- Outputs sorted matching scores to the terminal and `result.txt`

## How It Works

1. Reads a job description from `job.txt`
2. Reads candidate resumes from `resumes.txt`, with each resume separated by a blank line
3. Encodes all texts into vector embeddings using BERT
4. Calculates cosine similarity between the job and each resume
5. Sorts and displays the resumes based on similarity score
6. Writes the results to `result.txt`

## File Structure·
resume-matcher-ai/
├── job.txt # Text file containing the job description
├── resumes.txt # Text file containing candidate resumes (separated by blank lines)
├── result.txt # Output file with sorted resume similarity scores
├── match.py # Python script that performs the matching logic
├── README.md # Project documentation
└── venv/ # (Optional) Virtual environment directory
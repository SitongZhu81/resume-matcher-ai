from sentence_transformers import SentenceTransformer, util

# Load the pre-trained BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Read job description
with open('job.txt', 'r') as f:
    job = f.read().strip()

# Read resumes (separated by empty lines)
with open('resumes.txt', 'r') as f:
    resumes = [r.strip() for r in f.read().split('\n\n') if r.strip()]

# Combine and compute embeddings
texts = [job] + resumes
embeddings = model.encode(texts)

# Compute similarity scores
scores = util.cos_sim(embeddings[0], embeddings[1:])[0]

# Pair each resume with its similarity score, and sort from highest to lowest
results = sorted(zip(resumes, scores), key=lambda x: x[1], reverse=True)

# Print sorted resumes and their scores
for i, (resume, score) in enumerate(results):
    print(f"Resume {i+1} | Similarity Score: {score:.4f}")
    print(resume)
    print('-' * 50)
    # Write results to result.txt
with open('result.txt', 'w') as out:
    for i, (resume, score) in enumerate(results):
        out.write(f"Resume {i+1} | Similarity Score: {score:.4f}\n")
        out.write(resume + '\n' + '-' * 50 + '\n')

import pandas as pd
import matplotlib.pyplot as plt
from compute_similarity import compute_similarity
from topsis import topsis

print("Running Sentence Similarity TOPSIS — Roll No 183")

# Sample sentences
sentences1 = [
    "The cat sits on the mat",
    "I love artificial intelligence",
    "He is playing football"
]

sentences2 = [
    "A cat is sitting on a rug",
    "AI is amazing",
    "A man plays soccer"
]

# Compute similarity
similarity_results = compute_similarity(sentences1, sentences2)

# Create dataframe
df = pd.DataFrame(similarity_results.items(), columns=["Model", "Similarity"])
df["Time"] = [0.12, 0.10, 0.20]   # dummy values
df["Size"] = [90, 85, 420]        # dummy values

# TOPSIS
weights = [1, 1, 1]
impacts = ["+", "-", "-"]

final = topsis(df, weights, impacts)

# Save result
final.to_csv("results/topsis_result.csv", index=False)
print(final)

# Plot graph
plt.barh(final["Model"], final["TOPSIS Score"])
plt.xlabel("TOPSIS Score")
plt.title("Sentence Similarity Model Ranking")
plt.tight_layout()
plt.savefig("results/similarity_comparison_graph.png")
plt.show()


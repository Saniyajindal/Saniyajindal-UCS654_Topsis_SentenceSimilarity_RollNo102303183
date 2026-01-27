from sentence_transformers import SentenceTransformer, util

models = {
    "M1_all-MiniLM-L6-v2": SentenceTransformer("all-MiniLM-L6-v2"),
    "M2_paraphrase-MiniLM-L6-v2": SentenceTransformer("paraphrase-MiniLM-L6-v2"),
    "M3_all-mpnet-base-v2": SentenceTransformer("all-mpnet-base-v2"),
}

def compute_similarity(sentences1, sentences2):
    results = {}

    for name, model in models.items():
        scores = []
        for s1, s2 in zip(sentences1, sentences2):
            emb1 = model.encode(s1, convert_to_tensor=True)
            emb2 = model.encode(s2, convert_to_tensor=True)
            score = util.cos_sim(emb1, emb2).item()
            scores.append(score)

        avg_score = sum(scores) / len(scores)
        results[name] = avg_score

    return results

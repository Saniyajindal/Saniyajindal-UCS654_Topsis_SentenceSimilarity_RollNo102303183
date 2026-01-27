import numpy as np
import pandas as pd

def topsis(df, weights, impacts):
    matrix = df.iloc[:, 1:].values.astype(float)

    norm = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted = norm * weights

    ideal_best = np.max(weighted, axis=0)
    ideal_worst = np.min(weighted, axis=0)

    for i, impact in enumerate(impacts):
        if impact == "-":
            ideal_best[i], ideal_worst[i] = ideal_worst[i], ideal_best[i]

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["TOPSIS Score"] = score
    df["Rank"] = df["TOPSIS Score"].rank(ascending=False)

    return df


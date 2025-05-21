# face.py

import matplotlib.pyplot as plt
import numpy as np

def draw_thermometer(score):
    score = np.clip(score, -1, 1)

    fig, ax = plt.subplots(figsize=(6, 1.5))
    ax.set_xlim(-1, 1)
    ax.set_ylim(0, 1)
    ax.axis("off")

    # Background bar
    ax.barh(0.5, width=2, left=-1, height=0.4, color="#eee", edgecolor="black")

    # Determine bar color from red (-1) to green (+1)
    cmap = plt.get_cmap("RdYlGn")  # Red to Yellow to Green
    norm_score = (score + 1) / 2   # Normalize [-1,1] -> [0,1]
    color = cmap(norm_score)

    # Foreground bar showing sentiment level
    ax.barh(0.5, width=score, left=0 if score >= 0 else score, height=0.4, color=color)

    # Label text
    ax.text(score, 0.95, f"Sentiment: {score:+.2f}", ha='center', fontsize=12)

    plt.tight_layout()
    plt.show()

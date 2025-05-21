# 🎭 Sentiment Visualizer

A real-time desktop sentiment analyzer built with Python, HuggingFace Transformers, and a sleek Tkinter interface. As you type, the app instantly analyzes your text sentiment and visualizes it with a glowing yellow emoji and a sentiment bar.

---

## 🖼️ Demo

<p align="center">
  <img src="sentiment.gif" alt="Sentiment Visualizer Demo" width="50%">
</p>

---

## ✨ Features

- 🔍 **Live Sentiment Detection** as you type
- 🤖 HuggingFace **Transformer-powered** analysis
- 😊 Dynamic emoji that reflects your emotion (green-happy, yellow-neutral, red-angry)
- ⚡ GPU/CPU compatible via PyTorch

---

## Model Used
- cardiffnlp/twitter-roberta-base-sentiment
A RoBERTa-based model fine-tuned on Twitter data.
It classifies input into:

- negative

- neutral

- positive

## Project Structure
sentiment-visualizer/
│
├── src/
│   └── sentiment_analysis/
│       ├── app.py        # GUI application (Tkinter)
│       └── analyzer.py   # HuggingFace-based sentiment logic
│
├── sentiment.gif         # Demo animation (used in README)
├── requirements.txt      # Dependencies
└── README.md             

## 🛠️ Installation & Usage
python -m venv venv
- Windows: venv\Scripts\activate
- macOS/Linux: source venv/bin/activate
- Follow: pip install -r requirements.txt
- Run: python src/sentiment_analysis/app.py

## 👤 Author
Mohammed Rakibul Hasan

## 📃 License
MIT License © Mohammed Rakibul Hasan

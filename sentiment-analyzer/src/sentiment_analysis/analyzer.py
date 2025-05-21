# analyzer.py
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import numpy as np

class SentimentAnalyzer:
    def __init__(self):
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        model_name = "cardiffnlp/twitter-roberta-base-sentiment"
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_name).to(self.device)

    def analyze(self, text):
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True).to(self.device)
        with torch.no_grad():
            output = self.model(**inputs)
            scores = torch.nn.functional.softmax(output.logits, dim=1)[0].cpu().numpy()

        # Convert to sentiment score: negative * -1 + neutral * 0 + positive * 1
        sentiment_score = -1 * scores[0] + 0 * scores[1] + 1 * scores[2]
        return sentiment_score

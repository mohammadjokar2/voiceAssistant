from transformers import pipeline
import hazm

class NLPProcessor:
    def __init__(self):
        print("Loading Persian NLP model...")
        self.tokenizer = hazm.word_tokenize
        self.model = pipeline("text-classification", model="HooshvareLab/bert-fa-base-uncased")

    def process_intent(self, text):
        tokens = self.tokenizer(text)
        result = self.model(" ".join(tokens))[0]
        intent = result["label"]
        
        # Simple intent-response mapping
        with open("intents.json", "r", encoding="utf-8") as f:
            intents = json.load(f)
        
        response = intents.get(intent, "متوجه نشدم. لطفاً دوباره امتحان کنید.")
        return response

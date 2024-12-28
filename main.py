from speech_utils import speech_to_text, text_to_speech
from nlp_utils import NLPProcessor
import json

def main():
    print("Starting Persian Voice Assistant...")
    nlp_processor = NLPProcessor()

    while True:
        print("Listening for command...")
        command = speech_to_text(lang="fa-IR")
        if "خروج" in command:
            print("خداحافظ!")
            text_to_speech("خداحافظ!", lang="fa")
            break
        
        response = nlp_processor.process_intent(command)
        print(f"Response: {response}")
        text_to_speech(response, lang="fa")

if __name__ == "__main__":
    main()

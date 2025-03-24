import json
class flash_Card:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    def display_info(self):
        return f"Question: {self.question}, Answer: {self.answer}"
    def to_dict(self):
        return {"question": self.question, "answer": self.answer}
flash_cards = [
    flash_Card("Is Grayton Dumb", "NO"),
    flash_Card("what is 1 + 1", "2"),
   

]
cards_data = [flash_Card.to_dict() for flash_Card in flash_cards]
with open("flashcards.json", "w") as file:
    json.dump(cards_data, file, indent=4)

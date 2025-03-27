import random
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



    class teacher(flash_Card):
        def __init__(self, question, answer, user):
            super().__init__(question, answer)
            self.user = user
""" try:
    with open("cars.json", "r") as file:
        cars_data = json.load(file)
except FileNotFoundError:
    cars_data = []

cards_data.append(new_card.to_dict())

with open("cars.json", "r") as file:
    json.dump(cards_data, file, indent=4) """

class Students(flash_Card):
    def __init__(self, question, answer, streak):
        super().__init__(question, answer)
        self.streak = streak
    
    mode = input("Student or TeacherMODE: input s or t")
    if mode.lower() == "s":
        print("student mode")
        

        ask = "do you want to continue: yes/no"
        askA = input(f"{ask}")
        streak = 0
        points = 0 


    while askA.lower() == "yes":      
        question = random.choice(cards_data)
        answer =  input(f"{question['question']} answer:")
        if streak == 5:
            points += 2
        
        if answer.lower() == question['answer'].lower():
            streak += 1
            points += 1
            print(input(f"correct, {ask}           points:{points}     streak:{streak}"))
        
        else:
            print(f"incorrect the correct answer is {question['answer']}     points:{points}     streak:{streak}")
            streak = 0
            
            askA = input(f"{ask}")
            if askA.lower() == "no":
                print("Goodbye")
                break
    
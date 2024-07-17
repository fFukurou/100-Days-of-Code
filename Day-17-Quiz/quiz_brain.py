class QuizzBrain:
    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list 
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(f"\nQ.{self.question_number}: {current_question.question} (True/False)?  \n")
        self.check_answer(answer, current_question.correct_answer)


    def still_has_questions(self):
        return self.question_number != len(self.question_list)
    
    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            print('You got it right!')
            self.score += 1
        else:
            print("Wrong!")

        print(f"The correct answer was {correct_answer}")
        if self.still_has_questions() == True:
            print(f"Your current score is: {self.score}/{self.question_number}")
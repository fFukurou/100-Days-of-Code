#Quiz Project

from question_model import Question
from data import question_data
from quiz_brain import QuizzBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question['question'], question['correct_answer']))

quizz = QuizzBrain(question_bank)
while quizz.still_has_questions() == True:
    quizz.next_question()

print("You've completed the quiz.")
print(f"\nYour final score was {quizz.score}/{len(quizz.question_list)}\n")
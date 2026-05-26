from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_data = question["answer"]
    new_question = Question(question_text, question_data)
    question_bank.append(new_question)

ques_1 = QuizBrain(question_bank)
while ques_1.still_has_questions():
    ques_1.next_question()

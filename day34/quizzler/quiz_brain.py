from question_model import Question


class QuizBrain:

    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.current_question: Question = self.question_list[self.question_number]
        self.score = 0

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        return f"Q.{self.question_number}: {self.current_question.text}"

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer):
        correct_answer = self.current_question.answer
        print(correct_answer)
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

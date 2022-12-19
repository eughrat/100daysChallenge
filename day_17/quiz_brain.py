class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        if self.question_number == len(self.question_list) - 1:
            print("\nYou've completed the quiz")
            print(f"Your final score was: {self.score} / {len(self.question_list)}")
            return False
        else:
            return True

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("Correct answer!")
        else:
            print("False answer!")
        print(f"The correct answer was: {correct_answer}")
        return self.score


    def next_question(self):
        current_question = self.question_list[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {current_question.text[0]} (True/False): ")
        self.check_answer(answer, current_question.answer)
        print(f"Your current score is: {self.score}/ {self.question_number + 1}")
        self.question_number += 1
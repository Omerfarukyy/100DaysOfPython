class QuizBrain:
    def __init__(self, question_list,):
        self.question_list = question_list
        self.question_number = 0

    def next_question(self):
        cq = self.question_list[self.question_number]
        input(f"Q.{self.question_number + 1}: {cq.text} (True/False)")

    def quiz(self):
        check = 0
        for question in self.question_list:
            answer = input(f"Q.{self.question_number + 1}: {question.text} (True/False)")
            if question.answer == answer:
                print("Your answer is true!")
                check += 1
                print(f"Your current score is:{check}/{self.question_number + 1}")
            else:
                print("Your answer is false!")
                print(f"Your current score is:{check}/{self.question_number + 1}")
            self.question_number += 1


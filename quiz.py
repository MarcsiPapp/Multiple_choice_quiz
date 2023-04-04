import csv
from question import Question


class Quiz:
    def __init__(self):

        self.questions = self.read_in_questions()
        self.score = 0

    def read_in_questions(self):

        # Reads in a list of Question objects from a csv file

        questions = []

        with open("questions.csv") as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=",")

            for row in csv_reader:
                # Get the prompt and answers form the row of the csv
                prompt = row[0]
                answers = row[1:]

                # Create a question object and add it to our list
                question = Question(prompt, answers)
                questions.append(question)

        return questions

    def run_quiz(self):

        # Loops through the questions and asks the user for an answer
        for question in self.questions:
            print("\n" + question.prompt)
            for i, answer in enumerate(question.answers):
                print(index_to_letter(i) + ": " + answer[0])
            print()

            # Get a valid answer from the user
            while True:
                response = input(":")
                try:
                    response = response.upper()
                    if response in [index_to_letter(i) for i in range(len(question.answers))]:
                        break
                    else:
                        print("Invalid response. Please try again.")

                except AttributeError:
                    print("Invalid response. Please try again.")

            
            # Check if the answer is correct and update the score
            if question.answers[letter_to_index(response)][1]:
                self.score += 1
                print("\nCorrect answer! Keep going!")
            else:
                print( f"\nWrong answer! Better luck next time!\nCorrect answer: {question.correct_answer}" )


        # Print the final score
        print("You got " + str(self.score) + "/" + str(len(self.questions)) + " correct")


### Helpers

# These functions transform a list index to the corresponding capital letter and back
def index_to_letter(index):
    return chr(65 + index)

def letter_to_index(letter):
    return ord(letter) - 65


if __name__ == "__main__":
    quiz = Quiz()
    quiz.run_quiz()

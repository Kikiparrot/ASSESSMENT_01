import math
import random


# Check that users have entered a valid answer

def yes_no(yes_no_question):
    """Checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:
        response = input(yes_no_question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes / no")


def one_two_three(one_two_three_question):
    """Checks user response to a question is one, two, or three to decide which game code to follow"""
    while True:
        response = input(one_two_three_question).lower()

        # check the user says yes / no
        if response == "1":
            return "one"
        elif response == "2":
            return "two"
        elif response == "3":
            return "three"
        else:
            print("please answer one / two / three")


def instruction():
    """prints instructions for users"""

    print("""
    *** Instructions ***

    Answer basic math questions
    from multiplication to addition and subtraction!
    examples include:
    1+1! which is not 11 or window but 2!!
    2+2! which is not fish but 4!!
    3x3! which is not 6 but 9!!
    
    if questions are too hard please try an easier version
    if questions are too easy please try a harder version
    if questions are still too easy please play a different game

         """)


def int_check(question, integer=None, exit_code=None):
    """ checks that integers are added and put into a proper order
    e.g. 1, 2 instead of 2, 1"""

    # if any integer is allowed

    while True:
        response = input(question).lower()

        if integer is None and int == "":
            error = "please enter an integer"
            print(error)

        # exit code
        if response == 'xxx':
            return response, exit_code

        try:
            response = int(response)

            # integer is  too low
            if integer is None and int == "":
                error = "please enter an integer"
                print(error)
                continue

            elif integer is not None:
                return response
            # valid response
            else:
                return response

        except ValueError:
            error = "please enter an integer"
            print(error)


def generate_question():
    """generates random math questions that range from addition, subtraction, and multiplication
     and provides an answer"""
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    quiz_type = random.choice(['+', '-', '*'])
    quiz_question = f"{num_1} {quiz_type} {num_2}"


    if quiz_type == '*':
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 20)
        quiz_question = f"{num_1} x {num_2}"
        quiz_answer = num_1 * num_2

    if quiz_type == '-':
        num_1 = random.randint(50, 100)
        num_2 = random.randint(1, 50)
        quiz_question = f"{num_1} - {num_2}"
        quiz_answer = num_1 - num_2

    if quiz_type == '+':
        quiz_question = f"{num_1} + {num_2}"
        quiz_answer = num_1 + num_2

    return quiz_question, quiz_answer


def generate_question_unrestrained():
    """generates harder math questions for users"""
    num_1 = random.randint(1, 500)
    num_2 = random.randint(1, 500)
    quiz_type = random.choice(['+', '-', '*'])

    quiz_question = f"{num_1} {quiz_type} {num_2}"
    
    if quiz_type == '*':
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        quiz_question = f"{num_1} x {num_2}"
        quiz_answer = num_1 * num_2

    elif quiz_type == '-':
        num_1 = random.randint(500, 1000)
        num_2 = random.randint(1, 500)
        quiz_question = f"{num_1} - {num_2}"
        quiz_answer = num_1 - num_2

    elif quiz_type == '+':
        quiz_question = f"{num_1} + {num_2}"
        quiz_answer = num_1 + num_2

    return quiz_question, quiz_answer


def generate_question_baby():
    """generates easier questions for users"""

    num_1 = random.randint(1, 20)
    num_2 = random.randint(1, 20)
    quiz_type = random.choice(['+', '-', '*'])

    quiz_question = f"{num_1} {quiz_type} {num_2}"

    if quiz_type == '*':
        num_1 = random.randint(1, 10)
        num_2 = random.randint(1, 5)
        quiz_question = f"{num_1} x {num_2}"
        quiz_answer = num_1 * num_2

    if quiz_type == '-':
        num_1 = random.randint(10, 30)
        num_2 = random.randint(1, 10)
        quiz_question = f"{num_1} - {num_2}"
        quiz_answer = num_1 - num_2

    if quiz_type == '+':
        quiz_question = f"{num_1} + {num_2}"
        quiz_answer = num_1 + num_2

    return quiz_question, quiz_answer


# main routine
print()
print("WELCOME TO SAPPHIRES CUTESY BASIC FACTS GAME. \n"
      "LEARN YOUR FACTS (basic ones) \n"
      "                 (or not basic ones!!)"
      "\n"
      "\n"
      "no exit code just press terminate")
print()

# check if user wants to see instructions
want_instructions = yes_no("do you want to see the instructions? ")
if want_instructions == "yes":
    instruction()

quiz_type = one_two_three("do you want to play restrained, unrestrained, or baby mode? \n"
                          "(1, 2, 3) \n"
                          "")

# game variables
mode = "regular"
questions_answered = 0
right_ans = 0
wrong_ans = 0
end_quiz = "no"
feedback = ""
history_feedback = ""
all_scores = []
game_history = []
user_answer = ""
# checks number of questions generated
num_rounds = int_check("How many questions would you like to do? ",
                       integer=1,)

# main code
while questions_answered is not num_rounds:
    # can leave if user desires

    if end_quiz == "yes":
        break


    rounds_heading = f"\n🌜🌜🌜 question {questions_answered + 1} of {num_rounds} 🌛🌛🌛"
    print(rounds_heading)
    print()
    # quiz type one is normal mode, no
    #t too hard, not too easy

    if quiz_type == "one":
        question, answer = generate_question()
        print(question)
        print(answer)
        print(".")

        user_answer = int_check('')
        if user_answer == 'x':
            end_quiz = "yes"

        if user_answer == answer:
            feedback = "correct"

        elif user_answer is not answer:
            feedback = "incorrect"
            print("never in my 15 years...")

        if user_answer is answer:
            right_ans += 1
        elif user_answer is not answer:
            wrong_ans += 1

    # quiz type two is hard mode
    elif quiz_type == "two":
        question, answer = generate_question_unrestrained()
        print(question)
        print(answer)

        user_answer = int_check("")
        if user_answer == 'x':
            end_quiz = "yes"

        if user_answer == answer:
            feedback = "correct"
            right_ans += 1

        if user_answer is not end_quiz and user_answer is not answer:
            feedback = "incorrect"
            print("never in my 15 years...")
            wrong_ans += 1

    # quiz type three is easy mode
    elif quiz_type == "three":
        question, answer = generate_question_baby()
        print(question)
        print(answer)

        user_answer = int_check("")
        if user_answer == "x":
            end_quiz = "yes"

        if user_answer == answer:
            feedback = "correct"

        elif user_answer is not answer:
            feedback = "incorrect"
            print("never in my 15 years...")
        if user_answer == answer:
            right_ans += 1
        elif user_answer is not answer:
            wrong_ans += 1

    # see if user answer is right or wrong and makes feedback

    questions_answered += 1
    print(feedback)

    # adds feedback to game history
    game_history.append(feedback)

if questions_answered > -1:
    see_history = yes_no(" \ndo you want to see your game history?")
    if see_history == "yes":
        for item in game_history:
            print(item)

    correct_ans = questions_answered - wrong_ans
    percent_won = round(right_ans / questions_answered * 100)
    percent_lost = round(wrong_ans / questions_answered * 100)
    print("+++ game statistics +++")
    print(f"won: {percent_won:.2f}% \t "
          f"lost: {percent_lost:.2f}% \t ")
else:
    print(":(")

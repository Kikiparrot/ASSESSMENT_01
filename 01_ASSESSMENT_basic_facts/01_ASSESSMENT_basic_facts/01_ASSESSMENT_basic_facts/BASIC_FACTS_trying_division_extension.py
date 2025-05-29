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
    """Checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:
        response = input(one_two_three_question).lower()

        # check the user says yes / no
        if response == "1":
            return "one"
        elif response == "2":
            return "one"
        elif response == "3":
            return "one"
        else:
            print("please answer one / two / three")


def instruction():
    """prints instructions for users"""

    print("""
    *** Instructions ***

    Answer basic math questions
    from multiplication and division to addition and subtraction!
    examples include:
    1+1! which is not 11 or window but 2!!
    2+2! which is not fish but 4!!
    3x3! which is not 6 but 9!!
    
    when doing division questions please round
    please.

         """)


def int_check(int_question, low=None, high=None, exit_code=None):
    """ checks that integers are added and put into a proper order
    e.g. 1, 2 instead of 2, 1"""

    # if any integer is allowed
    if low is None and high is None:
        error = "please enter an integer"

    # if the number needs to be more than an
    # integer (ie: rounds / 'high number')
    elif low is not None and high is None:
        error = ("please enter an integer that is "
                 f"more than / equal to {low}")

    if int == '':
        error = "please enter an integer"
    while True:
        response = input(int_question).lower()

        # exit code
        if response == exit_code:
            return response

        try:
            response = int(response)

            # integer is not too low
            if low is not None and response < low:
                print(error)
                continue

            # response is more than low number
            elif high is not None and response > high:
                print(error)
                continue

            # valid response
            else:
                return response

        except ValueError:
            print(error)


def generate_question():
    """generates random math questions that range from addition, subtraction, multiplication, and division
     and provides an answer"""

    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    quiz_type = random.choice(['/'])
    quiz_question = f"{num_1} {quiz_type} {num_2}"
    if quiz_type == '/' and num_1 == 0:
        random.randint(1, 10)

    if quiz_type == '/':
        quiz_answer_1 = num_1
        quiz_answer_2 = num_2
        quiz_answer_3 = quiz_answer_1 * quiz_answer_2
        quiz_answer = quiz_answer_3 / quiz_answer_2

        quiz_question = f"{quiz_answer} / {quiz_answer_2}"

    return quiz_question, quiz_answer


# main routine
print()
print("WELCOME TO SAPPHIRES CUTESY BASIC FACTS GAME. \n"
      "LEARN YOUR FACTS (basic ones) \n"
      "                 (or not basic ones!!)")
print()

quiz_type = one_two_three("do you want to play restrained, unrestrained, or baby mode? \n"
                          "(1, 2, 3) \n"
                          "")
# game variables
questions_answered = 0
right_ans = 0
wrong_ans = 0
end_quiz = "no"
feedback = ""
history_feedback = ""
all_scores = []
game_history = []
# checks number of questions generated
num_rounds = 10
# unfinished

#
while questions_answered is not num_rounds:
    # can leave if user desires
    if end_quiz == "yes":
        break

    # Rounds Heading

    rounds_heading = f"\n🌜🌜🌜 question {questions_answered + 1} of {num_rounds} 🌛🌛🌛"
    print(rounds_heading)

    # quiz type one is normal mode, not too hard, not too easy
    if quiz_type == "one":
        quiz_question, quiz_answer = generate_question()
        print(quiz_question)
        print(quiz_answer)
        print(".")
        user_answer = int(input(""))

        if user_answer == quiz_answer:
            feedback = "correct"

        elif user_answer is not quiz_answer:
            feedback = "incorrect"
            print("never in my 15 years...")
        if user_answer is quiz_answer:
            right_ans += 1
        elif user_answer is not quiz_answer:
            wrong_ans += 1

    # see if user answer is right or wrong and makes feedback

    questions_answered += 1
    print(feedback)

    # adds feedback to game history
    game_history.append(feedback)

if questions_answered > 0:
    see_history = yes_no(" \ndo you want to see your game history?")
    if see_history == "yes":
        for item in game_history:
            print(item)
    correct_ans = questions_answered - wrong_ans
    percent_won = round(right_ans / questions_answered * 100)
    percent_lost = round(wrong_ans / questions_answered * 100)
    print("+++ game statistics +++")
    print(f"won: {percent_won:.2f} \t "
          f"lost: {percent_lost:.2f} \t ")

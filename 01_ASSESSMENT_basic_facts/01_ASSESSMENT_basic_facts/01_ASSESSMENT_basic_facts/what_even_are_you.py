import random


# Check that users have entered a valid answer

def yes_no(question):
    """Checks user response to a question is yes/no (y/n), returns 'yes' or 'no'"""
    while True:
        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please answer yes / no")


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
    
    please dont pick multiplication or division haha
    
    please.

         """)


def int_check(question, low=None, high=None, exit_code=None):
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

    # number between low and high
    else:
        error = ("please enter an integer that"
                 f" is between {low} and {high} (inclusive)")
    while True:
        response = input(question).lower()

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


def quiz_type(addition, subtraction, multiplication, division):
    while True:
        response = ""
        if response == 1:
            return addition
        if response == 2:
            return subtraction
        if response == 3:
            return multiplication
        if response == 4:
            return division

        else:
            return "please input the type or the initial"
# main routine
print()
print("WELCOME TO SAPPHIRES CUTESY ADDITION GAME. \n"
      " I WILL ADD DIFFERENT ONES LATER!!!!!!!!!!!!! \n"
      "LEARN YOUR FACTS (basic ones)")
print()

quiz_type(addition=1, subtraction=2, multiplication=3, division=4)
quiz_q = "what quiz type do you want to play \n" \
         "1 for add \n" \
         "2 for sub \n" \
         "3 for mul \n" \
         "4 for div \n"

print(quiz_q)



want_instructions = yes_no("do you want to see the instructions? ")
if want_instructions == "yes":
    instruction()
else:
    print("okay")
# variables???????????????????? I don't know hahahahahahahaha. kms.
questions_answered = 0
right_ans = 0
wrong_ans = 0
end_quiz = "no"
feedback = ""
history_feedback = ""
all_scores = []
game_history = []
# left blank
# FOR NOW!!!!!!


num_rounds = int_check("How many questions would you like to do? ",
                       low=1, exit_code="")

while num_rounds < questions_answered:
    if quiz_q == 1:

        # random integer between low_num and high_num
        if end_quiz == "yes":
            break
        # Rounds Heading
        # no infinite mode we don't accept indecisive people
        # "quiz question 1" will be what the rounds component looks like

        rounds_heading = f"\n🌜🌜🌜 question {questions_answered + 1} of {num_rounds} 🌛🌛🌛"

        print(rounds_heading)
        print()

        add_num_1 = random.randint(1, 10)
        add_num_2 = random.randint(1, 10)
        add_answer = add_num_1 + add_num_2

        addition = f"what is {add_num_1} + {add_num_2}"
        print(addition)
        user_choice = addition

        correct_add_ans = add_answer
        user_ans = int(input("your answer : "))
        print(user_ans)

        if user_ans == correct_add_ans:
            feedback = "correct!!!!!!!!"

        else:
            feedback = "wrong :("

        print(feedback)

        questions_answered += 1

    if quiz_q == 2:
        print("still being constructed")


    if quiz_q == 3:
        print("still in construction")

    if quiz_q == 4:
        print("still in progress")
# set and code random math questions that HAVE RIGHT ANSWERS and do not involve decimal places
# (IMPORTANT!!!!!!)
# HOW TF DO I DO THIS !!!!


# like this guide I found online that goes like this:
# Generate two random numbers first.
# Put the two random numbers into a simple math equation,
# which can be addition, subtraction, multiplication or division. Calculate the equation and verify user input.
# Avoid errors such as division by zero.


# if user gets question right celebrate if user gets question wrong add to bad score list and say
# "you got it wrong, never in my fifteen years of being a computer program have I seen an answer this wrong"
# then continue program / quiz

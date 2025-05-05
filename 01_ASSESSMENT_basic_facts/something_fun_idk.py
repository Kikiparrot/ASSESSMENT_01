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

    Form a loop in the end of the rope. Tuck a bight of the standing end through the loop.
    
    Make the bight larger and pass it around the object. 
    
    Pull on the standing end to tighten the noose.

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


# main routine


# check if user wants instructions
want_instructions = yes_no("do you want to see the instructions? of how to tie a noose")
if want_instructions == "yes":
    instruction()

while want_instructions == "yes":
    ask_question = yes_no("would you want to perchance do this knot on yourself")
    if ask_question == "yes":
        print("GREAT CHOICE ME TOO")
        break

    else:
        print("sorry wrong answer bro")

else:
    print("okay but ur missing out fr")

    ask_question = yes_no("do you like apples and bananas")

    if ask_question == "yes":
        print("YES THAT'S THE RIGHT ANSWER CONGRATULATIONS WOOHOO")

    else:
        print("you suck and I hate you")

while ask_question == "yes":

    final_question = yes_no("okay okay whatever that doesn't matter "
                            "would you,,, perchance,, commit a beautiful symbolic double suicide with me")

    print("...")

    if final_question == "yes":
        print("okay okay YES LET'S GO I DON'T WANT TO DO MY ASSESSMENT"
              " THIS IS HEAVEN")
        print("I look you in the eyes as we both stand side by side on the edge of a cliff   \n" 
              " the careful wind caresses us as we both stare into the mournful sunset,   \n" 
              " a bird caws overhead but we do not care, overwhelmed with sorrow    \n"
              "for death, the plague of life matters not   \n"
              "life is misery but death is deliverance \n"
              "the only sensation the clasp of our hands"
              " it feels like a dream, the end is in sight \n"
              " there is nothing that can touch our broken souls now \n"
              " no malicious world to tear us from deaths sugar sweet embrace \n"
              "it would be comforting if not so cold, but humans feel not in death \n"
              
              "we both glance at each-other, the setting sun the only witness to our salvation \n"
              "misery has brought us here and misery will be the one to grant us freedom. \n")
        print(".")
        print(".")
        print("we both plunge into the grief-soaked sun")
        break

    elif final_question == "no":
        print("...")
        print("...")
        print("...")
        print("excuse me..? I thought I heard that wrong, you mean yes right?")

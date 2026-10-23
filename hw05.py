"""
Name: Eleni Kahsay Elias (Ella)
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """ Checks if the length is one character and is A or B or C """
   
    user_input = input("Give an single uppercase letter: ")
    while True:
        if len(user_input) == 1:
            if user_input == 'A' or user_input == 'B' or user_input == 'C' :
                return user_input
            else:
                print("Error: You provided the wrong character.")
                user_input = input("Give an single uppercase letter: ")
                continue
        else:
             print("Error: it needs to be a single character.")
             user_input = input("Give an single uppercase letter: ")
             continue
    

def get_digit():
    """ Checks if the length is one character and is 1 or 2 or 3 """
   
    user_input = input("Give an single number character: ")
    while True:
        if user_input.isdigit():
            if user_input == '1' or user_input == '2' or user_input == '3':
                return user_input
            else:
                print("Error: a single digit needs to be in [1,3].")
                user_input = input("Give an single number character: ")
                continue
        else:
            print("Error: your input should be only digits.")
            user_input = input("Give an single number character: ")
            continue
    


def check_pattern(letter, digit, lst):
    """Print strings where the letter comes before the digit."""
    print("Strings with the pattern:")

    for result in lst:
        found_letter = False

        for character in result:
            if character == letter:
                found_letter = True

            if character == digit and found_letter:
                print(result, end=" ")
                break

    print()


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    
    while True:
    
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter, digit, st_list)
        
        try_again = input("Try Again? (y/n): ")
        if try_again != 'y':
            break

    # Your code Here

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()
import random

# This will display the introduction
def display_intro():
    title = "** Welcome to my Number Quiz! **"
    print("*" * len(title))
    print(title)
    print("*" * len(title))

# This displays the math topics
def display_menu():
    menu_list = ["1. Addition", "2. Subtraction", "3. Multiplication", "4. Integer Division", "5. Abort"]
    print(menu_list[0])
    print(menu_list[1])
    print(menu_list[2])
    print(menu_list[3])
    print(menu_list[4])


def display_separator():
    print("-" * 24)

# This will determine the users answer on the menu
def get_user_input():
    user_input = int(input("Enter your choice: "))
    while user_input > 5 or user_input <= 0:
        print("Invalid menu option.")
        user_input = int(input("Please try again: "))
    else:
        return user_input


# This part will ask the user for his response on the question asked
def get_user_solution(problem):
    print("Enter your answer")
    print(problem, end="")
    result = int(input(" = "))
    return result

# This will check if the user got the answer correct or not
def check_solution(user_solution, solution, count):
    if user_solution == solution:
        count = count + 1
        print("Correct.")
        return count
    else:
        print("Incorrect.")
        return count

# This is the part of the code that defines the menu options
def menu_option(index, count):
    number_one = random.randrange(1, 21)
    number_two = random.randrange(1, 21)
    if index == 1:
        problem = str(number_one) + " + " + str(number_two)
        solution = number_one + number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 2:
        problem = str(number_one) + " - " + str(number_two)
        solution = number_one - number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    elif index == 3:
        problem = str(number_one) + " * " + str(number_two)
        solution = number_one * number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count
    else:
        problem = str(number_one) + " // " + str(number_two)
        solution = number_one // number_two
        user_solution = get_user_solution(problem)
        count = check_solution(user_solution, solution, count)
        return count

#This prints the total amount of question the user has gotten incorrect or correct
def display_result(total, correct):
    if total > 0:
        result = correct / total
        percentage = round((result * 100), 2)
    if total == 0:
        percentage = 0
    print("You answered", total, "questions with", correct, "correct.")
    print("Your score is ", percentage, "%. Thank you.", sep = "")

# These are the main routines for the quiz
def main():
    display_intro()
    display_menu()
    display_separator()

    option = get_user_input()
    total = 0
    correct = 0
    while option != 5:
        total = total + 1
        correct = menu_option(option, correct)
        option = get_user_input()

    print("Exit the quiz.")
    display_separator()
    display_result(total, correct)

main()

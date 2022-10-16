def question():

    while not valid:
        valid = False


    print("Enter a times table that you would like to be tested on: ")

    times_table = int(input())
    answer = 0
    print("Enter the maximum value for your times table: ")
    range_max = int(input()) + 1

    print(f"Here is your quiz on the {times_table} times table")
    for x in range(1, range_max):
                answer = x * times_table
                print(f"{x} times {times_table} is...")
                user_answer = int(input("Answer: "))

                if user_answer == answer:
                    print("Correct!")
                else:
                    print("Incorrect")

#ask the user if they have played before or not
def yes_no(question):
   valid = False
   while not valid:

       response = input(question).lower()

       if response == "yes" or response == "y":
           response = "yes"
           return response
       elif response == "no" or response =="n":
           response = "no"
           return response
       else:
           print("Please enter Yes or No: ")
#will display instructions depending on yes_no checker
def instructions():
   print("***************************")
   print("        How to Play")
   print("***************************\n")
   print("""Welcome to the Math Quiz!
   
   
Here we will test your knowledge of this wonderful game
Are you good with numbers? Lets hope so!
\n""")
   return ""

print("Welcome to my Number Quiz!")
print()
played_before = yes_no("Have you played the game before? ")

if played_before == "no":
   instructions()

#will check the users answer for the question
def num_check(question):
   error = "Please enter a whole number between 1 and 10"
   valid = False
   while not valid:
       try:
           response = int(input(question))

           if response <= 0 or response > 10:
               print(error)
           else:
               print(f"You are playing with ${response}")
               valid = True
               return response
       except ValueError:
               print(error)


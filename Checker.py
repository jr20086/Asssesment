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

def instructions():
   print("*** Quiz of Minecraft ***\n")
   print("""Welcome to The Minecarft, the cost is $1 per round to
play.
If you get a Unicorn you win $5.
If you receive a Horse or Zebra you win 50c.
A Donkey gets you nothing.
Good Luck!\n""")
   return ""

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


print("Welcome to the Lucky Unicorn Game!")
print()
played_before = yes_no ("Have you played the game before? ")

if played_before == "no":
   instructions()

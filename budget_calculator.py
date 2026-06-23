#defines a function to obtain a number with or without a decimal
#we will use this function multiple times in our program
def collect_number():
  while True: #while loop to keep asking for a number until we get a valid one
    number = input("Please enter a number in $USD:\n")
    try:
      digit = float(number) #float rather than int to allow for decimals
      return digit #if valid number is found value is retunred to collect_number
    except:
      print('\n' + "Please enter numbers only") #reruns loop if input is not a valid number

print("Welcome to your new budget!\n")
print("Let's take a look at your income.")
income = collect_number() #calls function to run again for valid number
print("\n" + "Great! Your total income is $"+ str(income) + "\n") #line spacing using \n for visual appeal in output
print("Now let's calculate your bills...\n") #output display to begin asking user for bills

def get_expenses(): #calls function to collect values on multiple expenses
  print("Let's take a look at your rent:")
  rent = collect_number() #again we will call our function to obtain valid number
  print('\n' + "Great! Next let's take a look at your utilities:")
  utilities = collect_number()
  print('\n' + "Next up we'll look at your groceries:")
  groceries = collect_number()
  print('\n' + "Finally we'll take a peak at your transportation costs:")
  transportation = collect_number()
  #here we will calculate total of all expenses 
  total_expenses = rent + utilities + groceries + transportation
  print('\n' + "Great! Your total expenses are $"+ str(total_expenses) + "\n") #display output of total expenses
  return total_expenses #Return value to get_expenses

budget_balance = float(income) - get_expenses()
#we use if, elif, and else statements to determine users financial standing and display statment based on results with remaining balance
if budget_balance > 0: #if value is greater than 0, we have a positive remaining balnce
  print("--Awsome! You're on track with a remaining balance of $"+ str(budget_balance) + "--")
elif budget_balance == 0: #if value is equal to 0, we broke even
  print("--Careful! You broke even with $0 left over in your budget!--")
else: #all remaining, we are overbudget and will result in a negative balance
  print("--Oh no! You're in debt with a balance of $"+ str(budget_balance) + "--")

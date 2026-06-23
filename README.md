# Personal Budget Calculator

•	In this program we will be developing code to generate a personal budget, useful for consolidating multiple inputs such as expenses and incomes into a program which tracks our financial standing. 

•	This program will depend on user inputted data including income and expenses. 

•	The user will input these values, continuing to interact with the program adding expenses, incomes and their descriptions. The program will subtract all expenses from all incomes. 

•	The program will continue to run while the user adds additional info, finalizing with a summary of their budget. 

# Working Through Specific Examples

Positive remaining budget balance:

•	A user inputs an income (i.e. $1000). This could be an example of their monthly income. Now we will add expenses individually. These could include things such as bills, groceries, rent and so on. Let’s say our user enters $250 for rent, $100 for groceries and $75 for dining out. The program will subtract these expenses from our income data to compile a resulting value. If the user chooses to show a summary of their budget, the result will show that they have a remaining balance of $575. 

Negative remaining budget value:

•	Let’s assume our user inputs the same income of $1000. However, they then input additional expenses such as a $600 auto loan payment. In this case, the program will still subtract all expenses from our income data however will return a value of negative 25 dollars. 


We will need to spend some additional time, however adding code which would return a statement based on either a positive or negative return value could be useful to the user. This could be “You’re on track” for a positive value and returning “You’ve overspent” if our value returns negative.

# Pseudocode

Display initial welcome screen

Request for user input of income in dollars and decimal format

- Collect number using code which requires numbers and decimals only. (We will use this process multiple times and may create a reusable code)
     
Display confirmation of total income with dollar sign

Display request for bills

- Request rent input (using digit required input based on reusable code)

- Request utilities input (using digit required input based on reusable code)
     
- Request groceries expenses (using digit required input based on reusable code)
     
- Request transportation costs (using digit required input based on reusable code)
     
- Calculate combined bills 
     
- Display confirmation of total combined bills
     
Calculate budget balance based on total income – total expenses

Display final balance

Statement based on result

- If positive statement of remaining balance and on budget
     
- If negative statement of negative balance and going overbudget
     

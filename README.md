# Budget
Simple budget program with a concept similar to EveryDollar and Goodbudget, but totally free and it tracks total money rather than by month.

# How to use

Download 
 * budget_gui.py
 * budget.py
 * dollar_icon.py
and put them all in the same folder. Open budget.py and replace the main and sub accounts with your own personal accounts. Make sure that the name of each account is the same as the variable for the account/subaccount. Open budget_gui.py and replace ic with the path to the dollar_icon.py file. 

Create a google spreadsheet document called budgeet_py. On the first sheet, put headings for " Date	amount	Description	subaccount	Subtotal	Main name	Main total"
and open a second sheet. On the second sheet, fill the first column with letter values and the second column with number values as placeholders. Run the budget_gui.py file from the command line and wait until the window pops up. Input any transaction or tansfer, then go back to the second page of the google sheet. to the right of each title, input the actual initial values of your subaccounts and delete the fillers you had added. Delete the test tranfer/transaction. And that's it! youre done! Run the budget_gui.py file from the command line any time you want to transfer money back and forth between subaccounts. The program will keep a running total of how much in each account and a receipt for each transfer and transaction.

# to do
* package the program to a .exe
* let the program write to multiple sheets without hardcoding
* maybe make a mobile app

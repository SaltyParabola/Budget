# Budget
Simple budget program with a concept similar to EveryDollar and Goodbudget, but totally free and it tracks total money rather than by month.

# Getting started

Download 
 * budget_gui.py
 * budget.py
 * dollar_icon.py
and put them all in the same folder. Open budget.py and replace the main and sub accounts with your own personal accounts. Make sure that the name of each account is the same as the variable for the account/subaccount. Open budget_gui.py and replace ic with the path to the dollar_icon.py file. 

Create a google spreadsheet document called budget_py. On the first sheet, put headings for " Date,	amount,	Description,	subaccount,	Subtotal,	Main name,	Main total" in that order and open a second sheet. On the second sheet, fill the first column with letter values and the second column with number values as placeholders. Follow along with this tutorial(or a similar one): https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
to get google sheets talking with the program. Run the budget_gui.py file from the command line and wait until the window pops up. Input any transaction or tansfer, then go back to the second page of the google sheet. to the right of each title, input the actual initial values of your subaccounts and delete the fillers you had added. Delete the test tranfer/transaction. And that's it! youre done! Run the budget_gui.py file from the command line any time you want to transfer money back and forth between subaccounts. The program will keep a running total of how much in each account and a receipt for each transfer and transaction.

## Use

Transactions are withdrawals from or deposits into your subaccounts. Transfers go between different subaccounts, and will give receipts that look like two transfers in a row.
When making a transaction, **make sure you get the sign right.** A negative sign means you're making a withdrawal, while no sign (a positive number) makes a deposit. Don't use a negative sign when making a transfer.

When selecting an account and a subaccount, make sure that the subaccount you've selected belongs to the main account you've selected. Currently selection of the main account doesn't change the drop downs for the subaccounts, so no matter what you choose you can select any subaccount. If you select a subaccount that doesn't match with the main account you've chosen, you'll probably get an error.

### Optional
Make a .bat file that has the path to python followed by the path to the file budget_gui.py. It'll be the exact same thing you would type into the command prompt to start the program. You can just make it in notepad and save it with a .bat extension--then you can just click on the .bat file and it'll run the program.

# to do
* figure out and fix why it runs so slowly
* make selection of main account determine selection of subaccount
* make initialization of accounts a little easier
* package the program to a .exe
* let the program write to multiple sheets without hardcoding
* maybe make a mobile app

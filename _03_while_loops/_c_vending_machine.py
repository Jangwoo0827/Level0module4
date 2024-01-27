"""
Calculate the value of the change (coins) the user has.
"""
from tkinter import messagebox, simpledialog, Tk

qwe = 0

# Write you code under the if __name__ == '__main__': below
def vending_machine(money):
    global qwe
    items_for_sale = {"water" : 0.50, "soda" : 1.00, "pretzels" : 1.00, "candy bar" : 1.50, "exit" : 0.00}

    while True:
        intro_str = "Welcome to the vending machine! You have " +\
                    str("{:.2f}".format(money)) + " dollars left.\n"
        intro_str += "Enter the item you want to buy?\n"

        for item, cost in items_for_sale.items():
            intro_str += item + ' - $' + str("{:.2f}".format(cost)) + '\n'

        item_num = simpledialog.askstring(title='Vending Machine', prompt=intro_str)

        # Cancel button pressed
        if item_num is None:
            return 0.00
        elif item_num in items_for_sale:
            return items_for_sale[item_num]
        else:
            messagebox.showwarning('Invalid item',
                                   'Please enter one of the following ' + str([item for item in items_for_sale]))
            qwe = qwe + 1
            if qwe == 5:
                messagebox.showwarning(title=None, message="You just canceled 5 times.")
            if qwe == 10:
                messagebox.showwarning(title=None, message="Stop. You just canceled 10 times.")
            if qwe == 15:
                messagebox.showwarning(title=None, message="Okay. Get out. You just canceled 15 times.")
                break

# ======================= DO NOT EDIT THE CODE ABOVE =========================


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    money_in_dollars = 3.00

    # TODO) Write a while loop that ends when you have no money left
    while money_in_dollars > 0:
        # TODO) Call the vending_machine() function and save the money spent
        #  in a variable, for example:
        #  money_spent = vending_machine(money_in_dollars)
        money_spent = vending_machine(money_in_dollars)
        # TODO) If no money was spent, tell the user how much money they still
        #  have and exit the while loop
        if money_spent == 0:
            break
        # TODO) Otherwise, subtract the money spent from the amount of money
        #  you still have (money_in_dollars)
        if money_spent > 0:
            money_in_dollars = money_in_dollars - money_spent
    # TODO) If there is exactly 0 money left, create a message that
    #  congratulates the user because they maximized their money.
        if money_in_dollars == 0.00:
            messagebox.showinfo(title=None, message="You maximized your money.")
    # TODO) If there is a negative amount of money, tell the user they
    #  overspent!
        if money_in_dollars < 0.00:
            messagebox.showwarning(title=None, message="You overspent your money.")

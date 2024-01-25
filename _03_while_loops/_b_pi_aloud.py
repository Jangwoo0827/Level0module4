"""
Use a while loop to recite the digits of pi
"""
from tkinter import messagebox, simpledialog, Tk
import math


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    # TODO) Place the first 20 digits of pi into a variable as a string
    #     #  3.1415926535897932384
    pi = 3.1415926535897932384
    pi_str = str(pi)
    n = 0
    # TODO) Print out the first 3 digits of pi. For example,
    #  pi_str[0]   # first digit
    #  pi_str[1]   # second digit
    messagebox.showinfo(title="PI", message=pi_str[0])
    messagebox.showinfo(title="PI", message=pi_str[1])
    messagebox.showinfo(title="PI", message=pi_str[2])
    messagebox.showinfo(title="PI", message=pi_str[3])
    n = 4
    # TODO) Use a while loop to keep asking for the next digit of pi
    while True:
        pie = simpledialog.askstring(title="PI", prompt="What is next digit of pi?")
        # TODO) If they are correct, print "correct".
        if pie == pi_str[n]:
            messagebox.showinfo(title="PI", message="Correct!")
            n = n + 1
        else:
            messagebox.showinfo(title="PI", message="Incorrect.")
            messagebox.showinfo(title="PI", message="You recited")
            messagebox.showinfo(title="PI", message=n)
            messagebox.showinfo(title="PI", message="digits of pi!")
            break
        #  If they are not, print "incorrect" and break out of the while loop


    # TODO) Print out how many digits of pi the user was able to recite
    #  in a row

"""
Write a program to return the correct letter grade
"""
from tkinter import simpledialog, Tk, messagebox
p = Tk()
# The teacher wants you to write a program that converts the score on 2
# 100 point tests to a letter grade. The teacher wants you to average the
# score from the 2 tests and print out the letter grade back to the user.
# The letter grades are assigned as follows:
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5

if __name__ == '__main__':
    # TODO) Ask the user for their score on the FIRST test and store their
    #  score in a variable
    q = simpledialog.askinteger(title="123123", prompt="What is your score in first test?")
    # TODO) Ask the user for their score on the SECOND test and store their
    #  score in a variable
    w = simpledialog.askinteger(title="123123", prompt="What was your score in second test?")
    # TODO) Take the average score of both tests (total score / 2)
    a = (q + w) / 2
    # TODO) Use if statements to check the average score and print the
    #  corresponding letter grade back to the user. Also, give a different
    #  message according to their grade. Example, for an 'A' grade:
    #  "Wow! You must have studied really hard for those tests!"
    if a >= 89.5 and a <= 100:
        messagebox.showinfo(title=None, message="Tests were easy, right?")
    if a > 79.5 and a < 89.5:
        messagebox.showinfo(title=None, message="You got low scores.")
    if a > 69.5 and a < 79.5:
        messagebox.showinfo(title=None, message="You are so bad at math.")
    if a > 59.5 and a < 69.5:
        messagebox.showinfo(title=None, message="Work hard for next tests.")
    if a <= 59.5:
        messagebox.showinfo(title=None, message="What did you do when others were studying?")
    if a == 123123:
        messagebox.showinfo(title=None, message="How did you find this?")
    pass
#   A = 89.5 to 100
#   B = 79.5 to less than 89.5
#   C = 69.5 to less than 79.5
#   D = 59.5 to less than 69.5
#   F = less than 59.5

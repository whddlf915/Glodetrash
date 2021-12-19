# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import turtle


def draw_pos(x, y):
    t.goto(x, y)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# password: str = ""
# while password != "python":
#     password = input("password : ")

print("ok")


colors = ["red", "purple", "blue", "green", "yellow", "orange"]

t = turtle.Turtle()
t.shape("turtle")

t.speed(0)
t.width(3)
# Press the green button in the gutter to run the script.


length = 5
i = 0
# print(colors(i % len(colors)))
while i < 80:
    t.forward(length)
    t.right(89)
    i = i + 1
    length += 5
    t.color(colors[i % len(colors)])


turtle.done()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

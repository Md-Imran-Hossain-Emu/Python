import re

print("Our Magical Calculator")
print("Type 'Quit' to Exit\n")

previous = 0
run = True

def performOperation():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter Equation: ")
    else:
        equation = input(str(previous))

    if equation == "Quit":
        print("GoodBye!")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)

while run:
    performOperation()
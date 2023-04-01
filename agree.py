from cs50 import get_string

s = get_string("Do you agree?\n")

if s in ["Y", "y", "Yes", "yes"]:
    print("Agreed")
elif s in ["N", "n", "No", "no"]:
    print("Not agreed")
else:
    print("Wrong input!!!!")        
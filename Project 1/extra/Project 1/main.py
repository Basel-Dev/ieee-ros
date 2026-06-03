import subprocess

print("Welcome to the Drone Dashboard. Enter one of the following keys to continue:\n\n")

print("a) Register New Drone/Package")
print("b) Set No-Fly Zone")
print("c) Start Flight Simulation")
print("d) Display \'Champions of Efficiency\'")
print("e) Exit")


while True:
    letter = input("Input: ")

    if len(letter) != 1 or letter.lower() not in list("abcde"):
        print("Invalid Input")
        continue;
    break;

match letter:
    case "a":
        pass

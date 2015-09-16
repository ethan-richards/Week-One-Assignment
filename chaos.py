__author__ = 'ethan.richards'

# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    loop = 20
    multiplier = 2.0
    print("This program illustrates a chaotic function")
    x = input("Enter a number between 0 and 1: ")
    for i in range(loop):
        x = multiplier * x * (1 - x)
        print(x)

main()

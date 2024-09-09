# Author: Seth Stemen
# FizzBuzz for Buckeye AutoDrive entrance exam

def main():
    for i in range(1, 251):
        output = ""
        if i % 3 == 0:
            output += "Fizz"
        if i % 5 == 0:
            output += "Fizzy"
        if i % 7 == 0:
            output += "Buzz"
        print(output or i)

if __name__ == "__main__":
    main()

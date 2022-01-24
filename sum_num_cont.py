# !/usr/bin/env python3
# Created By: Jedidiah.
# Date: Jan 18, 2022
# This program uses a while true loop to find the sum
# of numbers the user inputs.

def main():

    user_range = int(input("How many numbers do you want to add: "))
    count = 0
    num_sum = 0
    number = 1
    while number > 0:
        number_as_string = input("Enter a positive number: ")
        try:
            number_as_int = int(number_as_string)
            if number_as_int > 0:
                num_sum = num_sum + number_as_int
                print("{} was added to the sum".format(number_as_int))
            elif number_as_int <= 0:
                print("Your input is less than 0")
                continue
            if count  == user_range:
                break
            count = count + 1

        except Exception:
            print("invalid input")
    print("The total sum is {}".format(num_sum))
    print("Thanks for playing")


if __name__ == "__main__":
    main()
    
#!/user/bin/env python3
# created by : adrian student
# date : 22th sep 2026
# THis program asks the user for radius of
# a circle in mm . it then calculates
# the circumference using tau.
import constants


def main():
    # get radius from the user
    radius = float(input("Enter the radius of the circle in (mm): "))

    # calculate the circumference
    circumference = constants.TAU * radius

    # Display the circumference
    print("")
    print("circumference = {} mm".format(circumference))


if __name__ == "__main__":
    main()

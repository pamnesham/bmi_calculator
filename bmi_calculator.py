#!python3

#Ask the user to input their body measurements to calculate their bmi
def main():
    print("Enter your weight in pounds.")
    wt = int(input())
    print("Enter your height in inches.")
    ht = int(input())
    print("Enter your age in years.")
    age = int(input())
    print("Enter your gender using 'M' for male or 'F' for female.")
    gend = input()
    if gend.lower() == 'f':
        gend = 0

    result = bmr(wt, ht, age, gend)
    print(str(result) + " is your bmi.")

#The calculations for bmi based on gender
def bmr(wt, ht, age, gend):
    if gend == 0:
        numbars = (655+(4.3*wt) + (4.7*ht) - (4.7*age))/230
    else:
        numbars = (66+(6.3*wt) + (12.9*ht) - (6.8*age))/230
    return(numbars)


if __name__ == '__main__':
    main()

W = int(input("Please enter your Weight(kg):"))
H = float(input("Please enter your Height(Metres):"))

BMI = W / H ** 2


if BMI < 18.5:
    print("Your BMI is: " + str(BMI) + " You are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print("Your BMI is: " + str(BMI) + " You are at a normal weight.")
elif BMI >= 25 and BMI < 30:
    print("Your BMI is: " + str(BMI) + " You are overweight.")
else:
    print("Your BMI is: " + str(BMI) + " You are obese")

#Date
#Name
#This program works out what credit card a person is entitled to

age = int(input("What is your age? "))
income = int(input("What is your annual salary? "))

if age < 18:
    print("You are not eligible for a Credit Card")

elif age > 18 and income > 40000:
    print("You are eligible for a Credit card!")

elif age > 30 and 80000 > income > :
    print("You are entitled to a Gold Credit Card!!")


elif age > 40 and income > 120000:
    print("You are entitled to a Platinum Credit Card!!!")

else:
    print("Sorry you are not eligible for a Credit Card at the moment.")
    

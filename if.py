# A company decided to give a bonus of 5% to the employee if his/her years of service is more than 5 years. Ask the user for their salary and years of service and print the bonus amount.
salary = int(input("What is your salary? "))
years = int(input("How many years have you worked here? "))

if years >= 5:
    print(f"Your bonus will be {salary * 0.05}")
else:
    print("You do not qualify for a bonus.")
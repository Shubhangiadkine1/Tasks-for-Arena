
print("=" * 45)
print("       PERSONAL INTRODUCTION PROGRAM")
print("=" * 45)

# Collect user information
name = input("Enter your name: ").strip().title()
age = int(input("Enter your age: "))
city = input("Enter your city: ").strip().title()
hobby = input("Enter your favorite hobby: ").strip().title()
food = input("Enter your favorite food: ").strip().title()
subject = input("Enter your favorite subject: ").strip().title()
goal = input("What is your future goal? ").strip()

# Store interests in a list
interests = [hobby, food]

# Age category
if age < 0:
    print("Invalid age!")
elif age < 13:
    category = "Child"
elif age < 20:
    category = "Teenager"
else:
    category = "Adult"

# Display welcome message
if age >= 0:
    print("\n" + "=" * 45)
    print(f"       Welcome, {name}!")
    print("=" * 45)

    print(f"Name           : {name}")
    print(f"Age            : {age}")
    print(f"Age Category   : {category}")
    print(f"City           : {city}")
    print(f"Hobby          : {hobby}")
    print(f"Favorite Food  : {food}")
    print(f"Favorite Subject: {subject}")
    print(f"Future Goal    : {goal}")

    print(f"\nYour interests: {interests}")
    print(f"Next year, you will be {age + 1} years old.")

    print(f"\nKeep learning, {name}!")
    print("Believe in yourself and achieve your goals.")

    print("=" * 45)
    print("Thank you for using my program!")
    print("=" * 45)

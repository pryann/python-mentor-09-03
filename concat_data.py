firstName = "John"
lastName = "Doe"
age = 30

me = (
    "My name is " + firstName + " " + lastName + " and I am " + str(age) + " years old."
)
me_format = "My name is {} {} and I am {} years old.".format(firstName, lastName, age)
me_f = f"My name is {firstName} {lastName} and I am {age} years old."

print("My name is", firstName, lastName, "and I am", age, "years old.")

age_input = input("How old are you? ")

if age_input.isdigit():
    age = int(age_input)
    print("You are", age, "years old.")
else:
    print("Invalid input. Please enter a number.")

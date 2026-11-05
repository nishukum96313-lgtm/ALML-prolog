print("Welcome to Course Advisory System")
print("Choose your interest:")
print("1. Artificial Intelligence")
print("2. Python")
print("3. AIML")
print("4. Data Structure and Algorithm")

interest = input("Enter your interest: ")

if interest == "Artificial Intelligence" or interest == "1":
    print("Recommended Elective: Machine Learning")

elif interest == "Python" or interest == "2":
    print("Recommended Elective: Coding")

elif interest == "AIML" or interest == "3":
    print("Recommended Elective: Learning about agents")

elif interest == "Data Structure and Algorithm" or interest == "4":
    print("Recommended Elective: solving problems")

else:
    print("Sorry, no course recommendation available.")

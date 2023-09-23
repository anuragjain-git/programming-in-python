
marks = (float(input("Enter marks : ")))
grade = (input("Enter your Grade : "))[0]
post = (input("Enter your post : "))
experience = (int(input("Enter year of experience : ")))


# Mark

if marks >= 300 and marks <= 400 :
    print("Marks is greater than 300 and less than 400")
else :
    print("invalid marks")

# grade


if(grade.isupper()) :
    print("Upper Case")
else :
    print("Lower case")

# post

if(post == "engineer") :
    print("Valid Post")
else :
    print("Invalid Post")

# experience

if(experience >= 4) :
    print("Experience is more than 4 year")
else :
    print("Less Experience")

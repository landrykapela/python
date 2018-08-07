names =  list(input("Enter the students' names separated by commas(,):"))
assignments = list(input("Enter the students' missed assignments separated by commas(,) in the same order as names:"))
grades =  list(input("Enter the students' grades separated by commas(,) in the same order as names:"))

#print(len(names),len(assignments),len(grades))
# message string to be used for each student
# HINT: use .format() with this string in your for loop
for index in range(len(names)):
    name = names[index]
    grade = grades[index]
    assignment = assignments[index]
    potential_grade = grade + 2*assignment
    message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n".format(name,assignment,grade,potential_grade)
    print(message)
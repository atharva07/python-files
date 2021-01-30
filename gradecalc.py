# python code for grade calculator
# creating a dictionary which consists of students name
# their assignment result test result and lab result

# 1. Jack's dictionary
jack = {"name" : "Jack Dorsey",
        "Assignment" : [80,50,40,20],
        "Test" : [75,75],
        "Lab" : [77.20,75.44]
}

# 2. Martin's dictionary
martin = {"name" : "Martin Guptill",
          "Assignment" : [77,54,66,23],
          "Test" : [77,64], 
          "Lab" : [62.55,71.77]
}

# 3. Victor's Dictionary
victor = {"name" : "Victor Fernandes",
          "Assignment" : [56,63,87,45],  
          "Test" : [88,43],  
          "Lab" : [56.77,64.33]  
} 

# 4. Brayan's dictionary
brayan = {"name" : "Brayan simione",
          "Assignment" : [44,43,78,55],
          "Test" : [54,76],
          "Lab" : [45.55,65.77]
} 

# 5. Mason's dictionary
mason = {"name" : "Mason Mount",
         "Assignment" : [77,43,81,62],
         "Test" : [58,69],
         "Lab" : [56.33,44.77]
}

# function to get average
def get_average(marks):
    total_sum = sum(marks)
    total_sum = float(total_sum)
    return total_sum / len(marks)

# function calculates total average
def calculate_total_average(students):
    Assignment = get_average(students["Assignment"]) 
    Test = get_average(students["Test"])
    Lab = get_average(students["Lab"])

    return(0.1 * Assignment + 0.7 * Test + 0.2 * Lab)

# caluclate letter grade of students
def assign_letter_grade(score): 
    if score >= 90: return "A"
    elif score >= 80: return "B"
    elif score >= 70: return "C"
    elif score >= 60: return "D"
    else: return "E"

# function to calculate the total 
# marks of the average class
def class_average_is(student_list):
    result_list = []

    for students in student_list:
        stud_list = calculate_total_average(students)
        result_list.append(stud_list)
        return get_average(result_list)

# students list conisists 
# dictionary of all students
students = [jack,martin,victor,brayan,mason]

# printing the total average marks 
for i in students:
    print(i["name"])
    print("+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+")
    print("Average marks of %s is : %s " %(i["name"], calculate_total_average(i)))
    print("Letter grade of %s is : %s " %(i["name"],assign_letter_grade(calculate_total_average(i))))
    print()

# calculate the average of whole class 
class_av = class_average_is(students)

print( "Class Average is %s" %(class_av)) 
print("Letter Grade of the class is %s " 
        %(assign_letter_grade(class_av))) 

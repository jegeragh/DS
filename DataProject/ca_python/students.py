lloyd = {
    "name": "Lloyd",
    "homework": [90, 97, 75, 92],
    "quizzes": [88, 40, 94],
    "tests": [75, 90]
}
alice = {
    "name": "Alice",
    "homework": [100, 92, 98, 100],
    "quizzes": [82, 83, 91],
    "tests": [89, 97]
}
tyler = {
    "name": "Tyler",
    "homework": [0, 87, 75, 22],
    "quizzes": [0, 75, 78],
    "tests": [100, 100]
}

students = [lloyd, alice, tyler]

# Add your function below!
def average(list):
    sum = 0
    count = 0
    for item in list:
        sum += item
        count += 1
    return sum/count
    
def get_average(student):
    hw_sum = 0
    hw_count = 0
    
    q_sum = 0
    q_count = 0
    
    t_sum = 0
    t_count = 0
        
    for item in student["homework"]:
        hw_sum += item
        hw_count += 1
    hw_avg = hw_sum / hw_count
    
    for item in student["quizzes"]:
        q_sum += item
        q_count += 1
    q_avg = q_sum / q_count
    
    for item in student["tests"]:
        t_sum += item
        t_count += 1
    t_avg = t_sum / t_count
    return (hw_avg * 0.1) + (q_avg * 0.3) + (t_avg * 0.6)
    
def get_letter_grade(score):
    if round(score) >= 90:
        return "A"
    elif round(score) >= 80:
        return "B"
    elif round(score) >= 70:
        return "C"
    elif round(score) >= 60:
        return "D"
    else:
        return "F"
        
print get_letter_grade(get_average(lloyd))

def get_class_average(student_list):
    sum1 = 0
    count1 = 0
    for item in student_list:
        sum1 += get_average(item)
        count1 += 1
    return sum1/count1
    
print get_class_average(students)
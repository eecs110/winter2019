import helpers

'''
Problem 8
Write a function called get_students_by_major that takes 
a file object as an argument and returns a 
list of student names that where they key is the major 
and the value is a list of students belonging to the major.
'''

def get_students_by_major(file, student_major):
    student_names = []
    for line in file.readlines()[1:]:
        line = line.replace('\n', '')
        cells = line.split(',')
        major = cells[2]
        if student_major == major:
            full_name = cells[0] + ' ' + cells[1]
            student_names.append(full_name)
    return student_names



f = open(helpers.get_file_path('students.csv'), 'r')
student_names = get_students_by_major(f, 'Psychology')
print(student_names)
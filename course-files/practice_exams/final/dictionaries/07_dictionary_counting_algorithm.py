import helpers

'''
Problem 7
Write a function called get_majors_counts that takes a 
file object as an argument and returns a dictionary 
where they key is the major and the value is the number 
of people belonging to each major.
'''

def get_majors_counts(file):
    counts_dictionary = {}
    for line in file.readlines()[1:]:
        line = line.replace('\n', '')
        cells = line.split(',')
        major = cells[2]
        if counts_dictionary.get(major):
            counts_dictionary[major] += 1
        else:
            counts_dictionary[major] = 1
    return counts_dictionary

        

f = open(helpers.get_file_path('students.csv'), 'r')
results = get_majors_counts(f)
print(results)
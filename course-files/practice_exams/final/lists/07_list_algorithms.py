import helpers

def get_majors_list(file):
    majors = []
    for line in file.readlines()[1:]:
        line = line.replace('\n', '') 
        cells = line.split(',')
        if cells[2] not in majors:
            majors.append(cells[2])

    return majors
    
f = open(helpers.get_file_path('students.csv'), 'r')
results = get_majors_list(f)
print(results)
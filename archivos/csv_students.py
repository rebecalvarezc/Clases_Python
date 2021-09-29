data = open('csv_data.txt', 'r')
database = [i.strip() for i in data.readlines()[1:]]
data.close()

for line in database:
    student_data = line.split(',') # [name, age, uni, career]
    name = student_data[0].capitalize()
    age = student_data[1]
    university = student_data[2]
    career = student_data[3].capitalize()

    print(f'{name} is {age} years old and is studying {career} in {university}')

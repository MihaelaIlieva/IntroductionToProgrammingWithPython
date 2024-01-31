def organize(cars, students):
    students_left = []
    for student in students:
        students_left.append(student)

    for car in cars:
        current_number_of_passengers = 4
        for student in students:
            if current_number_of_passengers > 0 and student.car == None:
                car.add_student(student)
                if student.is_comfy():
                    current_number_of_passengers -= 1
                    students_left.remove(student)
                else:
                    car.remove_student(student)

    if len(students_left) == 0:
        return True
    else:
        return False
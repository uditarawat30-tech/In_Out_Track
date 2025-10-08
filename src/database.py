students = {}

def add_student(student_id, name, room_no):
    students[student_id] = {'name': name, 'room': room_no}
    return "Student added"

def get_student(student_id):
    return students.get(student_id, "Student not found")

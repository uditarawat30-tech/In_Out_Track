from attendance import attendance_log
from leave import leave_requests

def view_attendance(student_id=None):
    if student_id:
        return attendance_log.get(student_id, [])
    return attendance_log

def view_leaves():
    return leave_requests

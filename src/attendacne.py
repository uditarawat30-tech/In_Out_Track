from datetime import datetime

attendance_log = {}

def mark_attendance(student_id, action):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if student_id not in attendance_log:
        attendance_log[student_id] = []
    attendance_log[student_id].append({'action': action, 'time': timestamp})
    return f"{action} marked at {timestamp}"

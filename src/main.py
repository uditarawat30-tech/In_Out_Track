# main.py
from auth import signup, login
from attendance import mark_attendance
from leave import apply_leave, review_leave
from database import add_student, get_student
from dashboard import view_attendance, view_leaves

# Sample flow
print(signup("anant123", "pass123", "student"))
print(login("anant123", "pass123"))
print(add_student("S101", "Anant", "Room 12"))
print(mark_attendance("S101", "Check-In"))
print(apply_leave("S101", "2025-10-10", "2025-10-12", "Family visit"))
print(view_attendance("S101"))
print(view_leaves())

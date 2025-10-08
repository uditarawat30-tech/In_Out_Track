def apply_leave(student_id, from_date, to_date, reason):
    leave_requests[student_id] = {
        'from': from_date,
        'to': to_date,
        'reason': reason,
        'status': 'Pending'
    }
    return "Leave request submitted"

def review_leave(student_id, decision):
    if student_id in leave_requests:
        leave_requests[student_id]['status'] = decision
        return f"Leave {decision}"
    return "No leave request found"

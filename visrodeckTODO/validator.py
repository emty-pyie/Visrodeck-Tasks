def validate_task_input(title, due_date):
    if not title or len(title.strip()) == 0:
        return False, "Title is required"
    if not due_date or len(due_date.strip()) == 0:
        return False, "Due date is required"
    return True, ""

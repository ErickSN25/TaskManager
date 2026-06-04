def format_task(task):
    status = "✓" if task["done"] else "○"
    return f"{status} [{task['priority'].upper()}] #{task['id']} - {task['title']}"
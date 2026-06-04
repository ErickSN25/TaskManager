def format_task(task):
    status = "✓" if task["done"] else "○"
    return f"{status} PRIORITY:{task['priority']} | ID:{task['id']} | {task['title']}"
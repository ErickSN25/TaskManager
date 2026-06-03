# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

def format_task(task):
    status = "[ ]"
    return f"{status} [{task['priority']}] #{task['id']} - {task['title']}"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]

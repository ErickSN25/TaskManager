from utils import format_task, filter_tasks

tasks = []

def add_task(title, priority="normal"):
    task = {"id": len(tasks) + 1, "title": title, "priority": priority, "done": False}
    tasks.append(task)
    return task

def complete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            return task
    return None

def list_tasks(show_done=True):
    visible = filter_tasks(tasks, show_done)
    for task in visible:
        print(format_task(task))

if __name__ == "__main__":
    add_task("Estudar rebase", "high")
    add_task("Fazer merge do PR", "normal")
    add_task("Escrever CHANGELOG", "low")
    complete_task(1)
    list_tasks()

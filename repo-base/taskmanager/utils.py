# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

#HotFix/Fix-Format: 
# conserto rapido para a produção

def format_task(task):
    status = "✓" if task["done"] else "ppppppp"
    return f"{status} [{task['priority'].upper()}] #{task['id']} - {task['title']}"

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]

#Ajustes para melhor finalidade
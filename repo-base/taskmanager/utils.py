# Zona de conflito intencional: ambos os devs modificarão format_task e filter_tasks

#HotFix/Fix-Format: 
# conserto rapido para a produção

def format_task(task):
#Segundo hotfix, conserto de format

def format_task(task):
<<<<<<< HEAD
    status = "[ ]"
    return f"{status} [{task['priority']}] #{task['id']} - {task['title']}"
=======
    status = "✓" if task["done"] else "o"
    status = "✓" if task["done"] else "○"
    return f"{status} [{task['priority'].upper()}] #{task['id']} - {task['title']}"
>>>>>>> 2ff3d12f3b1b3387323d1749cdd7f956a643cc23

def filter_tasks(tasks, show_done=True):
    if show_done:
        return tasks
    return [t for t in tasks if not t["done"]]
<<<<<<< HEAD
=======
    return [t for t in tasks if not t["done"]]

#Ajustes para melhor finalidade
    return [t for t in tasks if not t["done"]]
>>>>>>> 2ff3d12f3b1b3387323d1749cdd7f956a643cc23

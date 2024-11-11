def add_task(task, task_list):
    if task:
        task_list.append(task)
        return True
    return False

def delete_task(index, task_list):
    try:
        del task_list[index]
        return True
    except IndexError:
        return False

def complete_task(index, task_list):
    try:
        task_list[index] = f"{task_list[index]} (Completada)"
        return True
    except IndexError:
        return False

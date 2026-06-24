def delete_task(tasks, task_id):
    return [task for task in tasks if task["id"] != task_id]
  

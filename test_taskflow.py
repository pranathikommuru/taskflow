from create_task import create_task

task = create_task("Learn Git")

assert task["title"] == "Learn Git"

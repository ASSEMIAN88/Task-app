
from entities.task import Task

task = Task.create(title="test oto", description= "description")
task.start()
print(task)

task.update(description="nouvelle description")
task.finish()
print(task)
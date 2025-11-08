
from entities.task import Task
from entities.user import User
from services.task_service import TaskService

task = Task.create(title="test oto", description= "description")
task.start()
task1 = Task.create(title="ethique", description= "ceci est une description")
task1.start()
TaskService.add_task(task)
TaskService.add_task(task1)
TaskService.get_all_task()


task.update(description="nouvelle description")
task.finish()
#print(task)

user = User.create(firstname=" test", lastname="lastname", email="email", password="password")
# print(user)

user.update(firstname="new firstname", lastname="new lastname")
# print(user)
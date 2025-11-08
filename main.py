
from entities.task import Task
from entities.user import User

task = Task.create(title="test oto", description= "description")
task.start()
print(task)

task.update(description="nouvelle description")
task.finish()
print(task)

user = User.create(firstname=" test", lastname="lastname", email="email", password="password")
# print(user)

user.update(firstname="new firstname", lastname="new lastname")
# print(user)

class TaskRepository:
    def __init__(self):
        self.__tasks = []

    def add_task(self, task):
        self.__tasks.append(task)

    def get_all_tasks(self):
        for task in self.__tasks:
            task.display()
            print()
            print("*****************************")
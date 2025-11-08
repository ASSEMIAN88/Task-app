from repositories.task_repository import TaskRepository


class TaskService:
    
    task_repository= TaskRepository()
       
    @classmethod
    def add_task(cls,task):
        cls.task_repository.add_task(task)
        
    @classmethod
    def get_all_task(cls):
        print("liste des taches *****************************")
        print()
        cls.task_repository.get_all_tasks()
        
        
        

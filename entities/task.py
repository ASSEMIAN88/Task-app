from datetime import datetime

from entities.task_status import TaskStatus

class Task:
    
    def __init__(self, title:str, description:str, status:TaskStatus, create_at:datetime,update:datetime):
        self.__title = title
        self.__description = description
        self.__status = status
        self.__create_at = create_at
        self.__update = update 


    @classmethod   
    def create (cls,title:str , description:str):
        return Task(
            title=title,
            description=description,
            status= TaskStatus.PENDING,
            create_at=datetime.now(),
            update= None)
    
    def update(self, title:str = None ,description:str = None):
        if title is not None:
            self.__title = title
        if description is not None:
            self.__description = description

    def start(self):
        self.__status = TaskStatus.STARTING
        
    def finish(self):
        self.__status = TaskStatus.FINISHING
    
    def __repr__(self):
        return f"(title: {self.__title}, description: {self.__description}, status: {self.__status.value}, create_at: {self.__create_at}, update: {self.__update})"
    

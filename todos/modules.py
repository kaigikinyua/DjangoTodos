 
from todos.models import Todo
from datetime import datetime
class TodosCrud:
    @staticmethod
    def create_todo(useremail,todo,deadline,priority):
        response=False
        try:
            t=Todo(todo=todo,deadline=deadline,priority=priority,owner=useremail)
            t.save()
            response=True
        except:
            print("Error while creating todo")
        return response

    @staticmethod
    def delete_todo(useremail,todo):
        response=False
        try:
            t=Todo.objects.get(owner=useremail,todo=todo)
            t.delete()
            response=True
        except:
            print("Error while deleting todo")
            response=False

    @staticmethod
    def edit_todo(useremail,todo,new_todo,new_priority,new_deadline):
        response=False
        try:
            t=Todo.objects.get(owner=useremail,todo=todo)
            t.todo=new_todo
            t.priority=new_priority
            t.deadline=new_deadline
            t.save()
            response=True
        except:
            response=False
        return response

    @staticmethod
    def fetch_todos(useremail):
        todos=None
        try:
            todos=Todo.objects.filter(owner=useremail)
        except:
            print("Error while fetching todos")
            todos=False
        return todos


if __name__=="__main__":
    print("Testing module: TodosCrud")
    tests={"Create":False,"Delete":False,"Update":False,"Read":False}
    tests["Create"]=TodosCrud.create_todo("james@email.com","Build a car",datetime.today(),1,)
    tests["Read"]=TodosCrud.fetch_todos("james@email.com")
    tests["Update"]=TodosCrud.edit_todo("james@email.com","Build a sports car",datetime.today(),3)
    tests["Delete"]=TodosCrud.delete_todo("james@email.com","Build a sports car")
    for test in tests:
        print(test)


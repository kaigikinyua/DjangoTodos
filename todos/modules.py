from todos.models import Todo

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



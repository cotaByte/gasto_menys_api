from fastapi import Body,FastAPI,Path
from typing import Annotated
import sys
sys.path.append('./entities')
import user,expense,group

app = FastAPI()

# #region Auth
@app.post("/login")
def login(request: Annotated[object,Body()]):
    return user.login(request.get("user"),request.get("password"))    

@app.post("/createUser")
def createUser(request: Annotated[object, Body()]):
    return user.create(
        request.get("username"),
        request.get("password"),
        request.get("name"),
        request.get("surname"),
        request.get("age"),
        )
#End Auth region

# #region Expenses
@app.get("/expenses/{user_id}/{year}/{month}")
def get_expenses(user_id:str,year:int,month:int):
    return expense.get_expenses(user_id,year,month)
    
@app.post("/setExpense")
def addExpense(request: Annotated[object,Body()]):
    return expense.set_expense(
        request.get("user_id"),
        request.get("year"),
        request.get("month"),
        request.get("description"),
        request.get("type"),
        request.get("ammount"),
        request.get("expense_id"),
        request.get("group_id"),
        request.get("notes")
    )
    
@app.get("/expense/{expense_id}")
def get_expense_detail(expense_id):
    return expense.get_expense_detail(expense_id)

@app.delete("/deleteExpense/{expense_id}")
def delete_expense(expense_id):
    return expense.delete_expense(expense_id)
#End Expenses region

# #region Groups
@app.get("/groups/{user_id}")
def get_groups(user_id:str):
    return group.get_groups(user_id)

@app.delete("/deleteGroup/{group_id}")
def delete_group(group_id):
    return group.delete_group(group_id)

@app.post("/setGroup")
def set_group(request: Annotated[object, Body()]):
    return group.set_group(request.get("user_id"),request.get("name"),request.get("id"))
#End Expenses region
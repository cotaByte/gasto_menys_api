from fastapi import Body,FastAPI,Path
from typing import Annotated
import sys
sys.path.append('./entities')
import user,expense

app = FastAPI()

# #region Auth
@app.post("/login")
def login(request: Annotated[object,Body()]):
    return user.login(request.get("user"),request.get("password"))    
#End Auth region

# #region Expenses
@app.get("/expenses/{user_id}/{year}/{month}")
def get_expenses(user_id:str,year:int,month:int):
    return expense.get_expenses(user_id,year,month)
    
@app.post("/addExpense")
def addExpense(request: Annotated[object,Body()]):
    print(request)
    return expense.set_expense(
        request.get("user_id"),
        request.get("year"),
        request.get("month"),
        request.get("description"),
        request.get("type"),
        request.get("ammount"),
    )
    
@app.get("/expense/{expense_id}")
def get_expense_detail(expense_id):
    return expense.get_expense_detail(expense_id)

@app.delete("/deleteExpense/{expense_id}")
def delete_expense(expense_id):
    return expense.delete_expense(expense_id)
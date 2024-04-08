from fastapi import Body,FastAPI
from typing import Annotated

app = FastAPI()

@app.get("/")
async def root():
    return "root api"

#Auth region
@app.post("/login")
async def login(request: Annotated[object,Body()]):
    print(request)
    #TODO => IMPLEMENT LOGIN
    
#End Auth region

#Expenses region
@app.get("/expenses/{user_id}/{month}")
async def getExpenses(user_id:int,month:int):
    if(user_id==1 and month==1): return {"Object":"Object"}
    #TODO=> IMPLEMENT EXPENSES


    
#End Expenses region

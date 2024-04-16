import sys

sys.path.append('../utilites')
import connection

def get_expenses(user_id:str,year:int,month:int):
    if not user_id or not month: return {"ok":False, "msg": "Request params not valid"}
    
    with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
            sql="select * from expenses where user_id=%s and year=%s and month=%s"
            con.execute(sql, [user_id,year,month])
            return con.fetchall()

        
    
def get_expense_detail(expense_id:str):
    with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
            sql="select * from expenses where id=%s"
            con.execute(sql, [expense_id])
            return con.fetchone()
    
        
#TODO => IF has id update, sino nuevo pasar parametros por key
def set_expense(user_id:str,year:int,month:int,description:str, type:str, ammount:float, id:str="", group_id:str="" , notes:str="" ):
    sql =f'''insert into expenses 
    (user_id,year, month,description,type, ammount,group_id,notes)
    values
    (
        '{user_id}',
        {year},
        {month},
        '{description}',
        '{type}',
        {ammount},
        nullif('{group_id}',''), 
        nullif($${notes}$$,'')
    )'''
    msg="Expense added"    
    if (id): # the expense exists
        msg="Expense updated"
        sql=f'''
            update expenses set 
            description='{description}',
            type='{type}',
            ammount={ammount},
            group_id=coalesce('{group_id}'::uuid,null)::uuid,
            notes=coalesce('{notes}',null)
            '''

    with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
            con.execute(sql)
            ret=con.rowcount
            ret and odb.commit()
            
            msg= msg if ret else "Error trying to delete exepense"
            return {"ok":ret,"msg":msg}
    


def delete_expense(expense_id):
       with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
            msg = "Expense deleted"
            
            sql = "delete from expenses WHERE id = %s"
            con.execute(sql, (expense_id,))
            ret =bool(con.rowcount)
            ret and odb.commit()
            
            msg= msg if ret else "Error trying to delete expense"
            return {"ok": ret, "msg": msg}
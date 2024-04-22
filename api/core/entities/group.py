import sys
import json

sys.path.append('../utilites')
import connection



def get_groups(user_id:str):   
    with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
    
            sql ='''select id,
                name,
                case
                    when user_id=%s then true
                    else false
                end as deletable
            from expenses_groups
            where user_id is null
            or user_id=%s
            '''
            con.execute(sql, [user_id,user_id])
            return con.fetchall()
        
        
        
def delete_group(group_id):
    with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
            con.execute("select * from expenses where group_id=%s",[group_id])
            if(con.rowcount>0): return {"ok":False,"msg":"The group has expenses assigned and can't be deleted"}
            
            msg="Group deleted correctly"
            con.execute("delete from expenses_groups where id=%s",[group_id])
            ret=con.rowcount
            
            ret and odb.commit()
            
            msg= msg if ret else "Error trying to delete group"
            return {"ok":bool(ret),"msg":msg, "rowcount":ret}
        
        
        
def set_group(user_id, name,id=""):
    msg="Group added correctly"
    sql = f"insert into expenses_groups (name,user_id) values (INITCAP('{name}'),'{user_id}')"
    if(id):
        sql = f"update expenses_groups set name=INITCAP('{name}') where id='{id}'"
        msg="Group updated correctly"
       
    with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
            con.execute(sql)
            ret=con.rowcount
            ret and odb.commit()
            
            msg= msg if ret else "Error trying to preform the operation"
            return {"ok":bool(ret),"msg":msg, "rowcount":ret}
import sys
sys.path.append('../utilities')
import connection

def login(usr,pwd):
    
    
    with connection.get_db_connection("GASTOMENYS") as con:
    
        sql = "select * from users where username=%s and password=%s"
        con.execute(sql, [usr,pwd])
        if con.rowcount==0: return {"ok":False,"msg":"username or password are incorrect"}
        ouser= con.fetchone()
        
    return {"ok":True,"ouser":ouser}
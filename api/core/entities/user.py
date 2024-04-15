import sys
sys.path.append('../utilities')
import connection

def login(usr,pwd):
    
    odb=connection.connect("GASTOMENYS")
    
    with odb.cursor() as con:
    
        sql = "select * from users where username=%s and password=%s"
        #sql = f"select * from users where username='{usr}' and password='{pwd}'"
        #print(sql)
        con.execute(sql, [usr,pwd])
        if con.rowcount==0: return {"ok":False,"msg":"username or password are incorrect"}
        ouser= con.fetchone()
        
    return {"ok":True,"ouser":ouser}
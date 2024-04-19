import sys
sys.path.append('../utilities')
import connection

def login(usr:str,pwd:str)->object:

    with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
    
            sql = "select * from users where username=%s and password=%s"
            con.execute(sql, [usr,pwd])
            if con.rowcount==0: return {"ok":False,"msg":"username or password are incorrect"}
            ouser= con.fetchone()
            
        return {"ok":True,"ouser":ouser}
    
def create(username:str,password:str,name:str,surname:str,age:int)->object:
    with connection.connect("GASTOMENYS") as odb:
        with connection.get_cursor(odb) as con:
            
            sql='''select * from users where username=%s'''
            con.execute(sql,[username])
            res=con.fetchone()
            if(res): return {"ok":False,"msg":"This user already exists"}
            
            msg= "User created correctly"
            sql='''
            insert into users (username,password,name,surname,age)
            values
            (%s,%s,%s,%s,%s) returning id
            '''
            con.execute(sql,[username,password,name,surname,age])
            ok= bool( con.fetchone())
                        
            msg= msg if ok else "Error creating the user"
            return {"ok":ok,"msg":msg}
        
        #rafa 5dd1a5a8-d8a4-4684-b09f-57ef0a878bb9
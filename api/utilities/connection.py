import psycopg2
from psycopg2.extras import RealDictCursor

# List of connections
databases={
    "GASTOMENYS":{
        "host":"localhost",
        "port":5432,
        "username":"rafa",
        "password":"X18kdXBQM3JwNCRzX18=",
        "database":"GastoMenys"
    }
}


def connect(bd:str):
    o_bd= databases[bd]
    if not o_bd: return {"ok":False,"msg":f"Unable to find database {bd}"}
    
    try:
        con = psycopg2.connect(
            host=o_bd["host"],
            user=o_bd["username"],
            password=o_bd["password"],
            database=o_bd["database"]
        )
        return con
    except Exception as ex:
        print(ex)
        return False

def get_cursor(odb):
      return odb.cursor(cursor_factory=RealDictCursor)

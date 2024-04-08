import psycopg2


databases={

    "gastomenys":{
        "host":"localhost",
        "port":5432,
        "username":"rafa",
        "password":"cG9zdGdyZXM="
        
    }
}


print(databases["gastomenys"].host)
print(databases["gastomenys"].port)
print(databases["gastomenys"].username)



def connect():
    try:
        con = psycopg2.connect(
            host='localhost',
            user='rafa',
            password='X18kdXBQM3JwNCRzX18=',
            database='GastoMenys'
        )
        print(con)
        return con
    except Exception as ex:
        print(ex)
        
        

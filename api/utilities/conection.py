import psycopg2


databases={

    "gastomenys":{
        "host":"localhost",
        "port":5432,
        "username":"rafa",
        "password":"cG9zdGdyZXM="
        
    }
}


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
        
        

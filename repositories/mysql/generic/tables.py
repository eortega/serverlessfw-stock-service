import os
import json
import mysql.connector
from mysql.connector import errorcode

def handle(event, context):
    host = os.environ['AURORA_HOST']
    port = os.environ['AURORA_PORT']
    db = os.environ['AURORA_DB_NAME']
    user = os.environ['AURORA_USERNAME']
    p = os.environ['AURORA_PASSWORD']
    db_error ="None"
    
    try:
        cnx = mysql.connector.connect(host=host,user=user,passwd=p,db=db, port=port)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            db_error = "Something is wrong with your user name or password"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            db_error= "Database does not exist"
        else:
            db_error = "Another error"
    else:
        cursor = cnx.cursor()
        query = ("SELECT table_name FROM information_schema.tables")

        cursor.execute(query, (hire_start, hire_end))
        tables = []
        for (table_name) in cursor:
            tables.append(table_name)


        cursor.close()
        cnx.close()
        response = {
            "statusCode": 200,
            "body": json.dumps(tables})
        }

        return response

    
        
    response = {
        "statusCode": 400,
        "body": json.dumps({'Message': "Soemthing goes wrong", "db_error": db_error}})
    }

    return response
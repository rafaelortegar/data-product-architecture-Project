import psycopg2
import sys
import pandas as pd 

creds = pd.read_csv("credentials_postgres.csv")

try:
    connection = psycopg2.connect(user = creds.user[0],
                                  password = creds.password[0],
                                  host = creds.host[0],
                                  port = creds.port[0],
                                  database = creds.db[0])
                                  
    cursor = connection.cursor()
    cursor.execute('SELECT version()')

    version = cursor.fetchone()[0]
    print(version)

except psycopg2.DatabaseError as e:

    print(f'Error {e}')
    sys.exit(1)

finally:
    if connection:
        connection.close()

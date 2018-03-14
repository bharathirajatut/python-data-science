import pandas as pd
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                               user='username',
                               password='pass',
                               db='demo',
                               charset='utf8mb4',
                               cursorclass=pymysql.cursors.DictCursor)


countries=pd.read_sql("SELECT * FROM countries",con=connection)


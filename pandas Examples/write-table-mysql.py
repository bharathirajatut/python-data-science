import pandas as pd
import pymysql
from sqlalchemy import create_engine


cnx = create_engine('mysql+pymysql://username:password@localhost:3306/databaseName', echo=False)

data = pd.read_sql('SELECT * FROM countries', cnx)

data.to_sql(name='sample_table2', con=cnx, if_exists = 'append', index=False)
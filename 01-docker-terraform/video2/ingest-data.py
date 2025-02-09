import os
from time import time
import argparse
from sqlalchemy import create_engine
import pandas as pd

def main(params):
    user = params.user
    password = params.password
    host = params.host
    port = params.port
    db = params.db
    table_name = params.table_name
    
    file_name = 'taxi.parquet'
    taxi = pd.read_parquet(file_name)
    
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db}')
    
    taxi.to_sql(name='yellow_taxi_data', con=engine, if_exists='replace')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Ingest CSV data to Postgres')
    parser.add_argument('--user', help='user name for postgres')
    parser.add_argument('--password', help='password for postgres')
    parser.add_argument('--host', help='password for postgres')
    parser.add_argument('--port', help='password for postgres')
    parser.add_argument('--db', help='password for postgres')
    parser.add_argument('--table_name', help='password for postgres')

    args = parser.parse_args()
    params = args
    
    main(params)



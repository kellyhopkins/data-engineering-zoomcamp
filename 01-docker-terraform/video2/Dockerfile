FROM python:3.9

RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2 pyarrow

WORKDIR /app
COPY ingest-data.py ingest-data.py
COPY taxi.parquet taxi.parquet

ENTRYPOINT [ "python", "ingest-data.py" ]
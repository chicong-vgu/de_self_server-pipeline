FROM apache/airflow:slim-3.0.1-python3.9
USER root
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN chown -R 50000:50000 /opt/airflow
USER airflow
RUN pip install psycopg2-binary pandas pyyaml asyncpg apache-airflow-providers-fab==1.3.0
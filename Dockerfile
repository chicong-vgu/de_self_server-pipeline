FROM apache/airflow:2.9.2
RUN pip install great_expectations
RUN pip install pydantic==2.8.2

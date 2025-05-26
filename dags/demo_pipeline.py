from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import yaml
import pandas as pd
import sqlalchemy
import great_expectations as gx
# from great_expectations.data_context import FileDataContext
# from great_expectations.dataset import PandasDataset
# from great_expectations.core.batch import BatchRequest
import os

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def validate_data(**kwargs):
    config = load_config(kwargs['config_path'])
    data_path = config['pipeline']['source']['path']
    context = gx.get_context(mode="file", project_root_dir='/opt/airflow/great_expectations')

    preset_expectation = gx.expectations.ExpectColumnMaxToBeBetween(column="age", min_value=28, max_value=40)

    #Data source

    sample_batch = context.data_sources.pandas_default.read_csv(data_path)

    validation_results = sample_batch.validate(preset_expectation)
    
    if not validation_results['success']:
        raise ValueError("Data validation failed: " + str(validation_results['result']))

def process_data(**kwargs):
    config = load_config(kwargs['config_path'])
    # Read source data
    df = pd.read_csv(config['pipeline']['source']['path'])
    
    # Apply transformations
    for t in config['pipeline']['transformations']:
        if t['type'] == 'filter':
            df = df.query(t['column'] + t['condition'])
        elif t['type'] == 'aggregate':
            df = df.groupby(t['group_by'])[t['metric']].agg(t['function']).reset_index()
    
    # Write to destination
    engine = sqlalchemy.create_engine(config['pipeline']['destination']['connection'])
    df.to_sql(config['pipeline']['destination']['table'], engine, if_exists='replace', index=False)

with DAG(
    'demo_pipeline',
    start_date=datetime(2025, 5, 20),
    schedule=None,
    catchup=False
) as dag:
    validate_task = PythonOperator(
        task_id='validate_data',
        python_callable=validate_data,
        op_kwargs={'config_path': '/opt/airflow/data/demo_pipeline_config.yaml'}
    )
    
    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        op_kwargs={'config_path': '/opt/airflow/data/demo_pipeline_config.yaml'}
    )
    validate_task >> process_task
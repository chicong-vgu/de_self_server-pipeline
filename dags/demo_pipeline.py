from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import yaml
import pandas as pd
import sqlalchemy

def load_config(config_path):
    with open(config_path, 'r') as file:
        return yaml.safe_load(file)

def process_data(**kwargs):
    config = load_config(kwargs['config_path'])
    # Read source data
    df = pd.read_csv(config['pipeline']['source']['path'])
    
    # Apply transformations
    for t in config['pipeline']['transformations']:
        if t['type'] == 'filter':
            print('condition is ', t['condition'])
            # df = df.query(t['condition'])
            df = df.query(f"{t['column']} {t['condition']}")
        elif t['type'] == 'aggregate':
            df = df.groupby(t['group_by'])[t['metric']].agg(t['function']).reset_index()
    
    # Write to destination
    engine = sqlalchemy.create_engine(config['pipeline']['destination']['connection'])
    df.to_sql(config['pipeline']['destination']['table'], engine, if_exists='replace', index=False)

with DAG(
    'demo_pipeline',
    start_date=datetime(2025, 5, 20),
    schedule_interval=None,
    catchup=False
) as dag:
    process_task = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
        op_kwargs={'config_path': '/opt/airflow/data/demo_pipeline_config.yaml'}
    )
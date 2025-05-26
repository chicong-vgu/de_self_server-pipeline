Alternative: Use a Custom Docker Image
To avoid running apt-get and pip commands in every container startup, create a custom Docker image with pre-installed dependencies. This is more efficient and aligns with Effendi’s emphasis on modularity.

How to run
```shell
docker compose up -d
```
--to stop
```shell
docker compose down
```
 -- metadata on posstgres has been mounted so no impact user account wwhen down     volumes:- postgres_data:/var/lib/postgresql/data

### Access Airflow Web UI
Go to http://localhost:8080. Log in using the credentials you set up during the Airflow user creation process in login to airflow 2.x

### Access Airflow CLI
To access the Airflow CLI, run the following command in your terminal:
```shell
docker exec -it <container_id> airflow
```

### Access Postgres Database
To access the Postgres database, you can use a database management tool like pgAdmin or connect to it using the command line:
```shell
docker exec -it <postgres_container_id> psql -U postgres
```

### login to airflow 2.x
```shell
docker exec -it <container_id> bash, run command duoi:
```
```shell
airflow users create \
    --username airflow \
    --password airflow \
    --firstname Airflow \
    --lastname Admin \
    --role Admin \
    --email airflow@example.com
```

### login to airflow 3.0

user: admin (default)
password: (vao trong container check *)
```shell
docker exec -it <container_name_of_airflow_webserver> bash
```
-- show config if needed: 
```shell
airflow config list
```
password o day:
```shell
   cat $AIRFLOW_HOME/simple_auth_manager_passwords.json.generated
   ```




### Add Data Quality (Optional)
To align with Effendi’s emphasis on data quality (), integrate Great Expectations:

1. Install Great Expectations in Airflow:
dockerfile

```yml
FROM apache/airflow:2.9.2
RUN pip install great_expectations</code>
```

2. Update Docker Compose:
```shell
docker build -t custom-airflow:2.9.2 .
```
3. update docker-compose with new image (custom-airflow:2.9.2)

4. docker compose up -d

5. Create a Directory for Great Expectations:

```bash
mkdir -p great_expectations/expectations
mkdir -p great_expectations/checkpoints
```
6. Mount Great Expectations Directory:
```yml
volumes:
  - ./great_expectations:/opt/airflow/great_expectations
```
```


### Monitoring/ check log

```shell
docker compose logs airflow-webserver
```






### Error
why aiflow dags list-import-errors has found no errrors but on the airflow UI still display 
--> must install version pydantic correctly 2.8.2 ( built in docker file aalready to fix)
```sh
 "Broken DAG: [/opt/airflow/dags/demo_pipeline.py] Traceback (most recent call last): File "/home/airflow/.local/lib/python3.12/site-packages/pydantic/v1/typing.py", line 520, in update_field_forward_refs field.type_ = evaluate_forwardref(field.type_, globalns, localns or None) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ File "/home/airflow/.local/lib/python3.12/site-packages/pydantic/v1/typing.py", line 66, in evaluate_forwardref return cast(Any, type_)._evaluate(globalns, localns, set()) ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ TypeError: ForwardRef._evaluate() missing 1 required keyword-only argument: 'recursive_guard'"
 ```



### Check dag in airlow server

```sh
airflow dags list
airflow dags list-import-errors
```

check data in postgres
```sql
select * from output_table; 
```
-- output_table trong /Users/chicong/Study/DE_self-serve_pipeline/data/demo_pipeline_config.yaml
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
7. Initialize Great Expectations ben trong container airflow webserver
```bash
great_expectations --v3-api init
```


### Monitoring/ check log

```shell
docker compose logs airflow-webserver
```
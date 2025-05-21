Alternative: Use a Custom Docker Image
To avoid running apt-get and pip commands in every container startup, create a custom Docker image with pre-installed dependencies. This is more efficient and aligns with Effendi’s emphasis on modularity.



### login to airflow 2.x
docker exec -it <container_id> bash, run command duoi:

airflow users create \
    --username airflow \
    --password airflow \
    --firstname Airflow \
    --lastname Admin \
    --role Admin \
    --email airflow@example.com

### login to airflow 3.0

user: admin (default)
password: (vao trong container check *)
*:  docker exec -it <container_name_of_airflow_webserver> bash
   -- show config if needed: airflow config list
   password o day:
    cat $AIRFLOW_HOME/simple_auth_manager_passwords.json.generated




5. Add Data Quality (Optional)
To align with Effendi’s emphasis on data quality (), integrate Great Expectations:

Install Great Expectations in Airflow: Modify the Docker image to include Great Expectations by creating a custom Dockerfile:
dockerfile

<code>FROM apache/airflow:2.9.2
RUN pip install great_expectations</lewjokD    SPIAKP9U1 ` code>

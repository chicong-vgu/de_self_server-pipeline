#!/bin/bash
airflow webserver
airflow db init
exec "$@"
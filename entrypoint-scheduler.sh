#!/bin/bash
airflow scheduler
airflow db init
exec "$@"
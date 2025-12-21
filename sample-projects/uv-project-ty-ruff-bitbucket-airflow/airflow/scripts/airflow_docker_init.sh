#!/usr/bin/env bash

# Creating missing opt dirs if missing
mkdir -v -p /opt/airflow/{logs,dags,plugins,config}

# Change ownership to allow writing to it, others are RO
chown -v -R "${AIRFLOW_UID}:0" /opt/airflow/{logs,config}

/entrypoint airflow version
/entrypoint airflow config list >/dev/null

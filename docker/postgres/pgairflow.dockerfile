FROM postgres:13.1-alpine
LABEL maintainer "Manoel Teles"
ENV POSTGRES_USER=airflow
ENV POSTGRES_PASSWORD=airflow
ENV POSTGRES_DB=airflow
EXPOSE 5432
FROM jupyter/all-spark-notebook:latest
LABEL maintainer="Manoel Teles"

# RUN apt-get update \
#   && apt-get install -y --no-install-recommends \
#          vim \
#          wget\
#   && apt-get autoremove -yqq --purge \
#   && apt-get clean \
#   && rm -rf /var/lib/apt/lists/*
USER root
COPY all_spark_notebook/requirements.txt /requirements.txt
RUN pip install -r /requirements.txt && python -m spylon_kernel install
FROM python:3.11-slim-buster

ARG USER_HOME=/opt/workspace

USER 0

RUN mkdir -p $USER_HOME
COPY ./task-1 $USER_HOME/task1/
COPY ./task-2 $USER_HOME/task2/

RUN pip install polars faker

WORKDIR $USER_HOME
CMD ["while", "true;", "do", "sleep", "30;", "done;" ]

# docker build . -t python:3.11-cst -f Dockerfile --no-cache



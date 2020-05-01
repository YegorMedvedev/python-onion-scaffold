FROM python:3.8.2-alpine as base


# Use multi-stage build in order to minimize the final image size
# This builder was added in order to install psycopg2-binary, otherwise it doesn't build with alpine image
FROM base as setup

RUN mkdir -p /usr/local/app && \
    apk update && \
    apk add postgresql-dev gcc python3-dev musl-dev && \
    pip3 install -U pipenv --no-cache-dir

WORKDIR /usr/local/app

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install --system --deploy && \
    pip3 uninstall -y pipenv virtualenv-clone virtualenv


# Create workind directory and copy only nessesary files there
FROM setup as builder

RUN mkdir -p /config && \
    mkdir -p /src && \
    mkdir -p /alembic

COPY ./src ./src
COPY ./alembic ./alembic
COPY ./alembic.ini ./

ENV PYTHONPATH "/usr/local/app:/usr/local/app/src"
ENV PYTHONUNBUFFERED "1"


# Final steps... expose port and execute the script
FROM builder

EXPOSE $PORT
CMD ["python3", "/usr/local/app/src/app.py"]
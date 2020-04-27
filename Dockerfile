FROM python:3.8.2-alpine as base


# Use multi-stage build in order to minimize the final image size
# This builder was added in order to install psycopg2-binary, otherwise it doesn't build with alpine image
FROM base as builder

RUN mkdir -p /usr/install
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install pipenv

WORKDIR /usr/install

COPY ./Pipfile .
COPY ./Pipfile.lock .

RUN pipenv install --system --deploy


# Create workind directory and copy only nessesary files there
FROM base

COPY --from=builder /usr/install /usr/local/app
WORKDIR /usr/local/app

RUN mkdir /config

COPY ./src .
COPY ./alembic .
COPY ./alembic.ini .


# Final steps... expose port and execute the script
EXPOSE $PORT
CMD ["python", "./src/app.py"]
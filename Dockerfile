# FROM ubuntu:18.04
# FROM python:3.7.2-alpine3.8
FROM alpine:3.8
LABEL maintainer CK 

RUN apk add --updat \
    python3-dev \
    build-base \
    linux-headers \
    # pcre-dev \
    && pip3 install --upgrade pip \
    && rm -r /root/.cache

ENV PROJECT_NAME proj

# Using pipenv:
COPY ./$PROJECT_NAME/Pipfile ./$PROJECT_NAME/Pipfile.lock /home/$PROJECT_NAME/
RUN pip3 install pipenv
WORKDIR /home/$PROJECT_NAME/
RUN pipenv install --deploy --system --ignore-pipfile

EXPOSE 8888
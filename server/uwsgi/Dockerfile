## Base Python image for building uWSGI
FROM python:3.7.2-slim-stretch AS builder

# Install some basic tools
RUN apt-get update && apt-get -y install \
    build-essential \
    gettext

# Building uWSGI
COPY dynamic/python/requirements.txt .
RUN pip install $(grep uWSGI requirements.txt)

## Base Python image for final image
FROM python:3.7.2-slim-stretch

# Install some packages
#RUN apt-get update && apt-get -y install \
#    gettext-base

# Get python packages from previous build stage
ARG PYTHON_VERS=python3.7
WORKDIR /usr/local/lib/${PYTHON_VERS}/site-packages/
COPY --from=builder /usr/local/lib/${PYTHON_VERS}/site-packages/ .

# Get compiled uWSGI executable from previous build stage
COPY --from=builder /usr/local/bin/uwsgi /usr/local/bin/uwsgi

# Get envsubst
COPY --from=builder /usr/bin/envsubst /usr/bin/envsubst

# Get python source
ARG PYTHON_SRC='/usr/local/src'
COPY dynamic ${PYTHON_SRC}

# Get rest of requirements
RUN pip install $(grep -v uWSGI ${PYTHON_SRC}/python/requirements.txt | tr '\n' ' ')

# Get config file
ARG UWSGI_CONFIG='/etc/uwsgi'
COPY config ${UWSGI_CONFIG}

# Setup ENV variables
ENV UWSGI_ADDR="0.0.0.0" \
    UWSGI_PORT="9090" \
    UWSGI_MASTER="true" \
    PYTHON_SRC="${PYTHON_SRC}/python/src/" \
    PYTHON_APP="server.py" \
    PYTHON_CALLABLE="app" \
    PROC_NUM="4" \
    THREAD_NUM="2"

# Change workdir
WORKDIR ${UWSGI_CONFIG}

# Set launch command
CMD /bin/sh -c \
    "envsubst < \
     uwsgi.tmpl > \
     uwsgi.ini && \
     uwsgi uwsgi.ini || \
     printf '\n---> CONFIG ERROR: Check settings printed below\n\n' && \
     cat uwsgi.ini"


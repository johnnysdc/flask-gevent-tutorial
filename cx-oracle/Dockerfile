FROM python:3.8
# FROM python:3.7-slim

ENV LD_LIBRARY_PATH="/usr/lib/oracle/19.5/client64/lib/${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
ENV ORACLE_HOME="/usr/lib/oracle/19.5/client64"
ENV PATH="/usr/lib/oracle/19.5/;"+${PATH}

WORKDIR /

RUN mkdir /libs
RUN mkdir /build

COPY libs /libs

# install all the specific requirements for a state
COPY requirements.sh /requirements.sh
RUN sh requirements.sh

# upgrade python dependency
RUN pip install --upgrade pip setuptools wheel

RUN pip install Flask requests sqlalchemy uwsgi greenify gevent cx-Oracle==8.3.0 Flask-SQLAlchemy flask_marshmallow flask_migrate marshmallow-sqlalchemy

COPY app.py /app.py
COPY patched.py /patched.py

CMD uwsgi --master \
  --single-interpreter \
  --workers $WORKERS \
  --gevent $ASYNC_CORES \
  --protocol http \
  --socket 0.0.0.0:$PORT_APP \
  --module $MODULE:app


FROM python:3.11

RUN useradd --shell /bin/bash --home /home/dev dev

USER dev

WORKDIR /home/dev

COPY dev-reqs.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

LABEL name="gpkgstatus"
LABEL version="2.0"
LABEL description="Dev environment for gpkgstatus"

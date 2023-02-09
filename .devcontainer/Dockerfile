FROM python:latest

RUN useradd -ms /bin/bash dev
USER dev

WORKDIR /home/dev/

COPY dev-reqs.txt /home/dev/
RUN pip3 install --no-cache-dir -r dev-reqs.txt

LABEL name="gpkgstatus"
LABEL version="1.0"
LABEL description="Dev environment for gpkgstatus"

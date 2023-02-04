FROM python:latest

RUN useradd -ms /bin/bash dev
USER dev

WORKDIR /home/dev/

COPY requirements.txt /home/dev/
RUN pip3 install --no-cache-dir -r requirements.txt

LABEL name="gpkgstatus-dev"
LABEL version="0.4-beta"
LABEL description="Dev environment for gpkgstatus"

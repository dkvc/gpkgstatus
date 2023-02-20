FROM python:3.10-alpine

RUN addgroup --system dev && \
    adduser --system --shell /usr/sbin/nologin --ingroup dev dev

USER dev

WORKDIR /usr/app

COPY dev-reqs.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

LABEL name="gpkgstatus"
LABEL version="1.0"
LABEL description="Dev environment for gpkgstatus"

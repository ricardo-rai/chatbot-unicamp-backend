FROM python:3.10-slim

COPY pyproject.toml /tmp/

RUN pip install poetry==1.1.12 keyring artifacts-keyring

RUN cd /tmp && \
     poetry export -f requirements.txt --dev --output requirements.txt && \
     pip install -r requirements.txt && \
     pip uninstall -y poetry

WORKDIR /app

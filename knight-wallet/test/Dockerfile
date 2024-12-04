FROM python:3.9-slim

WORKDIR /test

COPY app/ /app/
COPY test/requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
CMD ["python", "-m", "unittest", "discover", "-s", ".", "-p", "test_*.py"]

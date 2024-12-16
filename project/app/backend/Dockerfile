FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install poetry

RUN poetry install

COPY ssl/selfsigned.crt /app/ssl/selfsigned.crt
COPY ssl/selfsigned.key /app/ssl/selfsigned.key

EXPOSE 8000

CMD ["poetry", "run", "uvicorn", "main:app", \
     "--host", "0.0.0.0", "--port", "8000", \
     "--ssl-keyfile", "/app/ssl/selfsigned.key", \
     "--ssl-certfile", "/app/ssl/selfsigned.crt"]


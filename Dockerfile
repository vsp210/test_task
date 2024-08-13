# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 1337

CMD ["python", "manage.py", "runserver", "0.0.0.0:1337"]

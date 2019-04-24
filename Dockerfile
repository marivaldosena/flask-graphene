FROM python:3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver --port 8000 --host 0.0.0.0
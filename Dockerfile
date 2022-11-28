FROM python:3.10
ENV PYTHONBUFFERED 1
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY djangomicroservices /app
CMD python manage.py runserver 0.0.0.0:8000
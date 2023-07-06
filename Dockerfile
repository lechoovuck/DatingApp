FROM python:3.11
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

RUN apt-get update && apt-get install -f
RUN apt-get update && apt-get install -y python3-pkg-resources

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py createsuperuser --noinput
CMD python manage.py runserver 0.0.0.0:8000

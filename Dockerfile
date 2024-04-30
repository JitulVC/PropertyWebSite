FROM python:3.9-slim-buster

COPY requirements.txt /

RUN pip3 install --upgrade pip

RUN pip3 install -r /requirements.txt

COPY . /app

WORKDIR /app

EXPOSE 80
CMD ["gunicorn", "wsgi:app", "-b", "0.0.0.0:80"]
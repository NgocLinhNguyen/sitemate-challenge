FROM python:3.9.16
RUN apt-get update -y
RUN apt-get install build-essential -y
RUN apt-get install libpq-dev -y

COPY ./requirements.txt /requirements.txt
RUN pip3 install -r requirements.txt

COPY . /sitemate_challenge_backend
WORKDIR /sitemate_challenge_backend/

ENV PYTHONPATH=/sitemate_challenge_backend
EXPOSE 8000

CMD ["python", "-u", "api_server.py"]

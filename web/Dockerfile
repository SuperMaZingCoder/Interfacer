FROM python:3.9.1-buster

WORKDIR /app/

COPY . /app/

RUN pip install --upgrade pip
RUN pip install --upgrade pipenv && pipenv install --system --deploy

CMD [ "uwsgi", "app.ini" ]
FROM python:3.8-bullseye
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN python -m pip install -r requirements.txt

COPY . /code/

RUN chmod +x docker-entrypoint.sh

CMD [ "./docker-entrypoint.sh" ]

EXPOSE 8000


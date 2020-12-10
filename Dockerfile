FROM python:3.8-alpine

RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers python3-dev jpeg-dev zlib-dev
RUN pip3 install django
RUN pip3 install gunicorn
RUN pip3 install Pillow
RUN pip3 install whitenoise
RUN apk del .tmp

RUN mkdir /app

WORKDIR /app

ADD . /app/

ENV PYTHONUNBUFFERED=1
ENV PORT=8080

# EXPOSE 8080

CMD  ["gunicorn", "--chdir", "restaurant", "--workers", "5", "--threads", "2", "--bind", ":8080", "restaurant.wsgi:application"]
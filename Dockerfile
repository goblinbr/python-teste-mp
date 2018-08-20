FROM python:3.6.6-alpine3.8

LABEL maintainer="rodrigo.goblin@gmail.com"

COPY . /app
WORKDIR /app

ENTRYPOINT ["python3"]
CMD ["app.py"]
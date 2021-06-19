FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /video_library/requirements.txt
RUN pip install -r /video_library/requirements.txt

COPY . /video_library/
WORKDIR /video_library/

EXPOSE 8000

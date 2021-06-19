FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV DJANGO_ENV dev
ENV DOCKER_CONTAINER 1

COPY ./requirements.txt /video_library_code/requirements.txt
RUN pip install -r /video_library_code/requirements.txt

COPY . /video_library_code/
WORKDIR /video_library_code/

EXPOSE 8000

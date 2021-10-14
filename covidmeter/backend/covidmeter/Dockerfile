# pull the official base image
FROM python:3.9.5-slim
# set work directory
WORKDIR /Users/raveedahmad/gitlab/training-repo/raveed-covidmeter/backend/covidmeter/docker
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /Users/raveedahmad/gitlab/training-repo/raveed-covidmeter/backend/covidmeter/docker
RUN pip install -r requirements.txt
RUN apt-get update &&\
    apt-get install -y binutils libproj-dev gdal-bin
# copy project
COPY . /Users/raveedahmad/gitlab/training-repo/raveed-covidmeter/backend/covidmeter/docker
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
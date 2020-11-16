FROM python:3.8-buster

ENV DEBIAN_FRONTEND=noninteractive

COPY ./docker/openproblems/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -U -r requirements.txt

# Install single-cell open problems
COPY . /usr/src/singlecellopenproblems
RUN pip install -e /usr/src/singlecellopenproblems

RUN apt-get clean -y && apt-get autoremove -y

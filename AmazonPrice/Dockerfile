#FROM python:2-onbuild 
FROM centos:centos6
RUN yum install -y gcc  python python-pip libxslt-devel python-devel python-setuptools screen mc
RUN easy_install pip
ADD requirements.txt /src/requirements.txt
RUN cd /src; pip install -r requirements.txt
ADD . /src
CMD [ "python", "broker.py" ]

FROM ubuntu

RUN apt update
RUN apt install python3 python3-pip -y
RUN pip3 install flask
COPY . /spe_project

CMD python3 /spe_project/main.py
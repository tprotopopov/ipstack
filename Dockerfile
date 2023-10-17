# Use an official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.9

WORKDIR /app

COPY app/ .

RUN pip3 install --trusted-host pypi.python.org pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python3", "./main.py"]
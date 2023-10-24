FROM python:3.9

WORKDIR /app

COPY app/ .

RUN pip3 install --upgrade pip
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

ENTRYPOINT ["python3","main.py"]

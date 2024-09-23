FROM python:slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt


COPY . .

RUN python setup.py && python adduser.py

EXPOSE 8080

CMD ["python", "softdes.py"]

FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN python setup.py
RUN python adduser.py

EXPOSE 8080

CMD ["python", "softdes.py"]

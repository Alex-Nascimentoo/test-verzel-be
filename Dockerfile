FROM python:3.10.12

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN export FLASK_APP=app

CMD ["flask", "run", "--host=0.0.0.0"]
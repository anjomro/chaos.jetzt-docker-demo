FROM python:3.12-slim

RUN pip install flask

WORKDIR /chaos

COPY app.py /chaos/app.py

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
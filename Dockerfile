FROM python:3.7-slim
RUN pip install flask
RUN pip install flask-mysql
COPY connection.py /connection.py
CMD ["python", "connection.py"]

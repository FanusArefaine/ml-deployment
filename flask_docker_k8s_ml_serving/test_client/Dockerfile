FROM python:3.6
WORKDIR /test_client
COPY requirements.txt /test_client
RUN pip install -r ./requirements.txt
COPY client.py /test_client
CMD ["python", "/test_client/client.py"]
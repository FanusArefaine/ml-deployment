FROM python:3.6
WORKDIR /train
COPY requirements.txt /train
RUN pip install -r ./requirements.txt
COPY train_model.py /train
CMD ["python", "/train/train_model.py"]
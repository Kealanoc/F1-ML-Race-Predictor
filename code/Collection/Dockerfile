FROM python:3

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
ADD my_script.py /
CMD [ "python3", "./index.py" ]
FROM python:3.9
WORKDIR src

COPY . /src

COPY . /requirements.txt/src/requirements.txt

EXPOSE 8000

RUN pip3 install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["python3", "manage.py", "migrate"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
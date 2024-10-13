
FROM python:3.12


WORKDIR /remove-bg


COPY ./requirements.txt /remove-bg/requirements.txt


RUN pip install --no-cache-dir --upgrade -r /remove-bg/requirements.txt


COPY . /remove-bg/app

EXPOSE 10000


CMD ["fastapi", "run", "app/main.py", "--port", "10000"]
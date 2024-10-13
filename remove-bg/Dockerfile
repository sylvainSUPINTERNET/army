FROM python:3.12-slim

WORKDIR /remove-bg

COPY ./requirements.txt /remove-bg/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /remove-bg/requirements.txt \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

    # Download the model
RUN mkdir -p ~/.u2net

COPY . /remove-bg/app

EXPOSE 10000

CMD ["fastapi", "run", "app/main.py", "--port", "10000"]

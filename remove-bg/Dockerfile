# Can't use alpine due to onnxruntime not compatible with musl ...
FROM python:3.12-slim

WORKDIR /remove-bg

COPY ./requirements.txt /remove-bg/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /remove-bg/requirements.txt \
    && apt-get update \
    && apt-get install -y --no-install-recommends wget \
    && apt-get clean \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir -p /root/.u2net \
    && wget -O /root/.u2net/silueta.onnx https://github.com/danielgatis/rembg/releases/download/v0.0.0/silueta.onnx

COPY . /remove-bg/app

# defaut port for Render
EXPOSE 10000

CMD ["fastapi", "run", "app/main.py", "--port", "10000"]
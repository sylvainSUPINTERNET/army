# Remove.bg Fork


## Description

https://www.remove.bg/

https://www.similarweb.com/website/remove.bg/#traffic


## Objective

User can : 

- Remove background from images, using link, or upload
- Download the image

## Usage

```` bash

python -m pip install -r requirements.txt


fastapi dev

````

## Docker


```` bash 

docker build -t sylvaindev/army-background-remove:1.0.0 .

docker run -p 8000:10000 -e U2NET_HOME='/root/.u2net/' sylvaindev/army-background-remove:1.0.0

docker push sylvaindev/army-background-remove:1.0.0


````

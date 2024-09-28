from fastapi import UploadFile
from rembg import remove
from PIL import Image
import requests
from io import BytesIO

def remove_bg(file: UploadFile, media_url: str, allowed_types: list[str]):

    if file == None and ( media_url == None or media_url == "" ):
        return None

    if file != None:

        if file.content_type not in allowed_types:
            raise Exception(f"Invalid content type: {content_type}")

        input_image = Image.open(BytesIO(file.file.read())).convert('RGB')
        output_image = remove(input_image)
        return output_image, file.content_type


    if media_url != None or media_url != "" :
        url = f"{media_url}"
        response = requests.get(url)
        content_type = response.headers.get('Content-Type')

        if content_type not in allowed_types:
            raise Exception(f"Invalid content type: {content_type}")
        
        if response.content == None:
            raise Exception(f"Invalid content: {response.content}")

        input_image = Image.open(BytesIO(response.content)).convert('RGB')

        output_image = remove(input_image)
        return output_image, content_type

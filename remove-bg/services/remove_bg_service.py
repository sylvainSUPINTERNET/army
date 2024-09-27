from fastapi import UploadFile
from rembg import remove
from PIL import Image
import requests
from io import BytesIO


def remove_bg(file: UploadFile, media_url: str):

    if ( file == None and ( media_url == None or media_url == "" ) ):
        return None

    if ( file != None ):
        input_image = Image.open(BytesIO(file.file.read())).convert('RGB')
        output_image = remove(input_image)
        # output_image.show()
        # output_image.save('removed_bg.png
        return output_image

    if ( media_url != None or media_url != "" ):
        url = f"{media_url}"
        response = requests.get(url)
        content_type = response.headers.get('Content-Type')

        if 'image' not in content_type:
            raise Exception(f"Invalid content type: {content_type}")


        if response.content == None:
            raise Exception(f"Invalid content: {response.content}")

        input_image = Image.open(BytesIO(response.content)).convert('RGB')

        output_image = remove(input_image)
        # output_image.show()
        # output_image.save('removed_bg.png')
        return output_image

import uuid
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from PIL import Image
from io import BytesIO

router = APIRouter()


@router.post("/download")
async def download(file: UploadFile = File(None), type: str = Form(None)):
    input_image = Image.open(BytesIO(file.file.read())).convert('RGB')
    output_buffer = BytesIO()

    media_type = ""
    extension = ""

    if type not in ["png","webp"]:
        return JSONResponse(content={"error": "Invalid type provided"}, status_code=400)

    if type == "png":
        input_image.save(output_buffer, format="PNG", quality=100)
        media_type = "image/png"
        extension = "png"
        
    if type == "webp":
        input_image.save(output_buffer, format="WEBP", quality=100)
        media_type = "image/webp"
        extension = "webp"
    output_buffer.seek(0)

    print(output_buffer)
    
    return StreamingResponse(output_buffer, media_type=media_type, headers={"Content-Disposition": f"attachment; filename={str(uuid.uuid4())}.{extension}"})

    # if ( file == None and ( media_url == None or media_url == "" ) ):
    #     return JSONResponse(content={"error": "No file or media_url provided"}, status_code=400)


    # try:
    #     output_image, content_type = remove_bg_service.remove_bg(file, media_url, allowed_types)
    #     img_io = io.BytesIO()

    #     if "png" in content_type or "PNG" in content_type or "jpg" in content_type or "JPG" in content_type or "jpeg" in content_type or "JPEG" in content_type:
    #         output_image.save(img_io, format='PNG')
    #         img_io.seek(0)
    #     # elif "jpeg" in content_type or "JPEG" in content_type:
    #     #     if output_image.mode == "RGBA":
    #     #         output_image = output_image.convert("RGB")  # Convertir en RGB
    #     #     output_image.save(img_io, format='JPEG')
    #     #     img_io.seek(0)
    #     else:
    #         img_io.seek(0)
    #         raise Exception(f"Invalid content type: {content_type}")


    #     return StreamingResponse(img_io, media_type=f"{content_type}")
    # except Exception as e:
    #     return JSONResponse(content={"error": str(e)}, status_code=400)

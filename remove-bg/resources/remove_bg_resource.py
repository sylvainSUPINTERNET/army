
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from services import remove_bg_service
import io

router = APIRouter()

allowed_types = ["image/png", "image/jpg", "image/jpeg"]

@router.post("/removebg")
async def whisper_transcribe(
        file: UploadFile = File(None), 
        media_url: str = Form(None)
    ):

    if ( file == None and ( media_url == None or media_url == "" ) ):
        return JSONResponse(content={"error": "No file or media_url provided"}, status_code=400)


    try:
        output_image, content_type = remove_bg_service.remove_bg(file, media_url, allowed_types)
        img_io = io.BytesIO()

        if "png" in content_type or "PNG" in content_type:
            output_image.save(img_io, format='PNG')
            img_io.seek(0)
        elif "jpeg" in content_type or "JPEG" in content_type:
            if output_image.mode == "RGBA":
                output_image = output_image.convert("RGB")  # Convertir en RGB
            output_image.save(img_io, format='JPEG')
            img_io.seek(0)
        else:
            img_io.seek(0)
            raise Exception(f"Invalid content type: {content_type}")


        return StreamingResponse(img_io, media_type=f"{content_type}")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

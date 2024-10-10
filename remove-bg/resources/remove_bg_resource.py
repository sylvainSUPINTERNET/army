
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from services import remove_bg_service
import io

router = APIRouter()

allowed_types = ["image/png", "image/jpg", "image/jpeg", "image/webp"]

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
        
        if content_type in allowed_types:
            if content_type == "image/webp":
                output_image.save(img_io, format='WEBP')
                img_io.seek(0)
            else:
                output_image.save(img_io, format='PNG')
                img_io.seek(0)
        else:
            raise Exception(f"Invalid content type: {content_type}")

        return StreamingResponse(img_io, media_type=f"{content_type}")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

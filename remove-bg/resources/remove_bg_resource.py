
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from services import remove_bg_service
import io
import logging


router = APIRouter()
logger = logging.getLogger(__name__)

allowed_types = ["image/png", "image/jpg", "image/jpeg", "image/webp"]

@router.post("/removebg")
async def remove_bg(
        file: UploadFile = File(None), 
        media_url: str = Form(None)
    ):

    logger.info("[REMOVEBG-SVC] called")

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
        logger.error(f"Error: {str(e)}")
        return JSONResponse(content={"error": str(e)}, status_code=400)

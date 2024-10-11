import uuid
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
from PIL import Image
from io import BytesIO
import logging

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/download")
async def download(file: UploadFile = File(None), type: str = Form(None)):

    logger.info("[DOWNLOAD-SVC] called")
    input_image = Image.open(BytesIO(file.file.read())).convert('RGB')
    output_buffer = BytesIO()

    media_type = ""
    extension = ""

    try:
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
        
        return StreamingResponse(output_buffer, media_type=media_type, headers={"Content-Disposition": f"attachment; filename={str(uuid.uuid4())}.{extension}"})
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return JSONResponse(content={"error": str(e)}, status_code=400)
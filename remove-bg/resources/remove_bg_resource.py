
from fastapi import APIRouter, File, Form, UploadFile
from fastapi.responses import FileResponse, JSONResponse, StreamingResponse
from services import remove_bg_service
import io


# TODO => handle properly the extension of the file
# => allow to donwload jpg or png up to the user

router = APIRouter()

allowed_types = ["image/png", "image/jpg", "image/jpeg"]

@router.post("/removebg")
async def whisper_transcribe(
        file: UploadFile = File(None), 
        media_url: str = Form(None)
    ):

    if ( file == None and ( media_url == None or media_url == "" ) ):
        return JSONResponse(content={"error": "No file or media_url provided"}, status_code=400)
    
    if ( file != None and file.content_type not in allowed_types ):
        return JSONResponse(content={"error": "Invalid file type"}, status_code=400)

    try:
        output_image = remove_bg_service.remove_bg(file, media_url)
        img_io = io.BytesIO()
        output_image.save(img_io, format='PNG')
        img_io.seek(0)

        return StreamingResponse(img_io, media_type="image/png")
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=400)

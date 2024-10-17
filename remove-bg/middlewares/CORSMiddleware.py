from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import os

allowed_origins = os.getenv("CORS_UI_ORIGIN", "*").split(",")

"""
For some reason starlette / fastapi middleware cors built-in is not working ...
"""
class CORSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        request_origin = request.headers.get('Origin', None)
        response = await call_next(request)

        if request_origin is None:
            request_origin = ""
        elif request_origin in allowed_origins:
            response.headers['Access-Control-Allow-Origin'] = request_origin
        else:
            response.headers['Access-Control-Allow-Origin'] = ""

        response.headers['Access-Control-Allow-Credentials'] = 'true' 
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Expose-Headers'] = 'Content-Disposition'
        
        if request.method == 'OPTIONS':
            response = Response(status_code=204)
            if request_origin in allowed_origins:
                response.headers['Access-Control-Allow-Origin'] = request_origin
            else:
                response.headers['Access-Control-Allow-Origin'] = ""
                
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
            response.headers['Access-Control-Allow-Headers'] = '*'
            response.headers['Access-Control-Expose-Headers'] = 'Content-Disposition'

        return response
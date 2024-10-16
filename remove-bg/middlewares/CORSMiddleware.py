from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import Response
import os


"""
For some reason starlette / fastapi middleware cors built-in is not working ...
"""
class CORSMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):

        allow_origin = os.getenv("CORS_UI_ORIGIN", "*")
        
        response = await call_next(request)

        # Keep in mind 
        # Can't use wildcard '*' for 'Access-Control-Allow-Origin' with allow-credentials set to true
        
        response.headers['Access-Control-Allow-Origin'] = allow_origin
        response.headers['Access-Control-Allow-Credentials'] = 'true' 
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
        response.headers['Access-Control-Allow-Headers'] = '*'
        response.headers['Access-Control-Expose-Headers'] = 'Content-Disposition'
        
        if request.method == 'OPTIONS':
            response = Response(status_code=204)
            response.headers['Access-Control-Allow-Origin'] = allow_origin
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS, PUT, DELETE'
            response.headers['Access-Control-Allow-Headers'] = '*'
            response.headers['Access-Control-Expose-Headers'] = 'Content-Disposition'

        return response
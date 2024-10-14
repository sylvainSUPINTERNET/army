from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from dotenv import load_dotenv
from resources import download_resource, monitor_resource, remove_bg_resource
import os 

load_dotenv()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(threadName)s - %(levelname)s - %(message)s')

app = FastAPI(title="remove-bg-api", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv("CORS_UI_ORIGIN", "*") ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=['Content-Disposition']
)

# Register your routes
app.include_router(prefix="/api", router=remove_bg_resource.router)
app.include_router(prefix="/api", router=download_resource.router)
app.include_router(router=monitor_resource.router)
 


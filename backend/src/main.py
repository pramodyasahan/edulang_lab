from fastapi import FastAPI, APIRouter
from api.routes.text_processing import text_processing

app = FastAPI()

text_router = APIRouter()

text_router.add_api_route("/process-text", text_processing, methods=["POST"])

app.include_router(text_router)
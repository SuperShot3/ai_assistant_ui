from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import logging
from datetime import datetime

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Подключаем статические файлы и шаблоны
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatMessage(BaseModel):
    message: str

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: ChatMessage):
    try:
        logger.info(f"Получен запрос: {message.message}")
        
        # Проверяем специальную команду
        if message.message.lower() == "test":
            try:
                response = requests.get(
                    "http://localhost:3333/test",
                    timeout=5
                )
                if response.status_code == 200:
                    return {"response": "✅ API сервер работает!"}
                else:
                    return {"response": "❌ API сервер недоступен"}
            except:
                return {"response": "❌ API сервер недоступен"}
        
        # Отправляем запрос к локальному API
        logger.info("Отправляем запрос к API...")
        response = requests.post(
            "http://localhost:3333/chat",  # Изменено на localhost
            json={"message": message.message},
            headers={"Content-Type": "application/json"},
            timeout=60
        )
        
        logger.info(f"Статус ответа API: {response.status_code}")
        logger.info(f"Заголовки ответа: {response.headers}")
        logger.info(f"Тело ответа: {response.text}")
        
        if response.status_code == 200:
            return response.json()
        else:
            logger.error(f"Ошибка API: {response.status_code} - {response.text}")
            return {"response": "Извините, произошла ошибка при обработке запроса"}
            
    except requests.Timeout:
        logger.error("Таймаут при запросе к API")
        return {"response": "API не ответил вовремя. Пожалуйста, попробуйте позже."}
    except requests.ConnectionError:
        logger.error("Ошибка подключения к API")
        return {"response": "Не удалось подключиться к API. Проверьте доступность сервера."}
    except Exception as e:
        logger.error(f"Ошибка: {str(e)}")
        return {"response": "Произошла ошибка при обработке запроса"}

@app.get("/test")
async def test():
    return {"status": "ok", "message": "Сервер работает!"} 
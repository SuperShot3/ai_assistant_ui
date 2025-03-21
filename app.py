from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests
import logging

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = FastAPI()

# Настройка CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Разрешаем все источники для разработки
    allow_credentials=True,
    allow_methods=["*"],  # Разрешаем все методы
    allow_headers=["*"],  # Разрешаем все заголовки
)

# Монтирование статических файлов и шаблонов
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class ChatMessage(BaseModel):
    message: str

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/chat")
async def chat(message: ChatMessage):
    try:
        logger.info(f"Получен запрос: {message.message}")
        
        # Отправляем запрос к вашему API
        logger.info("Отправляем запрос к API...")
        response = requests.post(
            "http://192.168.1.7:3333/chat",
            json={"message": message.message},
            headers={"Content-Type": "application/json"},
            timeout=60  # Увеличиваем таймаут до 60 секунд
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
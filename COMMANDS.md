# Команды для управления сервером

## 🚀 Запуск сервера

### Активация виртуального окружения
```bash
# MacOS/Linux
source venv/bin/activate

# Windows
.\venv\Scripts\activate
```

### Запуск сервера для разработки
```bash
uvicorn app:app --reload
```

### Запуск сервера для продакшена
```bash
uvicorn app:app --host 0.0.0.0 --port 8000
```

## 🔄 Перезапуск сервера

### Остановка текущего процесса
```bash
# Найти процессы на порту 8000
lsof -i :8000

# Остановить все процессы uvicorn
pkill -f uvicorn
```

## 📦 Управление зависимостями

### Установка зависимостей
```bash
pip install -r requirements.txt
```

### Обновление requirements.txt
```bash
pip freeze > requirements.txt
```

## 🌐 Ngrok туннель

### Запуск Ngrok
```bash
ngrok http 8000
```

### Решение проблем с Ngrok

1. Если сайт недоступен (ERR_NGROK_3200):
   ```bash
   # Перезапустить Ngrok
   pkill -f ngrok
   ngrok http 8000
   ```

2. Проверка статуса Ngrok:
   ```bash
   # Проверить активные туннели
   ps aux | grep ngrok
   
   # Проверить статус подключения
   curl http://localhost:4040/api/tunnels
   ```

3. Альтернативные действия:
   - Перезапустите Ngrok агент
   - Проверьте подключение к интернету
   - Убедитесь, что ваш authtoken актуален:
   ```bash
   ngrok authtoken ВАШ_ТОКЕН
   ```
   - Попробуйте использовать другой регион:
   ```bash
   ngrok http 8000 --region eu
   ```

4. Временные решения:
   - Используйте локальный адрес: http://localhost:8000
   - Настройте проброс портов на роутере
   - Используйте альтернативные сервисы (localhost.run, localtunnel)

## 🔧 Полезные команды

### Проверка статуса сервера
```bash
curl http://localhost:8000
```

### Очистка кэша Python
```bash
find . -type d -name "__pycache__" -exec rm -r {} +
```

### Проверка логов
```bash
tail -f uvicorn.log
```

## ⚠️ Решение проблем

1. Если порт 8000 занят:
   ```bash
   pkill -f uvicorn
   # или
   kill $(lsof -t -i:8000)
   ```

2. Если виртуальное окружение не активируется:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Если не работает API:
   - Проверьте файл .env
   - Проверьте подключение к интернету
   - Проверьте API ключ

## 🔍 Мониторинг

### Просмотр активных процессов Python
```bash
ps aux | grep python
```

### Мониторинг использования CPU/RAM
```bash
top -pid $(pgrep -f uvicorn)
``` 
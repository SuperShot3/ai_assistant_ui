# AI Chat Application

Веб-приложение для общения с AI ассистентом через чат-интерфейс.

## Структура проекта

```
ai_showcase/
├── app.py              # FastAPI сервер
├── static/             # Статические файлы
│   ├── styles.css      # Стили
│   └── favicon.svg     # Иконка сайта
├── templates/          # HTML шаблоны
│   └── index.html      # Главная страница
└── requirements.txt    # Зависимости проекта
```

## Требования

- Python 3.8+
- pip (менеджер пакетов Python)

## Установка

1. Клонируйте репозиторий:
```bash
git clone <repository-url>
cd ai_showcase
```

2. Создайте виртуальное окружение и активируйте его:
```bash
python -m venv venv
source venv/bin/activate  # для Linux/Mac
# или
venv\Scripts\activate  # для Windows
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

## Запуск

1. Запустите FastAPI сервер:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

2. В отдельном терминале запустите ngrok для создания туннеля:
```bash
ngrok http 8000
```

3. Откройте URL, предоставленный ngrok, в вашем браузере.

## Конфигурация

- API сервер должен быть доступен по адресу `http://192.168.&.&:*****`
- FastAPI сервер работает на порту 8000
- Таймаут для API запросов установлен на 60 секунд

## Особенности

- Современный дизайн с использованием CSS Grid и Flexbox
- Адаптивный интерфейс для мобильных устройств
- Индикатор набора текста
- Обработка ошибок и таймаутов
- Поддержка CORS для безопасного взаимодействия
- Логирование всех запросов и ответов

## Технологии

- FastAPI - веб-фреймворк
- Jinja2 - шаблонизатор
- ngrok - туннелирование
- requests - HTTP клиент
- CSS Grid и Flexbox - верстка

## Безопасность

- CORS настроен для разрешения запросов с любых источников (для разработки)
- Таймауты для предотвращения зависания запросов
- Обработка ошибок подключения и таймаутов

## Разработка

Для внесения изменений:
1. Внесите изменения в код
2. Сервер автоматически перезагрузится благодаря флагу `--reload`
3. Проверьте логи в консоли для отладки

## Логирование

Логи содержат:
- Время запроса
- Уровень сообщения
- Детали запроса и ответа
- Ошибки и исключения 
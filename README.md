# Figma Local File AI Connector

MCP-сервер для Figma AI, который читает требования из локального текстового файла и публикует их через публичный HTTPS-туннель.

## Установка

```bash
pip install mcp
```

## Запуск

```bash
# Использовать файл requirements.txt из текущей папки
python server.py

# Или указать свой файл
$env:REQUIREMENTS_FILE = "C:\path\to\my-requirements.txt"
python server.py
```

Сервер создаст SSH-туннель через localhost.run и выведет публичный HTTPS URL:

```
=== FIGMA CONNECTOR URL: https://xxxxxx.lhr.life/sse ===
```

## Подключение к Figma

1. Запусти сервер: `python server.py`
2. Скопируй URL из вывода (вида `https://xxxxxx.lhr.life/sse`)
3. В Figma: чат AI → Connectors → Add custom connector → MCP Server
4. Вставь скопированный URL → Connect

## Использование в чате Figma AI

- "Сверстай экран авторизации согласно требованиям из файла"
- "Сверь этот макет с требованиями из файла. Всё ли я учёл?"
- "Прочитай требования и проверь, соответствует ли им этот дизайн"

## Переменные окружения

- `REQUIREMENTS_FILE` — путь к файлу с требованиями (по умолчанию: `./requirements.txt`)

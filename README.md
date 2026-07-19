# Figma Local File AI Connector

MCP-сервер для Figma AI, который читает требования из локального текстового файла.

## Деплой на VPS (Dokploy + Traefik)

```bash
docker-compose up --build -d
```

Сервер будет доступен по адресу: `https://figma.benzomesto.ru/sse`

## Подключение к Figma

1. Убедись, что сервер запущен на VPS
2. В Figma: чат AI → Connectors → Add custom connector → MCP Server
3. Введи URL: `https://figma.benzomesto.ru/sse`
4. Нажми Connect

## Использование в чате Figma AI

- "Сверстай экран авторизации согласно требованиям из файла"
- "Сверь этот макет с требованиями из файла. Всё ли я учёл?"
- "Прочитай требования и проверь, соответствует ли им этот дизайн"

## Переменные окружения

- `REQUIREMENTS_FILE` — путь к файлу с требованиями (по умолчанию: `./requirements.txt`)

# 📊 Цифровая карта
Запуск Apache Superset в Docker
---

### Структура проекта

```plaintext
superset-project/
├── data/                       # Исходные данные (CSV, Excel и др.)
├── geojson/                    # Гео-данные в формате GeoJSON
├── pg_data/                    # Данные PostgreSQL (для внешней БД)
├── superset_data/              # Конфигурации и метаданные Superset
├── docker-compose.yml          # Конфигурация Docker Compose
├── superset_config.py          # Настройки Superset
├── init.sql                    # SQL-скрипт инициализации БД (опционально)
└── README.md                   # Документация проекта
```

## 🚀 Быстрый старт

**!!!Требуется установленный Docker и Docker Compose!!!**

### 1. Клонировать репозиторий

```bash
git clone https://github.com/your-org/superset-project.git
cd superset-project
```

### 2. Запустить Superset

```bash
docker compose up --build
```

### 3. Инициализировать Superset (только при первом запуске)

```bash
docker exec -it superset superset fab create-admin
# Вводите придуманные логин, email и пароль (их запомните, будете использовать при входе в superset!)

docker exec -it superset superset db upgrade
docker exec -it superset superset init
```

Теперь Superset будет доступен по адресу (надо будет подождать минутку-две):

🔗 `http://localhost:8088`

## 📤 Экспорт и 📥 Импорт дашбордов

### 📤 Экспорт:

```bash
docker exec -it superset superset export-dashboards --path /app/exports/
docker cp superset:/app/exports ./exports
```

### 📥 Импорт дашбордов:

```bash
docker cp ./exports superset:/app/exports
docker exec -it superset superset import-dashboards --path /app/exports/
```


## ⚙️ Полезные команды

### Открыть терминал контейнера:

```bash
docker exec -it superset bash
```

### Перезапуск:

```bash
docker compose restart
```

### Просмотр логов:

```bash
docker-compose logs superset
```
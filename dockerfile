# Stage 1: Сборка приложения с зависимостями
FROM python:3.12-alpine AS builder

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем только файл зависимостей
COPY requirements.txt .

# Устанавливаем зависимости в локальную папку пользователя
RUN pip install --user -r requirements.txt && rm -rf /root/.cache/pip

# Копируем исходный код приложения
COPY . .

# Stage 2: Финальный минимальный образ
FROM python:3.12-alpine

WORKDIR /app

# Копируем приложение из стадии сборки
COPY --from=builder /app /app
# Переносим установленные пакеты
COPY --from=builder /root/.local /root/.local

# Добавляем папку с бинарниками в PATH
ENV PATH=/root/.local/bin:$PATH

# Открываем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "API.py"]
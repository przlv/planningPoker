FROM python:3.12-slim

WORKDIR /planningPoker

RUN pip install --upgrade pip && \
    pip install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root

COPY . .
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]

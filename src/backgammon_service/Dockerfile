# Use the official Python image as the base
FROM python:3.12

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /usr/local/backgammon_service

COPY . .

RUN uv sync --frozen

EXPOSE 8001

CMD pytest test_main.py && uvicorn main:app --host 0.0.0.0 --port 8001

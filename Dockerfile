FROM ghcr.io/astral-sh/uv:python3.12-bookworm

ADD . /app

WORKDIR /app/app

RUN uv sync --locked

CMD [ "uv", "run", "uvicorn","main:app", "--host","0.0.0.0", "--port","8000" ]
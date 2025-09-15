FROM ghcr.io/astral-sh/uv:python3.12-bookworm

ADD . /

WORKDIR /

RUN uv sync --locked

# CMD [ "uv", "run", "uvicorn","main:app", "--host","0.0.0.0", "--port","8000" ]

CMD ["uv", "run", "python", "-m","app.main"]
FROM python:3.8-slim-buster as production
LABEL maintainer="Alisher A. Khassanov <a.khssnv@gmail.com>" \
      description="Khassan-O-vBot" \
      org.opencontainers.image.source="https://github.com/khssnv/Khassan-O-vBot"

ARG APP_PATH=/github.com/khssnv/Khassan-O-vBot/

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:${APP_PATH}"
ENV POETRY_VERSION 1.1.8

RUN pip install "poetry==$POETRY_VERSION"

WORKDIR $APP_PATH
COPY poetry.lock pyproject.toml $APP_PATH
RUN poetry config virtualenvs.create false \
  && poetry install --no-dev --no-interaction --no-ansi

COPY . $APP_PATH

CMD ["python", "-m", "khassan_o_vbot"]

FROM python:3.8-slim-buster as production
LABEL maintainer="Alisher A. Khassanov <a.khssnv@gmail.com>" \
      description="Khassan-O-vBot" \
      org.opencontainers.image.source="https://github.com/khssnv/Khassan-O-vBot"

ARG APP_PATH=/github.com/khssnv/Khassan-O-vBot

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:${APP_PATH}"
WORKDIR $APP_PATH

# Dependencies
COPY Pipfile* "${APP_PATH}/"
RUN pip install pipenv
RUN pipenv install --deploy --ignore-pipfile

# App code
ADD . $APP_PATH

CMD ["pipenv", "run", "khassan_o_vbot"]

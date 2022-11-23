FROM python:3.10.0-bullseye

WORKDIR /app
COPY api /app/api
COPY poetry.lock pyproject.toml README.md /app/

RUN pip install poetry

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]

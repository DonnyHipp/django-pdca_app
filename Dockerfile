FROM python:3.12.1-slim-bullseye

WORKDIR /app/pdca

COPY pyproject.toml poetry.lock /app/pdca

RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install --no-dev
COPY . /app/
EXPOSE 8000
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
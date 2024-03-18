FROM python:3.11.7

WORKDIR /django_develop_way

COPY poetry.lock pyproject.toml /django_develop_way/
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -U poetry && \
    poetry config --local virtualenvs.create false && \
    poetry install

COPY . /django_develop_way/

CMD ["sh", "-c", "gunicorn backend.wsgi:application --bind 0.0.0.0:8000 --log-level=info --timeout=600 --workers 4"]

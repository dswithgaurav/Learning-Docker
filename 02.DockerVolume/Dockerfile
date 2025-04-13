FROM python:slim

WORKDIR /src

COPY src/ /src

ENV PORT=80

# Run when image is created
RUN pip install -r requirements.txt

EXPOSE $PORT

# Adding a Volume (inside container)
VOLUME ["/src/logs/"]

# Runs when container is started
CMD ["sh", "-c", "uvicorn app:app --host 0.0.0.0 --port $PORT"]
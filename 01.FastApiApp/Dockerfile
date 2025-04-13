FROM python:slim

WORKDIR /src

COPY src/ /src

# Run when image is created
RUN pip install -r requirements.txt

EXPOSE 8000

# Runs when container is started
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
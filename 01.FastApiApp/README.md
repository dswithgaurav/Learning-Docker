
### **Step 1: Create a FastAPI Application**
Create a file `main.py` with the following content:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q}
```

---

### **Step 2: Create a `requirements.txt` file**
List the dependencies needed:

```
fastapi
uvicorn
```

---

### **Step 3: Create a `Dockerfile`**
Create a `Dockerfile` to containerize your FastAPI app.

```dockerfile
# Use an official Python runtime as a parent image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 8000
EXPOSE 8000

# Command to run the FastAPI app
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### **Step 4: Build the Docker Image**
Run the following command in the directory containing your `Dockerfile`:

```bash
docker build -t fastapi-app .
```

---

### **Step 5: Run the Container**
Start the container with:

```bash
docker run -d -p 8000:8000 fastapi-app
```

Now, your FastAPI application is running in Docker, accessible at:

```
http://localhost:8000
```

---

### **Step 6: Test the API**
Use `curl` or a browser to check if it's working:

```bash
curl http://localhost:8000/
```

You should see:

```json
{"message":"Hello, FastAPI in Docker!"}
```

You can also visit `http://localhost:8000/docs` for the interactive Swagger UI.

<hr>

## Some Commands
```
```
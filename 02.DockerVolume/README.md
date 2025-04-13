
## 📘 Table of Contents
- Images, Containers & Volumes  
- Arguments & Environment Variables  
- Data Persistence Strategies  
- Docker Build & Run Steps  
- Volumes & Bind Mounts  


## 📦 Data Types in Containers

Understanding where and how data is stored is key to building reliable Dockerized applications.

### 1. **Application Code & Dependencies**
- Added during the `docker build` phase via `Dockerfile`
- Immutable after build
- 🔒 **Stored in Image**
> _E.g., FastAPI app code, Python libraries, system packages_

---

### 2. **Temporary Runtime Data**
- Exists only during the container's lifecycle
- Lost when the container stops
- 🧠 **Stored in Container Layer**
> _E.g., in-memory data, temp files, user session data_

---

### 3. **Persistent Data**
- Must survive container restarts or rebuilds
- 💾 **Stored in Volumes or Bind Mounts**
> _E.g., uploaded files, logs, databases (SQLite), user content_

---

## 🚀 Docker Commands

### 🔨 Build the Image
```bash
docker build -t fastapi-app .
```

### ▶️ Run the Container with Volume
```bash
docker run --name my_container --rm -p 1000:8000 -v logme:/app/logs fastapi-app
```

---

## 🗂️ Understanding Volumes

Volumes are **managed by Docker** and stored on the host file system. They're used to persist data **outside the container**.

- Automatically created if not existing
- Data is preserved even if the container is deleted
- Preferred over bind mounts for production

📌 Example Volume Mapping:
```
Host Path         →    Container Path
logme:/app/logs   →    Container logs directory
```

---

## 🧰 Volume Types

### 1. **Anonymous Volumes**
- Created without a name
- Used temporarily
- Removed when the container is deleted (unless retained manually)

```bash
docker run -v /app/temp-data fastapi-app
```

### 2. **Named Volumes**
- Explicitly named and reusable
- Good for persistent storage
- Can be inspected via `docker volume ls`

```bash
docker run -v logs:/app/logs fastapi-app
```

You can also inspect volume content using a temporary container:
```bash
docker run -it --rm -v logs:/app busybox sh
```

---

## 🔄 Bind Mounts

Bind mounts map a **specific folder on the host** to a path inside the container.

- Offers full control of the host path  
- Useful for local development (live code changes)

```bash
docker run -v $(pwd)/data:/app/data fastapi-app
```

📌 **Difference vs. Volumes**:
| Feature         | Volumes         | Bind Mounts       |
|-----------------|-----------------|-------------------|
| Managed by      | Docker          | You (host system) |
| Portability     | ✅ Yes           | ❌ No              |
| Dev Friendly    | ❌ Less ideal    | ✅ Great for local dev |
| Performance     | ✅ Better        | ⚠️ Depends on OS   |

---
## Read Only Volume (Bind-Mount)

> By default, Docker volumes and bind mounts are mounted with read and write permissions. If you want to make a **bind mount** read-only — meaning the container can read the files but not modify them — you can add `:ro` at the end of the mount path.  
>
> **Example:**  
> ```bash
> docker run -v /host/path:/container/path:ro my-image
> ```
> In this example, the container will be able to access the files at `/host/path`, but it won't be able to change them.




Here's a cleaned-up, clearer, and slightly expanded version of your note for better readability and understanding:

---

## 🐳 Docker Supports Build-time Arguments and Run-time Environment Variables

### 🔧 `ARG` (Build-time Argument)
- Used to **pass variables during the image build process**.
- Available **only inside the Dockerfile**, **not accessible to the running container** or application code.
- Typically used for things like installing dependencies or setting temporary build parameters.
- **Set using** `--build-arg` during the `docker build` command.

**Example:**
```Dockerfile
ARG VERSION=1.0
RUN echo "Building version $VERSION"
```
```bash
docker build --build-arg VERSION=2.0 -t my-image .
```

### 🌍 `ENV` (Environment Variable)
- Used to **set environment variables** that are available:
  - Inside the **Dockerfile** (can be used in `RUN`, `CMD`, etc.)
  - In the **running container and your application code**
- Can be set at **build-time** (in Dockerfile) or **run-time** (when starting the container).
- **Set using:**
  - `ENV` in Dockerfile  
  - `--env` or `-e` during `docker run`

**Example:**
```Dockerfile
ENV NODE_ENV=production
```
```bash
docker run -e NODE_ENV=development my-image
```

### Using .env with docker run
You can also pass environment variables from the .env file directly when running a container using the --env-file option.

**Example:**
```
docker run --env-file .env my-image
```
---


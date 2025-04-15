# 🚀 Steps to Deploy Docker Image to EC2

---

#### 1. 🛠️ Build the Docker Image (On Local Machine)

```bash
docker build -t my-image-name:latest .
```

> Replace `my-image-name` with your desired image name.

---

#### 2. ☁️ Push the Docker Image to a Container Registry (e.g., Docker Hub or Amazon ECR)

##### Option A: **Using Docker Hub**

1. Login to Docker Hub:

```bash
docker login
```

2. Tag your image:

```bash
docker tag my-image-name:latest your-dockerhub-username/my-image-name:latest
```

3. Push the image:

```bash
docker push your-dockerhub-username/my-image-name:latest
```

---

##### Option B: **Using Amazon ECR**

1. Authenticate Docker to your ECR registry:

```bash
aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com
```

2. Create a repository (if not already created):

```bash
aws ecr create-repository --repository-name my-image-name
```

3. Tag the image:

```bash
docker tag my-image-name:latest <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/my-image-name:latest
```

4. Push to ECR:

```bash
docker push <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/my-image-name:latest
```

---

#### 3. 💻 Pull the Docker Image on EC2 and Run the Container

SSH into your EC2 instance:

```bash
ssh -i your-key.pem ec2-user@your-ec2-public-ip
```

Make sure Docker is installed and running:

```bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -a -G docker ec2-user
```

Logout and log back in (for group changes to apply), then:

##### Option A: **Pull from Docker Hub**

```bash
docker pull your-dockerhub-username/my-image-name:latest
```

##### Option B: **Pull from Amazon ECR**

Re-authenticate ECR from EC2:

```bash
aws ecr get-login-password --region your-region | docker login --username AWS --password-stdin <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com
```

Then pull the image:

```bash
docker pull <aws_account_id>.dkr.ecr.<your-region>.amazonaws.com/my-image-name:latest
```

---

#### 4. ▶️ Run the Container

```bash
docker run -d -p 80:80 --name my-container-name my-image-name:latest
```

> Replace ports and names as needed.


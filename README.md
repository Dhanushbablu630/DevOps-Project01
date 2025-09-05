# DevOps Project – Python Application Deployment with Jenkins and Docker

## 📌 Project Overview
This project demonstrates a complete DevOps workflow where a Python application is deployed using **EC2, Jenkins, Docker, and GitHub**.  
The focus is not on the application itself, but on automating the **build, containerization, and deployment process**.

---

## 🚀 Steps Followed

### 1. Launched an EC2 Instance
- Created an **Ubuntu EC2 instance** on AWS.  
- Allocated security group rules to allow:
  - **Port 22 (SSH)**
  - **Port 8080 (Jenkins)**
  - **Port 3000 (App – optional)**
  - <img width="1830" height="705" alt="Image" src="https://github.com/user-attachments/assets/4504983c-a71d-4d1c-9b8f-935098160365" />

### 2. Installed Required Tools
- Installed **Docker** for containerization.  
- Installed **Jenkins** for CI/CD automation.  
- Verified Jenkins is accessible via `http://<EC2-IP>:8080`.

### 3. Configured Jenkins
- Installed necessary Jenkins plugins:
  - **Git Plugin**
  - **Docker Pipeline Plugin**
- Allocated a Jenkins admin password and unlocked Jenkins.  
- Created a **new Jenkins pipeline project**.  

### 4. Wrote and Pushed Python Application
- Created a simple Python application (Flask-based).  
- Added supporting files:
  - `Dockerfile`
  - `requirements.txt`
  - `Jenkinsfile`
- Pushed the project to **GitHub repository**.  

### 5. Integrated GitHub with Jenkins
- Added the **GitHub repo URL** in Jenkins pipeline configuration.  
- Set Jenkins to automatically pull the latest code during builds.  

### 6. Configured DockerHub Credentials
- Stored DockerHub **username & password** in Jenkins credentials manager.  
- Updated the pipeline to:
  1. Build the Docker image from the Python app.  
  2. Tag the image.  
  3. Push the image to DockerHub.  

### 7. Ran the Jenkins Pipeline
- Triggered the Jenkins build.  
- Verified steps:
  - ✅ Code cloned from GitHub  
  - ✅ Docker image built  
  - ✅ Image pushed to DockerHub repository  

---

## 🎯 What We Achieved
- **Automation:** No manual Docker build and push. Jenkins automates the process whenever code is updated.  
- **Consistency:** The same Docker image can be pulled and run on any environment (EC2, local, Kubernetes).  
- **CI/CD Practice:** Demonstrates how DevOps pipeline integrates Git, Jenkins, Docker, and AWS.  
- **Scalability Ready:** The application can now be extended to Kubernetes or ECS for production-level deployment.  

---

## 📂 Tech Stack Used
- **AWS EC2** – Server to host Jenkins & Docker  
- **Jenkins** – CI/CD pipeline automation  
- **Docker** – Containerization  
- **GitHub** – Source code management  
- **DockerHub** – Container image registry  

---

## ✅ Final Outcome
A Python application successfully:  
1. **Pushed to GitHub**  
2. **Built & containerized via Jenkins**  
3. **Pushed to DockerHub automatically**  
4. Ready to be **deployed anywhere** by pulling the image

---
## python application written in the project
just Wrote a python application which is just a simple notes webpage using flask.


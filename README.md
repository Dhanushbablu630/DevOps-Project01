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
- <img width="1323" height="783" alt="Image" src="https://github.com/user-attachments/assets/9a7990ae-1143-452b-a1d8-d2d88aa0bb8c" />

### 3. Configured Jenkins
- Installed necessary Jenkins plugins:
  - **Git Plugin**
  - **Docker Pipeline Plugin**
- Allocated a Jenkins admin password and unlocked Jenkins.  
- Created a **new Jenkins pipeline project**.
- <img width="1798" height="787" alt="Image" src="https://github.com/user-attachments/assets/9898b335-b8db-4cd0-9255-c1740e3d8e8e" />


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
- <img width="1818" height="764" alt="Image" src="https://github.com/user-attachments/assets/3beb188f-a808-49c7-88ad-023912b6fbc4" />  

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
  - <img width="1846" height="687" alt="Image" src="https://github.com/user-attachments/assets/acc1c3d9-8027-4247-85b5-680f7e3c44dd" /> 

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
5. <img width="1441" height="510" alt="Image" src="https://github.com/user-attachments/assets/1d7d2787-df7d-453d-84ba-208dda8c68ea" />

---
## python application written in the project
just Wrote a python application which is just a simple notes webpage using flask.
<img width="1755" height="708" alt="Image" src="https://github.com/user-attachments/assets/2ce86e07-13dc-4a91-9382-416a46208669" />

---
# Small Clip of the Project
https://github.com/user-attachments/assets/3ed814a1-ae5d-4f0f-b5b3-fb383cf6dc2a

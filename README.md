# Cloud-storage-project
Cloud-Based File Storage and Sharing System using AWS
Overview

This project is a cloud-based file storage and sharing system deployed using AWS, Flask, S3, CloudWatch, and Docker.
Users can upload files, store them securely on the cloud, and access/manage them through a simple web interface.
This project was created as part of Cloud Internship – Project 1.

Features:
Upload files through a simple web interface
Store files securely in Amazon S3
Generate file URLs for access/sharing
Deployment using AWS EC2
Containerization using Docker
Basic monitoring using CloudWatch Dashboard
Follows proper cloud architecture principles

Technologies Used:
Frontend
HTML
CSS
JavaScript
Backend
Python Flask
Cloud
Amazon EC2 (Deployment)
Amazon S3 (Storage)
CloudWatch (Monitoring)
Deployment
Docker
AWS EC2

 Project Structure:
cloud-storage-project/
│
├── app.py
├── requirements.txt
├── Dockerfile
├── templates/
├── static/
│
├── Cloud_Project_Report.pdf
├── Cloud_Project_Presentation_Final.pptx
└── screenshots/

How to Run the Project Locally:
. Install dependencies
pip install -r requirements.txt
.Run Flask app
python app.py
.Open in browser
http://localhost:5000
Run Using Docker
Build the Docker image
docker build -t cloudflaskapp .
Run the container
docker run -p 5000:5000 cloudflaskapp
Visit the app at:
http://localhost:5000

AWS Services used:
Amazon EC2
Hosted Flask app
Docker running on EC2 instance
Amazon S3
Stores uploaded files
Public/private access control
CloudWatch
Dashboard created with CPUUtilization graph
Basic EC2 instance monitoring

Screenshots:
EC2 Instance List
EC2 Instance Details
CloudWatch Dashboard
S3 Bucket
App Running
Docker Build Output
Docker Container Status
Live URL:

EC2 instance is currently stopped to avoid charges.

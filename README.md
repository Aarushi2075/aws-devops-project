# 🚀 AWS DevOps Project - Flask Application Deployment

> A production-inspired DevOps project demonstrating automated deployment of a Flask web application on AWS EC2 using GitHub Actions, Amazon S3, Gunicorn, and Nginx.

![AWS](https://img.shields.io/badge/AWS-Free%20Tier-orange)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Web%20Application-green)
![GitHub Actions](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)
![Ubuntu](https://img.shields.io/badge/Ubuntu-22.04-E95420)

---

# 📌 Project Overview

This project was developed as part of a **DevOps Engineer Technical Assignment** to demonstrate practical cloud deployment, automation, and security using AWS Free Tier services.

The application is hosted on an **Amazon EC2 Ubuntu instance** and deployed automatically through a **GitHub Actions CI/CD pipeline**. Every code push to the `main` branch triggers an automated deployment process that backs up the application to Amazon S3 before updating the EC2 instance.

The project focuses on implementing real-world DevOps practices including secure credential management, automated deployments, reverse proxy configuration, and cloud infrastructure setup.

---

# 🏗️ Architecture

```text
                    Developer
                        │
                  Push to GitHub
                        │
                        ▼
              GitHub Actions Pipeline
              │                    │
              ▼                    ▼
      Amazon S3 Backup      Amazon EC2 (Ubuntu)
                                   │
                            Git Pull Latest Code
                                   │
                        Install Dependencies
                                   │
                      Restart Gunicorn Service
                                   │
                              Gunicorn
                                   │
                                 Nginx
                                   │
                                   ▼
                           Flask Web Application
```

---

# ⚙️ Technologies Used

| Category | Technology |
|-----------|------------|
| Cloud Platform | AWS Free Tier |
| Compute | Amazon EC2 |
| Storage | Amazon S3 |
| IAM | AWS IAM |
| Programming Language | Python |
| Framework | Flask |
| Web Server | Gunicorn |
| Reverse Proxy | Nginx |
| CI/CD | GitHub Actions |
| Version Control | Git |

---

# 📂 Repository Structure

```
aws-devops-project/
│
├── .github/
│   └── workflows/
│       └── deploy.yml
│
├── app/
│   ├── app.py
│   ├── tasks.json
│   └── templates/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Features

- Flask web application hosted on AWS EC2
- Automated deployment using GitHub Actions
- Amazon S3 backup integration
- Gunicorn application server
- Nginx reverse proxy
- Secure IAM authentication
- GitHub Secrets for sensitive credentials
- Automatic Gunicorn restart after deployment
- Automatic Gunicorn startup after EC2 reboot

---

# ☁️ AWS Infrastructure

The project uses the following AWS services:

### Amazon EC2
- Ubuntu Server
- Hosts the Flask application
- Runs Gunicorn and Nginx

### Amazon S3
- Stores application backups during deployment
- Maintains project files uploaded by GitHub Actions

### AWS IAM
An IAM User was created instead of using the AWS Root account.

Permissions were configured to allow:

- Amazon S3 access
- Programmatic access using Access Keys
- Secure authentication from GitHub Actions

---

# 🔐 Security

The following security practices were implemented:

- IAM User instead of Root Account
- SSH Key Authentication
- GitHub Secrets for credentials
- Restricted Security Group rules
- Least Privilege Access
- Secure AWS Access Keys

GitHub Secrets used:

```
AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY
AWS_REGION
S3_BUCKET
EC2_HOST
EC2_USER
EC2_SSH_KEY
```

---

# 🔄 CI/CD Pipeline

The deployment workflow is fully automated using GitHub Actions.

Whenever code is pushed to the **main** branch:

1. Repository is checked out.
2. AWS credentials are configured.
3. Application files are uploaded to Amazon S3.
4. SSH connection is established with EC2.
5. Latest code is pulled.
6. Dependencies are installed.
7. Gunicorn service is restarted.
8. Updated application becomes available.

Deployment Flow:

```
Git Push
    │
    ▼
GitHub Actions
    │
Checkout Repository
    │
AWS Authentication
    │
Upload Backup to S3
    │
SSH into EC2
    │
Git Pull
    │
Install Requirements
    │
Restart Gunicorn
    │
Deployment Complete
```

---

# 🌐 Application Deployment

The Flask application is served using **Gunicorn** while **Nginx** acts as a reverse proxy.

```
Browser
    │
    ▼
Nginx
    │
    ▼
Gunicorn
    │
    ▼
Flask Application
```

Gunicorn is managed using **systemd**, ensuring:

- Automatic startup after EC2 reboot
- Easy service management
- Automatic restart during deployments

---

# 📋 Challenges Encountered

Throughout development, several issues were encountered and resolved:

- SSH authentication failures
- Security Group configuration issues
- IAM Access Key configuration
- GitHub Secrets setup
- Amazon S3 permission configuration
- GitHub Actions YAML syntax errors
- Incorrect application upload path (`app/app.py`)
- Deployment workflow debugging

These issues were resolved through iterative testing and GitHub Actions log analysis.

---

# 📈 Future Improvements

The following enhancements are planned:

- Amazon CloudWatch Monitoring
- HTTPS using SSL Certificates
- Load Testing (k6 / JMeter)
- Docker Containerization
- Auto Scaling
- Load Balancer Integration

---

# 📚 Learning Outcomes

Through this project, I gained practical experience with:

- AWS Infrastructure Deployment
- Linux Server Administration
- CI/CD Automation
- GitHub Actions
- IAM & Security
- Gunicorn
- Nginx
- Amazon S3
- Deployment Debugging
- DevOps Best Practices

---

# 👤 Author

**Aarushi Sharma**

B.Tech CSE (Cloud Computing)

AWS DevOps Internship Assignment

---
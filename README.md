# AWS-assignment
# task 1
# Application
# User Management System using Python and Mysql
# Tech Stack
Backend: Python Flask
Frontend: HTML, CSS
Database: MySQL
Environment: Python 3 + Virtual Environment
# 1 create a folder
mkdir python-app
# 2 Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate
# 3 Install dependencies
pip install -r requirements.txt
# 4 Run the flask app
python app.py
# 5 hit you ip on brower on port 5000
<img width="1920" height="1008" alt="Screenshot 2026-02-08 164022" src="https://github.com/user-attachments/assets/f0e2b4e0-f4b4-4c7c-9e16-da0b2043c783" />

<img width="1920" height="1008" alt="Screenshot 2026-02-08 164028" src="https://github.com/user-attachments/assets/d6636131-7f08-4f7d-8f97-5f09e81f7a62" />
# output
<img width="1920" height="1008" alt="Screenshot 2026-02-08 164028" src="https://github.com/user-attachments/assets/fe690358-94dc-4196-a059-ae050bb61bd4" />


# task 2 Docker
# Docker Nginx Project 

This project demonstrates how to create a custom Nginx Docker image using a Dockerfile.

## Dockerfile Used
- Base Image: nginx
- Exposed Port: 80
- Custom HTML Pages:
  - index.html
  - home.html
## Build Command
docker build -t mynginx .
## Run Command
docker run -d -p 8080:80 --name mycont1 mynginx
## Access in Browser
http://localhost:8080

## For Restart  
docker update --restart unless-stopped mycont1
## What this does
1.It sets the container to:
2.Restart automatically if it crashes
3.Restart after Docker service restarts
4.Restart after system reboot
5.BUT if you manually stop it → it will stay stopped

<img width="1920" height="1008" alt="Screenshot 2026-02-07 225004" src="https://github.com/user-attachments/assets/5f052221-6d4f-4103-a551-f5b4b5c15c74" />
<img width="1920" height="1008" alt="Screenshot 2026-02-07 225106" src="https://github.com/user-attachments/assets/0b921686-6c3f-4651-b697-4a619df6e1af" />
## output
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/821d0134-abcb-4903-a7ab-0566c6a9abb0" />
# home.html
<img width="1920" height="1008" alt="Screenshot 2026-02-07 225221" src="https://github.com/user-attachments/assets/226b904e-a982-4ae3-b1f9-2ccc04d92e79" />

## Task 3 AWS ec2 deployment
# Launch ec2 (t3.micro)

<img width="1920" height="1008" alt="Screenshot 2026-02-08 175814" src="https://github.com/user-attachments/assets/fc7bf2c1-fdb2-48f3-870f-8f80b66046f5" />
# install Docker on Ubuntu (EC2 / Linux)
1. Update system
sudo apt update
2. Install Docker
sudo apt install docker.io -y
3. Start Docker
sudo systemctl start docker

<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/ad0f53df-a909-4b3c-a29a-ac9b07d1a860" />
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/0eb26fd0-10f4-4826-bc7d-e1910d2a160b" />
<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/78e7e3d8-5ef2-4f40-b904-aad5572eb8f1" />
# Output

<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/a4adc431-feff-4211-8239-b9f6fb1ea37f" />

## Task Applicattion Access
# Create a Elastic Ip

![WhatsApp Image 2026-02-08 at 2 18 26 PM](https://github.com/user-attachments/assets/0f8ecda2-a162-4c22-aab1-3c99539cc6c3)

# Associate it 

![WhatsApp Image 2026-02-08 at 2 19 04 PM](https://github.com/user-attachments/assets/1925c3ca-1034-4620-9404-bfb2f8d8d54b)

# Then you can see your ip is attach to your server ip

![WhatsApp Image 2026-02-08 at 2 19 32 PM](https://github.com/user-attachments/assets/ca9aa459-f078-4ac1-8408-1097b04603ac)

# 1st output with public ip

![WhatsApp Image 2026-02-08 at 2 21 37 PM](https://github.com/user-attachments/assets/c5f97fdb-24aa-41cb-b8a1-9d536d94134a)

# 2nd output with elastic ip

![WhatsApp Image 2026-02-08 at 2 22 20 PM](https://github.com/user-attachments/assets/99eb6116-dead-42db-b2a0-4486117f9b70)

# task 5 Load Balancer and Auto Scalling 
I successfully configured an AWS Load Balancer to manage traffic across 6 server instances.
●Load Balancer Setup with 3 Facebook Servers & 3 Instagram Servers
●Traffic routing was set so that:
Facebook requests → Facebook server group
Instagram requests → Instagram server group
●Traffic routing was configured so that Facebook requests went to Facebook servers and Instagram requests went to Instagram servers.
# Step 1: Make 3 servers for Facebook and 3 servers for Instagram
# Step 2: Created 2 Target Groups (Facebook & Instagram).
 Added 3 servers to each Target Group for load distribution
# Step 3: Then created the AWS Load Balancer for the traffic and add two target 
 group which is for facebook and instagram
 Configured Listener on Port 80 (HTTP) to route traffic
# Step 4: Run the Load Balancer DNS in the browser to test successful routing

<img width="800" height="420" alt="image" src="https://github.com/user-attachments/assets/962d05db-a010-4d15-bc41-a03b0176760c" />

<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/cf8004e3-5f3f-48a9-8515-6cab393a3ac7" />

<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/db0c8150-32fe-4cca-92d8-70d16492435d" />

<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/58e8b7ff-266f-40f1-8b66-ccdc62edf303" />

<img width="1920" height="1008" alt="image" src="https://github.com/user-attachments/assets/b1d130b3-cec8-4b5b-a322-ac46f18211f3" />



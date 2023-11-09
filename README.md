# Flask Monitoring App Deployment on AWS EKS

This project involves creating a monitoring app using Flask, containerizing it with Docker, and deploying it on AWS EKS using AWS ECR for container registry, kubectl for Kubernetes orchestration, and Python for automation.
Thanks to [N4si](https://github.com/N4si) for this project step by step walkthrough.

## Prerequisites

Before getting started, ensure you have the following installed:

- Python
- Docker
- kubectl
- AWS CLI
- AWS EKS cluster configured
- AWS ECR repository

## Setup

1. Clone the Repository:

   ```bash
   git clone https://github.com/ARTSZL/flask-monitoring-app.git
   cd flask-monitoring-app

2. Install dependencies:

   ```bash
   pip3 install -r requirements.txt 

3. Build Docker image:

   ```bash
   docker build -t my-flask-app

4. Run Docker container:

   ```bash
   docker run -p 5000:5000 mt-flask-app

5. Create an ECR repository by running:

   ```bash
   python3 ecr.py

6. Retrieve an authentication token and authenticate your Docker client to your registry:

   ```bash
   aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com

7. Tag and Push to AWS ECR:

   ```bash
   docker tag my_monitoring_app_image:latest <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my_monitoring_app_image:latest
   docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/my_monitoring_app_image:latest

8. Create an EKS cluster and add node group.

9. Create a node group in the EKS cluster.

10. Run eks.py file:

   ```bash
   python3 eks.py
   ```

11. Check if pod is up and running:

   Check deployments
   ```
   kubectl get deployment -n default
   ```
   Check service
   ```
   kubectl get service -n default
   ```
   To check the pods
   ```
   kubectl get pods -n default
   ```
   
10. Run the port-forward to expose the service:

   ```bash
   kubectl port-forward service/<service_name> 5000:5000
   ```

## Usage

Visit the deployed monitoring app at http://your-eks-cluster-ip:app-port.

## Customization

Adjust the Flask app code in the app/ directory to meet your monitoring requirements.
Modify Kubernetes configurations in the eks.py file for specific deployment needs.

## License

This project is licensed under the MIT [License](https://github.com/ARTSZL/flask-monitoring-app/blob/main/LICENSE).

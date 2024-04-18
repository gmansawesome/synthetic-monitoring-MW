# Developing a Synthetic Monitoring Platform
This project develops an extendable synthetic monitoring platform using the Ping Parsing library in Python to collect data from a website. Prometheus is used to store these metrics, and Grafana is used to present them on a real-time dashboard.

## What does it do?
A synthetic monitoring platform provides insights into network connectivity, latency, and packet loss. This enables proactive monitoring, troubleshooting, etc of network infrastructure and services, such as a website.


## Setup
An IDE that works with Python is needed. This project was built in VS Code using Python 3.12.2.

You will need to install the Ping Parsing library, Prometheus, and Grafana, as well as make a Grafana account.

#### Ping Parsing Install:

paste the following command into your terminal
```
pip install pingparsing
```

#### Prometheus Install:

<a href="https://prometheus.io/download/" target="_blank">Prometheus</a> Select the latest release for your OS 

Follow setup instructions and test if working by running "prometheus.exe" and going to http://localhost:9090/

#### Grafana Install:

<a href="https://grafana.com/docs/grafana/latest/setup-grafana/installation/" target="_blank">Grafana</a> Select the latest release for your OS

Once installed test if working by going to http://localhost:3000/

## Usage
The platform consists of 3 key components: the ping monitor, Prometheus, and Grafana. These components communicate and share data through localhost instances. By default, ping monitor sends data into

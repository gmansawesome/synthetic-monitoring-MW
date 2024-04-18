# Developing a Synthetic Monitoring Platform
This project develops an extendable synthetic monitoring platform using the Ping Parsing library in Python to collect data from a website. Prometheus is used to store these metrics, and Grafana is used to present them on a real-time dashboard.

## What does it do?
A synthetic monitoring platform provides insights into network connectivity, latency, and packet loss. This enables proactive monitoring, troubleshooting, etc of network infrastructure and services. In it's basic form this platform monitors a website.


## Setup
An IDE that works with Python is needed. This project was built in VS Code using Python 3.12.2.

You will need to install the Ping Parsing library, Prometheus, and Grafana.

#### Ping Parsing Install:

paste the following command into your terminal
```
pip install pingparsing
```

#### Prometheus Install:

[Prometheus Install](https://prometheus.io/download/) Select the latest release for your OS 


#### Grafana Install:

[Grafana Install](https://grafana.com/docs/grafana/latest/setup-grafana/installation/) Select the latest release for your OS
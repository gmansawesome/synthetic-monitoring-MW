# Developing a Synthetic Monitoring Platform
This project develops an extendable synthetic monitoring platform using the Ping Parsing library in Python to collect data from a website. Prometheus is used to store these metrics, and Grafana is used to present them on a real-time dashboard.

## What does it do?
A synthetic monitoring platform provides insights into network connectivity, latency, and packet loss. This enables proactive monitoring, troubleshooting, etc of network infrastructure and services, such as a website.


## Setup
An IDE that works with Python is needed. This project was built in VS Code using Python 3.12.2.

You will need to install the Ping Parsing library, Prometheus, and Grafana.

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
The platform consists of 3 key components: the ping monitor, Prometheus, and Grafana. These components communicate and share data through localhost instances. By default, ping monitor sends data into localhost:8000, prometheus at localhost:9090, and Grafana at localhost:3000.

First, adjust the settings of the ping monitor, navigate to config.yml in the monitor folder. There, you can configure the target website ("website"),  the number of packets ("duration"), localhost port ("port"), and sleep duration between pings ("sleep"). Also add your port to the target list of "prometheus.yml".

Once desired settings are configured, run "main.py" and "prometheus.exe". Navigate to the localhost for prometheus and select Status -> Targets to confirm it's reading from your ping monitor localhost.

Finally, you can go to the Grafana localhost and sign in with Username: Admin, Password: Admin. Add prometheus as a data source, and create a new dashboard to begin visualizing using your data.

## System Diagram
![system diagram](https://github.com/gmansawesome/synthetic-monitoring-MW/assets/45411978/b3d342cd-a04e-49fe-a439-926ffe316ab0)

import json
import pingparsing
from prometheus_client import start_http_server, Gauge

# TO DO: implement reading from config.yml...
# TO DO: setup basic working gauge

ping_latency_avg = Gauge('ping_latency_avg_ms', 'Average round-trip time (RTT) in milliseconds')
ping_packet_loss_rate = Gauge('ping_packet_loss_rate', 'Ping packet loss rate')

ping_parser = pingparsing.PingParsing()
transmitter = pingparsing.PingTransmitter()
transmitter.destination = "google.com"
transmitter.count = 10
result = transmitter.ping()

parsed_data = ping_parser.parse(result).as_dict()

ping_latency_avg.set(4.2).labels("/fooBar")
ping_packet_loss_rate.set(4.2).labels("/fooBar")

start_http_server(8000)

print(json.dumps(parsed_data, indent=4))
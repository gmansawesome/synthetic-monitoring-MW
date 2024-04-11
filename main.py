import json
import pingparsing
from prometheus_client import start_http_server, Gauge
import yaml
import time

def read_config(config_path): 
    try:
        with open(config_path, 'r') as file:
            config_data = yaml.safe_load(file)
        return config_data

    except FileNotFoundError:
        print("File not found!")

    except yaml.YAMLError as error:
        print("Error occured!")
        print(error)

# initialize metrics
packet_transmit = Gauge('packet_transmit', "Packets Trasmitted") 
packet_receive = Gauge('packet_receive', "Packets Recieved")
packet_loss_count = Gauge("packet_loss_count", "Packets Loss Count")
packet_loss_rate = Gauge("packet_loss_rate", "Packet Loss Rate")
def get_metrics(parsed_results):
    # assign metric values
    packet_transmit.set(parsed_results["packet_transmit"])
    packet_receive.set(parsed_results["packet_receive"])
    packet_loss_count.set(parsed_results["packet_loss_count"])
    packet_loss_rate.set(parsed_results["packet_loss_rate"])


def main():
    # read data from config file
    config_data = read_config("config.yml")

    # syntactic sugar for config variables
    website = config_data["monitor_configs"]["website"]
    duration = config_data["monitor_configs"]["duration"]
    port = config_data["monitor_configs"]["port"]

    # starting up local server
    start_http_server(port)
    print(f"Local HTTP server started on port {port}")

    # setting up ping entity
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = website
    transmitter.count = duration

    # running ping and parsing result
    result = transmitter.ping()
    parsed_result = ping_parser.parse(result).as_dict()

    # outputting parsed data
    print(json.dumps(parsed_result, indent=4))

    while True:
        get_metrics(parsed_result)

main()
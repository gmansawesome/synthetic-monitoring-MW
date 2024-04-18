import json
import pingparsing
from prometheus_client import start_http_server, Gauge
import yaml
import time

# yaml file reader
def read_config(config_path): 
    try:
        with open(config_path, 'r') as file:
            config_data = yaml.safe_load(file)
        return config_data

    except FileNotFoundError:
        print("File not found!")

    except yaml.YAMLError as error:
        print(error)

# initialize metrics
packet_transmit = Gauge('packet_transmit', "Packets Trasmitted") 
packet_receive = Gauge('packet_receive', "Packets Recieved")
packet_loss_count = Gauge("packet_loss_count", "Packets Loss Count")
packet_loss_rate = Gauge("packet_loss_rate", "Packet Loss Rate")
packet_duplicate_count = Gauge("packet_duplicate_count", "Packet Duplicate Count")
packet_duplicate_rate = Gauge("packet_duplicate_rate", "Packet Duplicate Rate")
rtt_min = Gauge('rtt_min', "Round trip time min")
rtt_avg = Gauge('rtt_avg', "Round trip time avg")
rtt_max = Gauge('rtt_max', "Round trip time max")

# assigns metrics from parsed results into prometheus metrics objects
def assign_metrics(parsed_results):
    # assign metric values while ensuring they exist
    if parsed_results["packet_transmit"] is not None:
        packet_transmit.set(parsed_results["packet_transmit"])
    if parsed_results["packet_receive"] is not None:
        packet_receive.set(parsed_results["packet_receive"])
    if parsed_results["packet_loss_count"] is not None:
        packet_loss_count.set(parsed_results["packet_loss_count"])
    if parsed_results["packet_loss_rate"] is not None:
        packet_loss_rate.set(parsed_results["packet_loss_rate"])
    if parsed_results["rtt_min"] is not None:
        rtt_min.set(parsed_results["rtt_min"])
    if parsed_results["rtt_avg"] is not None:
        rtt_avg.set(parsed_results["rtt_avg"])
    if parsed_results["rtt_max"] is not None:
        rtt_max.set(parsed_results["rtt_max"])
    if parsed_results["packet_duplicate_count"] is not None:
        packet_duplicate_count.set(parsed_results["packet_duplicate_count"])
    if parsed_results["packet_duplicate_rate"] is not None:
        packet_duplicate_rate.set(parsed_results["packet_duplicate_rate"])

def main():
    # read data from config file
    config_data = read_config("config.yml")

    # syntactic sugar for config variables
    website = config_data["monitor_configs"]["website"]
    duration = config_data["monitor_configs"]["duration"]
    port = config_data["monitor_configs"]["port"]
    sleep = config_data["monitor_configs"]["sleep"]

    # starting up local server
    start_http_server(port)
    print(f"Local HTTP server started on port {port}")

    # setting up ping entity
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = website
    transmitter.count = duration

    while True:
        # running ping and parsing result
        result = transmitter.ping()
        parsed_result = ping_parser.parse(result).as_dict()

        # outputting parsed data
        print(json.dumps(parsed_result, indent=4))

        assign_metrics(parsed_result)
        time.sleep(sleep)

main()
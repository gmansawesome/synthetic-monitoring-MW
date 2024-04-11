import json
import pingparsing
from prometheus_client import start_http_server, Gauge
import yaml

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

main()
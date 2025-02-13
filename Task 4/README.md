markdown
# Network Packet Analyzer

This project is an ethical network packet analyzer written in Python using the Scapy library. It captures and analyzes network packets for educational purposes.

## Features
- Captures network packets from a specified interface.
- Analyzes packets and extracts relevant information (protocol, IP addresses, ports, etc.).
- Displays a summary of the captured packets.
- Provides troubleshooting steps for common issues.

## Requirements
- Python 3.x
- Scapy library: `pip install --upgrade scapy`

## Usage
Run the script from the command line, specifying the interface, number of packets to capture, and any filter criteria using BPF (Berkeley Packet Filter) syntax.

``bash
python packet_analyzer.py -i <interface> -c <number_of_packets> -f '<BPF_filter>'
<interface>: The network interface you want to capture packets from (e.g., eth0, wlan0).

<number_of_packets>: The number of packets you want to capture.

<BPF_filter>: Your filter criteria using BPF syntax (e.g., tcp, port 80, host 192.168.1.1).

For example, if you want to capture 100 TCP packets on interface eth0 that are going to or from port 80, you would run:

bash
sudo python packet_analyzer.py -i eth0 -c 100 -f 'tcp port 80'
Code Overview
PacketAnalyzer Class
The PacketAnalyzer class is responsible for analyzing and displaying packet information.

analyze_packet(packet): Analyzes individual packets and extracts relevant information.

display_packet_info(packet_info): Displays packet information in a formatted way.

start_capture(interface=None, packet_count=None, filter_str=None): Starts capturing packets with given parameters.

show_summary(): Displays a summary of the captured packets.

## Main Script
The main script parses command-line arguments and starts the packet capture.

python
if __name__ == "__main__":
    main()

## Troubleshooting
Make sure you have required permissions.
Try running without specifying an interface.
Check if your filter syntax is correct.
Ensure you have Scapy installed correctly: pip install --upgrade scapy.

Disclaimer

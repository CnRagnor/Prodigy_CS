# Network Packet Analyzer

A Python-based ethical network packet analyzer using Scapy library for educational packet capture and analysis.

## Overview

This project provides a simple yet powerful network packet analyzer that captures and analyzes network traffic for educational purposes. Built with Python and Scapy, it offers detailed packet inspection while maintaining ease of use.

## Features

- Real-time packet capture from specified network interfaces
- Detailed packet analysis with protocol information
- Extraction of key data (IP addresses, ports, protocols)
- Customizable packet filtering using BPF syntax
- Comprehensive packet summary display
- User-friendly command-line interface

## Requirements

- Python 3.x
- Scapy library

### Installation

```bash
pip install --upgrade scapy
```

## Usage

Run the analyzer using the following command structure:

```bash
python packet_analyzer.py -i <interface> -c <number_of_packets> -f '<BPF_filter>'
```

Where:
- `<interface>`: Network interface to capture from (e.g., eth0, wlan0)
- `<number_of_packets>`: Number of packets to capture
- `<BPF_filter>`: Filter criteria using BPF syntax

### Example

To capture 100 TCP packets on interface eth0 targeting port 80:

```bash
sudo python packet_analyzer.py -i eth0 -c 100 -f 'tcp port 80'
```

## Code Structure

### PacketAnalyzer Class

The core functionality is implemented in the PacketAnalyzer class:

- `analyze_packet(packet)`: Processes individual packets
- `display_packet_info(packet_info)`: Formats and shows packet data
- `start_capture(interface, packet_count, filter_str)`: Initiates packet capture
- `show_summary()`: Provides capture session summary

### Main Script

```python
if __name__ == "__main__":
    main()
```

## Troubleshooting Guide

1. Permission Issues
   - Run with sudo/administrator privileges
   - Check interface access rights

2. Interface Problems
   - Try without specifying interface
   - Verify interface name
   - Ensure interface is active

3. Filter Issues
   - Verify BPF syntax
   - Remove filter to test basic functionality

4. Installation Problems
   - Reinstall Scapy: `pip install --upgrade scapy`
   - Check Python version compatibility

## Disclaimer

This tool is intended for educational purposes only. Users are responsible for complying with applicable laws and regulations regarding network monitoring and packet capture. Always obtain proper authorization before capturing network traffic.

## License

[MIT License]

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

from scapy.all import sniff, IP, TCP, UDP, conf
import time
from datetime import datetime
import argparse
import sys

class PacketAnalyzer:
    def __init__(self):
        self.packet_count = 0
        self.start_time = None
        
    def analyze_packet(self, packet):
        """Analyze individual packets and extract relevant information."""
        self.packet_count += 1
        
        if not self.start_time:
            self.start_time = time.time()
            
        # Initialize packet info dictionary
        packet_info = {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'protocol': 'Unknown',
            'src_ip': 'Unknown',
            'dst_ip': 'Unknown',
            'src_port': 'Unknown',
            'dst_port': 'Unknown',
            'length': len(packet),
            'payload': 'No payload'
        }
        
        # Extract IP layer information if present
        if IP in packet:
            packet_info['src_ip'] = packet[IP].src
            packet_info['dst_ip'] = packet[IP].dst
            
            # Determine protocol and port information
            if TCP in packet:
                packet_info['protocol'] = 'TCP'
                packet_info['src_port'] = packet[TCP].sport
                packet_info['dst_port'] = packet[TCP].dport
                if packet[TCP].payload:
                    packet_info['payload'] = str(packet[TCP].payload)[:50] + '...'
            elif UDP in packet:
                packet_info['protocol'] = 'UDP'
                packet_info['src_port'] = packet[UDP].sport
                packet_info['dst_port'] = packet[UDP].dport
                if packet[UDP].payload:
                    packet_info['payload'] = str(packet[UDP].payload)[:50] + '...'
        
        self.display_packet_info(packet_info)
        
    def display_packet_info(self, packet_info):
        """Display packet information in a formatted way."""
        print("\n" + "="*80)
        print(f"Packet #{self.packet_count} - {packet_info['timestamp']}")
        print(f"Protocol: {packet_info['protocol']}")
        print(f"Source IP: {packet_info['src_ip']} : {packet_info['src_port']}")
        print(f"Destination IP: {packet_info['dst_ip']} : {packet_info['dst_port']}")
        print(f"Packet Length: {packet_info['length']} bytes")
        print(f"Payload Preview: {packet_info['payload']}")
        print("="*80)
        
    def start_capture(self, interface=None, packet_count=None, filter_str=None):
        """Start capturing packets with given parameters."""
        print("\nEthical Network Packet Analyzer")
        print("For Educational Purposes Only")
        print("\nStarting packet capture...")
        print(f"Interface: {interface if interface else 'default'}")
        print(f"Filter: {filter_str if filter_str else 'none'}")
        
        try:
            # Use L3 socket for capture
            if sys.platform.startswith('win'):
                conf.use_pcap = False
                conf.use_dnet = False
                conf.L3socket = conf.L3socket
            
            sniff(
                iface=interface,
                prn=self.analyze_packet,
                count=packet_count,
                filter=filter_str,
                store=0  # Don't store packets in memory
            )
        except KeyboardInterrupt:
            self.show_summary()
        except PermissionError:
            print("\nError: This program requires administrator/root privileges.")
            print("Please run the script with elevated privileges:")
            print("Windows: Run Command Prompt as Administrator")
            print("Linux/Mac: Use 'sudo python script.py'")
        except Exception as e:
            print(f"\nError during packet capture: {str(e)}")
            print("\nTroubleshooting steps:")
            print("1. Make sure you have required permissions")
            print("2. Try running without specifying an interface")
            print("3. Check if your filter syntax is correct")
            print("4. Ensure you have scapy installed correctly: pip install --upgrade scapy")
            
    def show_summary(self):
        """Display capture session summary."""
        duration = time.time() - self.start_time if self.start_time else 0
        print("\nCapture Summary:")
        print(f"Total Packets Captured: {self.packet_count}")
        print(f"Duration: {duration:.2f} seconds")
        print(f"Packets per second: {self.packet_count/duration:.2f}" if duration > 0 else "N/A")

def main():
    parser = argparse.ArgumentParser(description='Network Packet Analyzer for Educational Purposes')
    parser.add_argument('-i', '--interface', help='Network interface to capture packets from')
    parser.add_argument('-c', '--count', type=int, help='Number of packets to capture')
    parser.add_argument('-f', '--filter', help='BPF filter string (e.g., "tcp port 80")')
    
    args = parser.parse_args()
    
    analyzer = PacketAnalyzer()
    analyzer.start_capture(
        interface=args.interface,
        packet_count=args.count,
        filter_str=args.filter
    )

if __name__ == "__main__":
    main()

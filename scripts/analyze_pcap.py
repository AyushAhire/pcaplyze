import pyshark
import pandas as pd
import matplotlib.pyplot as plt

def parse_pcap(pcap_file):
    cap = pyshark.FileCapture(pcap_file)
    packets = []

    for packet in cap:
        try:
            packet_info = {
                "number": packet.number,
                "timestamp": packet.sniff_time,
                "src_ip": packet.ip.src,
                "dst_ip": packet.ip.dst,
                "protocol": packet.transport_layer,
                "src_port": packet[packet.transport_layer].srcport,
                "dst_port": packet[packet.transport_layer].dstport,
                "seq": packet.tcp.seq,
                "length": int(packet.length)
            }
            packets.append(packet_info)
        except AttributeError:
            # Packet does not have the expected attributes
            continue

    return packets

def main():
    pcap_file_path = '../logs/sample_capture.pcap'
    packets = parse_pcap(pcap_file_path)

    # Convert packet data to DataFrame
    df = pd.DataFrame(packets)
    df.to_csv('../data/processed_pcap.csv', index=False)

    # Basic Analysis
    print("Top 5 Source IPs:")
    print(df['src_ip'].value_counts().head())

    print("Top 5 Destination IPs:")
    print(df['dst_ip'].value_counts().head())

    print("Packet Count by Protocol:")
    print(df['protocol'].value_counts())

    # Plot packet length distribution
    plt.figure(figsize=(10, 6))
    plt.hist(df['length'], bins=50, alpha=0.7)
    plt.title('Packet Length Distribution')
    plt.xlabel('Length')
    plt.ylabel('Frequency')
    plt.show()

if __name__ == "__main__":
    main()


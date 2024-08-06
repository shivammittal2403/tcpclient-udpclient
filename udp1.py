import socket
import argparse
import sys

def udp_client(target_host, target_port, message):
    try:
        # Create a socket object
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Send some data
        client.sendto(message.encode(), (target_host, target_port))

        # Receive some data
        data, addr = client.recvfrom(4096)
        print(f"Received from {addr}: {data.decode()}")

    except KeyboardInterrupt:
        print("\n[INFO] User requested to stop. Closing the client.")
    finally:
        client.close()

if __name__ == "__main__":
    # Command-line argument parsing
    parser = argparse.ArgumentParser(description="Simple UDP client to send and receive messages.")
    parser.add_argument("host", help="Target host IP address or domain.")
    parser.add_argument("port", type=int, help="Target port number.")
    parser.add_argument("-m", "--message", default="AAABBBCCC", help="Message to send to the server.")
    
    args = parser.parse_args()

    udp_client(args.host, args.port, args.message)

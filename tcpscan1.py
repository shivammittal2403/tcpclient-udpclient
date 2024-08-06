import socket

# Define the target host and port
target_host = "www.google.com"
target_port = 80

# Create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect the client
    client.connect((target_host, target_port))
    print(f"Connected to {target_host} on port {target_port}")

    # Monitor the connection until Ctrl+C is pressed
    while True:
        # Send some data
        client.send(b"GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n")

        # Receive the response
        response = client.recv(4096)

        # Print the response
        print(response.decode())

except KeyboardInterrupt:
    # Handle the Ctrl+C interruption
    print("\nConnection closed by user.")

finally:
    # Close the client socket
    client.close()
    print("Socket closed.")

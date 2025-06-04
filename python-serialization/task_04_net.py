#!/usr/bin/env python3
"""Client-server application using socket and JSON serialization."""

import socket
import json


def start_server(host='127.0.0.1', port=65432):
    """Start a TCP server to receive a serialized dictionary."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        conn, addr = server_socket.accept()
        with conn:
            data = conn.recv(1024).decode('utf-8')
            try:
                received_dict = json.loads(data)
                print("Received Dictionary from Client:")
                print(received_dict)
            except json.JSONDecodeError:
                print("Failed to decode JSON data.")


def send_data(dictionary, host='127.0.0.1', port=65432):
    """Send a dictionary to the server after serializing it."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
            client_socket.connect((host, port))
            serialized_data = json.dumps(dictionary)
            client_socket.sendall(serialized_data.encode('utf-8'))
    except ConnectionRefusedError:
        print("Failed to connect to the server.")

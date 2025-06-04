#!/usr/bin/env python3
"""Test script for task_04_net.py"""

import threading
import time
from task_04_net import start_server, send_data


def main():
    # Start the server in a background thread
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    # Give server time to set up
    time.sleep(1)

    # Client sends dictionary
    sample_dict = {
        'name': 'Alice',
        'age': 30,
        'city': 'Paris'
    }
    send_data(sample_dict)

    # Wait for the server to finish
    server_thread.join()


if __name__ == "__main__":
    main()

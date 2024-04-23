import subprocess
import platform
import time
from ping3 import ping


def packet_loss_rate(destination, count=10):
    loss_count = 0
    for _ in range(count):
        result = ping(destination, timeout=1)
        if result is None:
            loss_count += 1
    return (loss_count / count) * 100

def main():
    print("Packet Loss Rate Tracker")
    destination = input("Enter the destination to ping: ")
    count = int(input("Enter the number of packets to send (default is 10): ") or 10)
    print("Pinging {}...".format(destination))
    time.sleep(1)  # Wait for 1 second before starting ping
    loss_rate = packet_loss_rate(destination, count)
    print("Packet loss rate to {} is {:.2f}%".format(destination, loss_rate))

if __name__ == "__main__":
    main()

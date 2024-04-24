import subprocess
import platform
import time
 
from ping3 import ping

def packet_loss_rate(destination, count=10):
    loss_count = 0
    for _ in range(count):
        result = ping(destination, timeout=1)
        if result is None:  # Check if there was no response
            loss_count += 1

    if count == 0:
        return None

    # If all packets were lost, return 100% packet loss rate
    if loss_count == count:
        return 100.0

    return (loss_count / count) * 100



def main():
    print("Packet Loss Rate Tracker")
    destination = input("Enter the destination to ping: ")
    count = int(input("Enter the number of packets to send (default is 10): ") or 10)
    print("Pinging {}...".format(destination))
    time.sleep(1)  # Wait for 1 second before starting ping
    loss_rate = packet_loss_rate(destination, count)
    if loss_rate is not None:
        print("Packet loss rate to {} is {:.4f}%".format(destination, loss_rate))
    else:
        print("Failed to determine packet loss rate.")

if __name__ == "__main__":
    main()

import ping3 as ping

def calculate_packet_loss(ping_results, threshold=1000):
    successful_pings = sum(1 for result in ping_results if result is not None and result <= threshold)
    packet_loss_rate = 100.0 - (successful_pings / len(ping_results) * 100.0)
    return packet_loss_rate

def main():
    target_host = input("Enter the host to ping (e.g., www.example.com): ")
    num_requests = int(input("Enter the number of ping requests to send: "))

    timeout = float(input("Enter the timeout duration in seconds (default is 1 second): ") or 1)

    ping.DEFAULT_TIMEOUT = timeout

    ping_results = []
    for _ in range(num_requests):
        response_time = ping.ping(target_host)
        ping_results.append(response_time)
    
    print("Ping Results:")
    for i, response_time in enumerate(ping_results):
        if response_time is not None:
            print(f"Ping {i+1}: {response_time} ms")
        else:
            print(f"Ping {i+1}: Request timed out")

    if all(result is None for result in ping_results):
        packet_loss_rate = 100.0
    else:
        packet_loss_rate = calculate_packet_loss(ping_results)
    print(f"\nPacket Loss Rate: {packet_loss_rate:.2f}%")

    # Wait for user input before exiting
    input("Press Enter to exit...")

if __name__ == "__main__":
    main()

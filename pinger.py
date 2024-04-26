import ping3 as ping

def main():
    try:
        target_host = input("Enter the host to ping (e.g., google.com): ")
        num_requests = int(input("Enter the number of ping requests to send: "))

        timeout = float(input("Enter the timeout duration in seconds (default is 1 second): ") or 1)

        ping.DEFAULT_TIMEOUT = timeout

        ping_results = []
        successful_pings = 0

        print(f"Pinging {target_host} with {num_requests} packets:")
        for _ in range(num_requests):
            response_time = ping.ping(target_host)
            if response_time is not None:
                successful_pings += 1
                print(f"Reply from {target_host}: time={response_time}ms")
            else:
                print("Request timed out")
            ping_results.append(response_time)

        packet_loss = num_requests - successful_pings
        packet_loss_rate = (packet_loss / num_requests) * 100 if num_requests > 0 else 0

        print(f"\nPing statistics for {target_host}:")
        print(f"    Packets: Sent = {num_requests}, Received = {successful_pings}, Lost = {packet_loss} ({packet_loss_rate:.0f}% loss)")

        if ping_results:
            # Filter out None values and calculate max, min, and average
            non_none_times = [time for time in ping_results if time is not None]
            min_time = min(non_none_times) if non_none_times else None
            max_time = max(non_none_times) if non_none_times else None
            avg_time = sum(non_none_times) / successful_pings if successful_pings > 0 else 0

            print("Approximate round trip times in milli-seconds:")
            print(f"    Minimum = {min_time}ms, Maximum = {max_time}ms, Average = {avg_time:.2f}ms")

    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except ping3.NetworkError as e:
        print(f"Network error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

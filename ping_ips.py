import argparse
import platform
import subprocess

def ping_ips_from_file(input_file, output_file):
    """
    Reads a list of IPs from a file, pings each, and logs results to another file.

    Args:
        input_file (str): Path to the file containing IP addresses.
        output_file (str): Path to the file where results will be logged.
    """
    try:
        with open(input_file, 'r') as file:
            ip_list = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        return
    except Exception as e:
        print(f"Error reading file '{input_file}': {e}")
        return

    results = {}
    ping_command = ["ping", "-n", "1"] if platform.system().lower() == "windows" else ["ping", "-c", "1"]

    for ip in ip_list:
        try:
            output = subprocess.run(ping_command + [ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if output.returncode == 0:
                results[ip] = "Success"
            else:
                results[ip] = "Failure"
        except Exception as e:
            results[ip] = f"Error: {str(e)}"

    try:
        with open(output_file, 'w') as file:
            for ip, status in results.items():
                file.write(f"{ip}: {status}\n")
    except Exception as e:
        print(f"Error writing to file '{output_file}': {e}")

def main():
    parser = argparse.ArgumentParser(description="Ping a list of hosts and write a connectivity report.")
    parser.add_argument("input_file", nargs="?", default="ips.txt", help="file with one IP or hostname per line (default: ips.txt)")
    parser.add_argument("-o", "--output", default="ping_results.txt", help="report file (default: ping_results.txt)")
    args = parser.parse_args()

    print(f"Reading IPs from {args.input_file} and logging results to {args.output}...")
    ping_ips_from_file(args.input_file, args.output)
    print(f"Ping operation complete. Check results in '{args.output}'.")

if __name__ == "__main__":
    main()

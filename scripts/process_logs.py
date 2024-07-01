import os
import pandas as pd

def read_log_file(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()
    return logs

def process_logs(logs):
    # Example processing: Count the number of logs
    log_count = len(logs)
    return log_count

def main():
    logs_dir = '../logs'
    log_files = [f for f in os.listdir(logs_dir) if os.path.isfile(os.path.join(logs_dir, f))]

    for log_file in log_files:
        file_path = os.path.join(logs_dir, log_file)
        logs = read_log_file(file_path)
        log_count = process_logs(logs)
        print(f"Processed {log_file}: {log_count} log entries")

if __name__ == "__main__":
    main()


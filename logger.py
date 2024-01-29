import sys
import datetime


def log_message(input_file):
    try:
        with open(input_file, "w") as file:
            while True:
                message = sys.stdin.readline().rstrip()
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                if message == "QUIT":
                    break
                # separates action and the rest (if any)
                action, rem = message.strip().split(None, 1)
                rem_list = []
                for val in rem:
                    rem_list.append(val)
                formatted_message = "{} [{}] {}".format(timestamp, action, ''.join(rem_list))
                file.write(formatted_message + "\n")
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    if len(sys.argv) != 2:  # if we forget to add the file name
        print("Usage: python logger.py <log_file>")
        sys.exit(1)
    log_file = sys.argv[1]
    log_message(log_file)

import subprocess
import sys


def call_all(log_file):
    history = []
    input_var = ""
    log_args, encryption_args = ["python", "logger.py", log_file], ["python", "encryption.py"]
    logger_process = subprocess.Popen(log_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    encryption_process = subprocess.Popen(encryption_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, universal_newlines=True)
    logger_process.stdin.write("START Logging Started.\n")
    logger_process.stdin.flush()
    while True:
        print("\nMenu:")
        print("1. Password")
        print("2. Encrypt")
        print("3. Decrypt")
        print("4. History")
        print("5. Quit")

        choice = input("Enter your choice: ")
        if choice == "1":
            print("1. Use a string from history")
            print("2. Enter a new string")
            password_choice = input("Enter your choice: ")
            if password_choice == "1":
                print("Select a password from history:")
                for i, password in enumerate(history):
                    print("{} {}".format(i + 1, password))
                password_index = int(input("Enter the number: ")) - 1
                if 0 <= password_index < len(history):
                    input_var = history[password_index]
                else:
                    print("Invalid selection.")
            elif password_choice == "2":
                input_var = input("Enter a new password: ")
            else:
                print("Invalid choice.")
            encryption_process.stdin.write("PASSKEY {}\n".format(input_var))
            encryption_process.stdin.flush()
            out = encryption_process.stdout.readline().strip()
            print(out)
            logger_process.stdin.write("SET_PASSWORD Password Set!\n")
            logger_process.stdin.flush()
        elif choice == "2":
            print("1. Use a string from history")
            print("2. Enter a new string")
            e_choice = input("Enter your choice: ")
            if e_choice == "1":
                print("Select an encryption string from history:")
                for i, e in enumerate(history):
                    print("{} {}".format(i + 1, e))
                e_index = int(input("Enter the number: ")) - 1
                if 0 <= e_index < len(history):
                    input_var = history[e_index]
                else:
                    print("Invalid selection.")
            elif e_choice == "2":
                input_var = input("Enter a new encryption string: ")
            else:
                print("Invalid choice.")
            history.append(input_var)
            encryption_process.stdin.write("ENCRYPT {}\n".format(input_var))
            encryption_process.stdin.flush()
            out = encryption_process.stdout.readline().strip()
            print(out)
            logger_process.stdin.write("ENCRYPT {} --> {}\n".format(input_var, out.split(' ', 1)[1]))
            logger_process.stdin.flush()
        elif choice == "3":
            print("1. Use a string from history")
            print("2. Enter a new string")
            d_choice = input("Enter your choice: ")
            if d_choice == "1":
                print("Select a decryption string from history:")
                for i, d in enumerate(history):
                    print("{} {}".format(i + 1, d))
                d_index = int(input("Enter the number: ")) - 1
                if 0 <= d_index < len(history):
                    input_var = history[d_index]
                else:
                    print("Invalid selection.")
            elif d_choice == "2":
                input_var = input("Enter a new decryption string: ")
            else:
                print("Invalid choice.")
            history.append(input_var)
            encryption_process.stdin.write("DECRYPT {}\n".format(input_var))
            encryption_process.stdin.flush()
            out = encryption_process.stdout.readline().strip()
            print(out)
            logger_process.stdin.write("DECRYPT {} --> {}\n".format(input_var, out.split(' ', 1)[1]))
            logger_process.stdin.flush()
        elif choice == "4":
            print("History:")
            for i, h in enumerate(history):
                print("{} {}".format(i + 1, h))
            logger_process.stdin.write("HISTORY Checked!\n")
            logger_process.stdin.flush()
        elif choice == "5":
            encryption_process.stdin.write("QUIT\n")
            encryption_process.stdin.flush()
            logger_process.stdin.write("STOP Logging Stopped.\n")
            logger_process.stdin.flush()
            logger_process.stdin.write("QUIT\n")
            logger_process.stdin.flush()
            encryption_process.wait()
            logger_process.wait()
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python driver.py <log_file>")
        sys.exit(1)
    log_file = sys.argv[1]
    call_all(log_file)

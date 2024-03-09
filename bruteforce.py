import subprocess
binary_path = "./chall"
start_value = 0
increment = 1

num_runs = None  # Set to a specific number, or None for continuous execution

current_value = start_value

while num_runs is None or num_runs > 0:
    command = [binary_path, str(current_value)]

    try:
        # Execute the binary using subprocess
        output = subprocess.run(command, check=True, capture_output=True).stdout.decode()  # Indent this line correctly

        subprocess.run(command, check=True)  # Use check=True to raise an exception if the binary fails

        print(f"Executed binary with argument: {current_value}")
        if "You win!" in output:
            print("Congratulations! You won!")
            break

        current_value += increment  # Increment for the next run

        if num_runs is not None:
            num_runs -= 1  # Decrement the run counter if applicable

    except subprocess.CalledProcessError as e:
        print(f"Error running binary: {e}")
        break  # Exit the loop if the binary fails


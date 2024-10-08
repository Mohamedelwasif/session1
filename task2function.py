import os
import random

def manage_folder(folder_path, num_files):
    # Step 1: Open the whole folder (ensure it exists)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Step 2: Create a number of files inside it
    for i in range(num_files):
        with open(os.path.join(folder_path, f"file_{i}.txt"), 'w') as f:
            f.write(f"Content of file {i}")

    # Step 3: Check the length of files in that folder
    all_files = os.listdir(folder_path)
    print(f"Total files created: {len(all_files)}")

    # Step 4: Delete random half of this folder
    num_to_delete = len(all_files) // 2
    files_to_delete = random.sample(all_files, num_to_delete)

    for file in files_to_delete:
        os.remove(os.path.join(folder_path, file))

    # Step 5: Check the result
    remaining_files = os.listdir(folder_path)
    print(f"Total files remaining: {len(remaining_files)}")
    print(f"Remaining files: {remaining_files}")

# Example usage:
manage_folder("example_folder", 10)

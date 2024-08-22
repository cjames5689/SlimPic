import os
import PIL.Image

DEFAULT_PHOTO_DIMENSION = (1600, 1200)
DESTINATION_PATH = "resized"
PROCESSED_PHOTO_COUNTER = 0


def main():
    display_title()
    display_instructions()

    while True:
        print("Type 'help' for instructions or 'exit' to exit the program.")

        user_input = input("Please enter a valid directory path or command: ").lower().strip('"\' ')

        user_input = os.path.normpath(user_input)

        input_logic(user_input)


def input_logic(command):
    """
    Processes user input and executes corresponding commands.

    Handles validation of the provided directory path or command. If a valid directory is
    entered, the function attempts to process the photos within. If an invalid directory
    or command is provided, appropriate error messages are displayed. Recognizes "help"
    and "exit" commands for guidance or exiting the program.

    Args:
        command (str): The user input, which can be a directory path or a command.

    Returns:
        None
    """
    if not command or command in [".", ".."]:
        print(f"""*Error: Invalid or empty directory entry: '{command}'
Please provide a specific directory path.
""")

    if os.path.isdir(command):
        try:
            process_photos(command)
        except Exception as e:
            print(f"""*Error: {e}
Please check input and ensure the entered directory path exists and is a valid path.
""")
        return
    elif command == "help":
        display_help()
    elif command == "exit":
        exit("User exited the program.")
    else:
        print(f"""*Error: The directory '{command}' was not found. 
Please check input and ensure the entered directory path exists and is a valid path.
""")


def display_title():
    print("""  _____   _   _               _____    _        
 / ____| | | (_)             |  __ \\  (_)       
| (___   | |  _   _ __ ___   | |__) |  _    ___ 
 \\___ \\  | | | | | '_ ` _ \\  |  ___/  | |  / __|
 ____) | | | | | | | | | | | | |      | | | (__ 
|_____/  |_| |_| |_| |_| |_| |_|      |_|  \\___|
 
A lightweight .jpeg size reducer.
""")


def display_instructions():
    print("""
To get started: 
Please provide a specific directory path containing the .jpeg(s) you wish to reduce. 
The program will not accept an empty input or relative path notation as valid input.
""")


def display_help():
    print("""
Instructions:
To get the work order's specific directory path:
1. Open Windows Explorer
2. Navigate to the folder with the current work order's photos
3. You can either:
   - Click the address bar to highlight the path, then copy and paste it into this program
   - Or simply drag and drop the folder into this program window to automatically add the directory path.

Note: 
*SlimPic is a tool designed to reduce the file size of your .jpeg images by fitting them within a maximum 
bounding box of 1600x1200 pixels. The program preserves the original aspect ratio of your photos, ensuring they are 
resized based on their orientation—whether portrait or landscape. If the photos to be processed are already within
the bounding box resolution, they will be saved in the resized folder, but remain the original size.
""")


def process_photos(working_path):
    """Resize all `.jpeg` and `.jpg` photos in the specified directory.

    Searches for photos in `working_path`, resizes them, and saves the results
    to a 'resized' folder within the directory. If the folder exists, it reuses it;
    otherwise, it attempts to create it. Permission errors are caught and reported.

    Args:
        working_path (str): Path to the directory containing the photos.

    Notes:
        - Uses a global counter `PROCESSED_PHOTO_COUNTER` to track processed photos.
        - If no photos are found, the function terminates early.

    Returns:
        None
    """
    global PROCESSED_PHOTO_COUNTER
    failed_processes = {}
    resized_path = os.path.join(working_path, DESTINATION_PATH)
    os.chdir(working_path)

    source_files = [
        picture for picture in os.listdir(working_path)
        if os.path.splitext(picture)[1].lower() in [".jpeg", ".jpg"]
    ]
    total_files = len(source_files)

    if not source_files:
        print("\nNo files found to process.\n")
        return

    print("\nResizing photos. Please do not close the program until this process has completed.")

    if os.path.exists(resized_path):
        print("Resized directory already exists. Processed photos will be saved in this directory path.\n")
    else:
        try:
            os.makedirs(resized_path, exist_ok=True)
        except PermissionError as p:
            print(f"""*Error: {p}
Please contact the system administrator for permission to access this folder.
""")

    for picture in source_files:
        resize_and_save_photo(picture, working_path, resized_path, failed_processes)

    print(f"\n{PROCESSED_PHOTO_COUNTER} of {total_files} processed.\n")

    if failed_processes:
        print("The following files could not be processed:")
        log_failed_processes(failed_processes)
        print("Please check these files and try again.\n")

    PROCESSED_PHOTO_COUNTER = 0


def resize_and_save_photo(picture, working_path, resized_path, failed_processes):
    """
        Resizes a .jpeg image to fit within the specified dimensions and saves it.

        If the resized image already exists, it skips processing. Otherwise, it
        resizes the image while preserving the aspect ratio and saves it to the
        specified folder. If an image cannot be processed, it logs the error.

        Args:
            picture (str): The filename of the image to resize.
            working_path (str): The directory path containing the original image.
            resized_path (str): The directory path to save the resized image.
            failed_processes (dict): Dictionary to log any failed image processes.

        Returns:
            None
    """
    global PROCESSED_PHOTO_COUNTER
    picture_path = os.path.join(working_path, picture)
    resized_picture_path = os.path.join(resized_path, picture)
    resized_picture_name = os.path.basename(picture)

    if os.path.exists(resized_picture_path):
        print(f"{resized_picture_name} already processed.")
    else:
        try:
            with PIL.Image.open(picture_path) as im:
                im.thumbnail(DEFAULT_PHOTO_DIMENSION)
                im.save(resized_picture_path)
                print(f"{resized_picture_name} has been processed.")
                PROCESSED_PHOTO_COUNTER += 1
        except PIL.UnidentifiedImageError as e:
            failed_processes[picture] = e


def log_failed_processes(failed_processes):
    for picture, error in failed_processes.items():
        print(f"Filename: {picture}; Error: {error}")


if __name__ == "__main__":
    main()

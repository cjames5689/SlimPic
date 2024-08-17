import os
import PIL.Image

default_dimension = (1600, 1200)
destination_path = "resized"
processed_photo_counter = 0


def main():
    display_title()
    display_instructions()
    while True:
        print("Type 'help' for instructions or 'exit' to exit the program.")
        user_input = input("Please enter a valid directory path or command: ").lower().strip()
        user_input = os.path.normpath(user_input)
        input_logic(user_input)


def input_logic(command):
    if not command or command in [".", ".."]:
        print(f"""*Error: Invalid or empty directory entry: '{command}'
Please provide a specific directory path.
""")
        return False

    if os.path.isdir(command):
        if make_folder(command):
            resize_photo(command)
    elif command == "help":
        display_help()
    elif command == "exit":
        exit("User exited the program.")
    else:
        print(f"""*Error: The directory '{command}' was not found. 
Please check input and ensure the entered directory path exists and is a valid path.
""")
        return False


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
3. Click the address bar to highlight the path
4. Copy the path and paste it into this program

Note: 
*SlimPic is a tool designed to reduce the file size of your .jpeg images by fitting them within a maximum 
bounding box of 1600x1200 pixels. The program preserves the original aspect ratio of your photos, ensuring they are 
resized based on their orientation—whether portrait or landscape. If the photos to be processed are already within
the bounding box resolution, they will be saved in the resized folder, but remain the original size.
""")


def make_folder(current_path):
    resized_path = os.path.join(current_path, destination_path)

    if os.path.exists(resized_path):
        print("\nThe resized folder already exists. Processed photos will be saved in this directory path.\n")
        return True
    else:
        try:
            os.makedirs(resized_path)
            print(f"\n{resized_path} has been created.\n")
            return True
        except PermissionError as p:
            print(f"""*Error: {p}
Please contact the system administrator for permission to access this folder.
""")
        except Exception as e:
            print(f"""*Error: {e}
Please check input and ensure the entered directory path exists and is a valid path.
""")
            return False


def resize_photo(working_path):
    global processed_photo_counter
    os.chdir(working_path)
    source_files = [
        picture for picture in os.listdir(working_path)
        if os.path.splitext(picture)[1].lower() in [".jpeg", ".jpg"]
    ]
    total_files = len(source_files)
    if source_files:
        print("Resizing photos. Please do not close the program until this process has completed.")
        resized_path = os.path.join(working_path, destination_path)
        for picture in source_files:
            picture_path = os.path.join(working_path, picture)
            resized_picture_path = os.path.join(resized_path, picture)
            resized_picture_name = os.path.basename(resized_picture_path)
            if picture not in os.listdir(resized_path):
                try:
                    with PIL.Image.open(picture_path) as im:
                        im.thumbnail(default_dimension)
                        im.save(resized_picture_path)
                        print(f"{resized_picture_name} has been processed.")
                        processed_photo_counter += 1
                except PIL.UnidentifiedImageError as e:
                    print(f"\n*Error: Unknown file type. {picture} was not processed.\n{e}\n")
            else:
                print(f"{resized_picture_name} already processed.")
        print(f"\n{processed_photo_counter} of {total_files} files processed.\n")
    else:
        print("\nNo files found to be processed.\n")
    processed_photo_counter = 0
    return


if __name__ == "__main__":
    main()

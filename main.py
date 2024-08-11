import os
import PIL.Image

size = (1600, 1200)


def main():
    while True:
        user_input = (input("""(Type 'help' for instructions or 'exit' to exit the program.)
Please enter the current working directory: """)).lower().strip()
        user_input = os.path.normpath(user_input)
        input_logic(user_input)


def input_logic(command):
    if not command or command == ".":
        print("Empty directory entry. Please enter a valid directory path.\n")
    elif command == "help":
        display_help()
    elif command == "exit":
        exit("User exited the program.")
    elif os.path.isdir(command):
        if make_folder(command):
            resize_photo(command)
    else:
        print(f"The directory '{command}' was not found. Please enter a valid directory path.\n")


def display_help():
    print("""\nTo get the current working directory:

1. Open Windows Explorer
2. Navigate to the folder with the current work order's photos
3. Click the address bar to highlight the path
4. Copy the path and paste it into this program

Note: This program will only resize .jpg and .jpeg files.\n""")


def make_folder(path):
    try:
        resized_path = os.path.join(path, "resized")
        os.makedirs(resized_path, exist_ok=True)
        print(f"\n{resized_path} has been created.\n")
        if os.path.isdir(resized_path):
            return True
    except WindowsError as w:
        print(f"\nAccess denied. Contact administrator for directory access.\n{w}\n")
    except Exception as e:
        print(f"\nThere was an error when creating the 'resized' folder.\nError code: {e}\n")


def resize_photo(path):
    success_count = 0
    os.chdir(path)
    source_files = [
        picture for picture in os.listdir(path)
        if os.path.splitext(picture)[1].lower() in [".jpeg", ".jpg"]
    ]
    total_files = len(source_files)
    if source_files:
        print("Resizing...")
        resized_dir = os.path.join(path, "resized")
        for picture in source_files:
            picture_path = os.path.join(path, picture)
            resized_picture_path = os.path.join(resized_dir, picture)
            resized_picture_name = os.path.basename(resized_picture_path)
            try:
                if picture not in os.listdir(resized_dir):
                    with PIL.Image.open(picture_path) as im:
                        im.thumbnail(size)
                        im.save(resized_picture_path)
                        success_count += 1
                        print(f"{resized_picture_name} has been processed.")
                else:
                    print(f"{resized_picture_name} already processed.")
            except PIL.UnidentifiedImageError as e:
                print(f"\nUnknown file type. {picture} was not processed.\n{e}\n")
        print(f"\n{success_count} of {total_files} files processed.\n")
    else:
        print("\nNo files found to be processed.\n")


if __name__ == "__main__":
    print("P H O T O    R E S I Z E R\n")
    main()

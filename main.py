import os
import PIL
from PIL import Image

size = (1600, 1200)


def main():
    while True:
        user_input = (input("(Type 'help' for instructions or 'exit' to exit the program.)\n"
                            "Please enter the current working directory: ")).lower()
        input_logic(user_input)


def make_folder(path):
    try:
        resized_path = os.path.join(path, "resized")
        os.makedirs(resized_path, exist_ok=True)
        print(f"\n"
              f"{resized_path} has been created.\n")
    except WindowsError as w:
        print(f"\nAccess denied. Contact administrator for directory access.\n{w}\n")
        main()
    except Exception as e:
        print(f"There was an error when creating the 'resized' folder.\nError code: {e}")
        main()


def resize_photo(path):
    success_count = 0
    os.chdir(path)
    jpg_jpeg_files = [
        picture for picture in os.listdir(path)
        if os.path.splitext(picture)[1].lower() in [".jpeg", ".jpg"]
    ]
    total_files = len(jpg_jpeg_files)
    if jpg_jpeg_files:
        print("Resizing...")
        resized_dir = os.path.join(path, "resized")
        for picture in jpg_jpeg_files:
            picture_path = os.path.join(path, picture)
            resized_picture_path = os.path.join(resized_dir, picture)
            try:
                if picture not in os.listdir(resized_dir):
                    with Image.open(picture_path) as im:
                        im.thumbnail(size)
                        im.save(os.path.join(path, "resized", picture))
                        success_count += 1
                        print(f"{os.path.basename(resized_picture_path)} has been processed.")
                else:
                    print("File already processed.")
            except PIL.UnidentifiedImageError as e:
                print(f"\nUnknown file type. {picture} was not processed.\n{e}\n")
        print(f"\n"
              f"{success_count} of {total_files} files processed.\n")
    else:
        print("\nNo files found to be processed.\n")


def input_logic(command):
    if command == "help":
        print("\nTo get the current working directory:\n"
              "1. Open Windows Explorer\n"
              "2. Navigate to the folder with the current work order's photos\n"
              "3. Click the address bar to highlight the path\n"
              "4. Copy the path and paste it into this program\n"
              "\n"
              "Note: This program will only resize .jpg/.jpeg files.\n")
    elif command == "exit":
        exit("User exited the program.")
    elif not command.strip():
        print("Empty entry. Please enter a valid directory path.\n")
    elif not os.path.isdir(command):
        print("Invalid directory entry. Please enter a valid directory path.\n")
    else:
        make_folder(command)
        resize_photo(command)


if __name__ == "__main__":
    print("P H O T O    R E S I Z E R\n")
    main()

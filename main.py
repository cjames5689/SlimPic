import os
from PIL import Image

size = (1600, 1200)


def make_folder(path):
    try:
        os.mkdir(path + "/resized/")
        print(f"\n"
              f"{os.path.join(path, "resized")} has been created.\n")
    except FileExistsError:
        print("\n"
              "The 'resized' directory already exists!\n")
    except OSError:
        print("Invalid directory path syntax. Please enter a valid directory path.")
    except Exception as e:
        print(f"The program exited with exit code {e}")


def resize_photo(path):
    success_count = 0
    os.chdir(path)
    pictures = os.listdir(path)
    jpg_jpeg_files = [picture for picture in pictures if os.path.splitext(picture)[1].lower() in [".jpeg", ".jpg"]]
    total_files = len(jpg_jpeg_files)
    if jpg_jpeg_files:
        print("Resizing...")
        for picture in jpg_jpeg_files:
            global size
            im = Image.open(picture)
            resized_picture = im.resize(size)
            resized_picture.save(f"{path}/resized/{picture}")
            file_name = os.path.basename(im.filename)
            success_count += 1
            print(f"{file_name} has been processed.")
            im.close()
        print(f"\n"
              f"{success_count} of {total_files} files processed.\n")
    else:
        print("No files found to be processed.\n")


def input_logic(command):
    if command == "help":
        print("\n"
              "To get the current working directory:\n"
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
    while True:
        user_input = (input("(Type 'help' for instructions or 'exit' to exit the program.)\n"
                            "Please enter the current working directory: ")).lower()
        input_logic(user_input)

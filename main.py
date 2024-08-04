import os
from PIL import Image

size = (1600, 1200)


def make_folder():
    try:
        path = user_input
        os.mkdir(path + "/resized/")
        os.chdir(path)
        name = os.getcwd()
        print(f"{name}\\resized\\ has been created.\n")
    except FileExistsError:
        print("The 'resized' directory already exists!\n")
    except OSError:
        print("Invalid directory path syntax. Please enter a valid directory path.")
    except Exception as e:
        print(f"The program exited with exit code {e}")


def resize_photo():
    success_count = 0
    os.chdir(user_input)
    current_directory = os.getcwd()
    pictures = os.listdir(current_directory)
    jpg_jpeg_files = [picture for picture in pictures if os.path.splitext(picture)[1].lower() in [".jpeg", ".jpg"]]
    total_files = jpg_jpeg_files.__len__()
    if jpg_jpeg_files:
        print("Resizing...")
    else:
        print("No files found to be processed.")
    for picture in pictures:
        picture_path = os.path.join(current_directory, picture)
        if os.path.isfile(picture_path):
            global size
            im = Image.open(picture)
            resized_picture = im.resize(size)
            resized_picture.save(f"{current_directory}/resized/{picture}")
            file_name = os.path.basename(im.filename)
            success_count += 1
            print(f"{file_name} has been processed.")
            im.close()
    print(f"\n"
          f"{success_count} of {total_files} files processed.\n")


def input_logic():
    if user_input == "help":
        print("To get the current working directory:\n"
              "1. Open Windows Explorer\n"
              "2. Navigate to the folder with the current work order's photos\n"
              "3. Click the address bar to highlight the path\n"
              "4. Copy the path and paste it into this program\n"
              "Note: This program will only resize .jpg/.jpeg files.\n")
    elif user_input == "exit":
        exit("User exited the program.")
    elif not user_input.strip():
        print("Empty entry. Please enter a valid directory path.\n")
    elif not os.path.isdir(user_input):
        print("Invalid directory entry. Please enter a valid directory path.\n")
    else:
        make_folder()
        resize_photo()


if __name__ == "__main__":
    print("P H O T O    R E S I Z E R")
    while True:
        user_input = (input("(Type 'help' for instructions or 'exit' to exit the program.)\n"
                            "Please enter the current working directory: ")).lower()
        input_logic()

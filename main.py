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
    os.chdir(user_input)
    current_directory = os.getcwd()
    pictures = os.listdir(current_directory)
    print("Resizing...")
    for picture in pictures:
        picture_path = os.path.join(current_directory, picture)
        if os.path.isfile(picture_path):
            extension = os.path.splitext(picture_path)[1].lower()
            if extension in [".jpeg", ".jpg"]:
                global size
                im = Image.open(picture)
                resized = im.resize(size)
                resized.save(f"{current_directory}/resized/{picture}")
                file_name = os.path.basename(im.filename)
                print(f"{file_name} has been processed.")
                im.close()


def input_logic():
    try:
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
        else:
            make_folder()
            resize_photo()
            exit_program()
    except FileNotFoundError:
        print("Invalid directory. Please enter a valid directory path.\n")


def exit_program():
    input("\n"
          "Press [Enter] to exit program.")
    exit("User exited the program.")


if __name__ == "__main__":
    print("P H O T O    R E S I Z E R")
    while True:
        user_input = (input("(Type 'help' for instructions or 'exit' to exit the program.)\n"
                            "Please enter the current working directory: ")).lower()
        input_logic()

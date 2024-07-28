import os
from PIL import Image
import pathlib


def main():
    make_folder()
    photo_resize()
    input("\n"
          "Press [Enter] to exit the script: ")
    exit()


def make_folder():
    try:
        os.mkdir(folder + "/resized/")
        os.chdir(folder)
        name = pathlib.Path.cwd()
        print(f"{name}\\resized\\ has been created.\n")
    except FileExistsError:
        print("The 'resized' directory already exists!\n")
        pass


def photo_resize():
    os.chdir(folder)
    current_directory = pathlib.Path.cwd()
    iterable = current_directory.iterdir()
    print("Resizing...")
    for item in iterable:
        if item.suffix == ".jpg":
            try:
                im = Image.open(item)
                resized = im.resize((1600, 1200))
                resized.save(f"{current_directory}/resized/{item.name}.jpg")
                print(f"{im.filename} has been processed.")
                im.close()
            except Exception as e:
                print(f"{item.name} was not processed. {e}")


if __name__ == "__main__":
    print("P H O T O    R E S I Z E R")
    while True:
        try:
            folder = (input("(Type 'help' for instructions or 'exit' to exit the program.)\n"
                            "Please enter the current working directory: ")).lower()
            if folder.lower() == "help":
                print("To get the current working directory:\n"
                      "1. Open Windows Explorer\n"
                      "2. Navigate to the folder with the current work order's photos\n"
                      "3. Click the address bar to highlight the path\n"
                      "4. Copy the path and paste it into this program\n"
                      "Note: This program will only resize .jpg/.jpeg files.\n")
            elif folder.lower() == "exit":
                exit("User exited the program.")
            elif folder == "":
                print("Empty entry. Please enter a valid directory path.\n")
            else:
                main()
        except FileNotFoundError:
            print("Invalid directory. Please enter a valid directory path.\n")

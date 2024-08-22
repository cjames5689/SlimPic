	
	 ____  _ _           ____  _      
	/ ___|| (_)_ __ ___ |  _ \(_) ___ 
	\___ \| | | '_ ` _ \| |_) | |/ __|
	 ___) | | | | | | | |  __/| | (__ 
	|____/|_|_|_| |_| |_|_|   |_|\___|
                                   


-----------------------------------------------------------------------------------------------------------------------------

OVERVIEW:

SlimPic is a tool designed to reduce the file size of your .jpeg images by fitting them within a maximum 
bounding box of 1600x1200 pixels. The program preserves the original aspect ratio of your photos, ensuring they are 
resized based on their orientation—whether portrait or landscape. If the photos to be processed are already within
the bounding box resolution, they will be saved in the resized folder, but remain the original size.
-----------------------------------------------------------------------------------------------------------------------------

USAGE:

Navigate to the directory containing the photo_resizer.exe executable. This can be found in the dist folder.

Run the executable 'main.exe'.

-----------------------------------------------------------------------------------------------------------------------------

INSTRUCTIONS:

Provide Directory Path:
   - You can manually input the directory path containing the .jpeg files by copying the path from Windows Explorer and pasting it into the program.
   - Alternatively, you can drag and drop the folder directly into the program window to automatically add the directory path.

Process Your Photos:
   - Once the directory is specified, SlimPic will resize the photos to fit within the 1600x1200 pixel bounding box while preserving their aspect ratio.
   - Photos that do not exceed these dimensions will be copied to the resized folder without modification.
-----------------------------------------------------------------------------------------------------------------------------

NOTES:

- This program only processes .jpg and .jpeg files.

- The script resizes images to fit within a maximum size of 1600x1200 pixels while preserving the original aspect ratio. This ensures that the images are scaled down proportionally 
without distortion independent of orientation, fitting within the bounding box while maintaining their natural dimensions.

- If the resized subdirectory already exists, the program will use it without creating a new one.
-----------------------------------------------------------------------------------------------------------------------------

EXIT:

To exit the program at any time, type exit when prompted.
-----------------------------------------------------------------------------------------------------------------------------


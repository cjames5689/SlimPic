  ########  ##     ##  #######  ########  #######           ########  ########  ######  #### ######## ######## ########  
  ##     ## ##     ## ##     ##    ##    ##     ##          ##     ## ##       ##    ##  ##       ##  ##       ##     ## 
  ##     ## ##     ## ##     ##    ##    ##     ##          ##     ## ##       ##        ##      ##   ##       ##     ## 
  ########  ######### ##     ##    ##    ##     ##          ########  ######    ######   ##     ##    ######   ########  
  ##        ##     ## ##     ##    ##    ##     ##          ##   ##   ##             ##  ##    ##     ##       ##   ##   
  ##        ##     ## ##     ##    ##    ##     ##          ##    ##  ##       ##    ##  ##   ##      ##       ##    ##  
  ##        ##     ##  #######     ##     #######           ##     ## ########  ######  #### ######## ######## ##     ##

-----------------------------------------------------------------------------------------------------------------------------

OVERVIEW:
The Photo Resizer is a simple program designed to resize all .jpg images in a specified directory to a max resolution of 1600x1200 pixels. The resized images are saved in a subdirectory named 'resized'. If the photo's original resolution is lower than the 1600x1200 bounding box, the script using thumbnail() will leave the image unchanged. It will not upscale the image, so the original resolution is preserved without any resizing.
-----------------------------------------------------------------------------------------------------------------------------

USAGE:
*Navigate to the directory containing the photo_resizer.exe executable. This can be found in the dist folder.

*Run the executable 'main.exe'.
-----------------------------------------------------------------------------------------------------------------------------

Follow the prompts to enter the path of the directory containing the photos you want to resize. If you need help finding the directory path, type help for instructions.
The program will create a subdirectory named resized in the specified directory and save all resized images there.
-----------------------------------------------------------------------------------------------------------------------------

INSTRUCTIONS:
*Open Windows Explorer and navigate to the folder with the current work order's photos.

*Click the address bar to highlight the path. (Refer to ADDRESS BAR EXAMPLE if necessary)

*Copy the path and paste it into the program when prompted.

*The program will resize all .jpg files in the specified directory and save the resized images in the resized subdirectory.
-----------------------------------------------------------------------------------------------------------------------------

NOTES:
*This program only processes .jpg and .jpeg files.

*The script resizes images to fit within a maximum size of 1600x1200 pixels while preserving the original aspect ratio. This ensures that the images are scaled down proportionally without distortion, fitting within the bounding box while maintaining their natural dimensions.

*If the resized subdirectory already exists, the program will use it without creating a new one.
-----------------------------------------------------------------------------------------------------------------------------

EXIT:
To exit the program at any time, type exit when prompted for a directory path.
-----------------------------------------------------------------------------------------------------------------------------

ERROR HANDLING:
*If an invalid directory path is entered, the program will prompt you to enter a valid path.

*If an error occurs while processing an image, the program will notify you and continue processing the remaining images.
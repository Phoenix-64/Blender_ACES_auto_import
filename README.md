# Blender_ACES_auto_import
Automatically set the colour spaces of all images and videos 
To execute the addon and set the image spaces for all found videos and images press the import ACES button in the tools panel. 
To include more file names as sRGB images you can add part of its file name to the sRGB input field, make sure to precede it with a semicolon:
;my_file_name
The same goes for the HDRis. All images whose name was not found are regarded as raw images.
To change the Colour Space the Images are set to you need to go into the python file and change the colorspace_settings.name.

# Wallpaper_changer
Wallpaper Changer is a graphical interface designed with PyQt5 which allows to periodically change the wallpaper. 

(For Windows)

# How does the program work ?
- The first thing to do is to select a folder containing images likely to be wallpapers. Once this is done, the program indicates the number of images present in the directory.
Note : if the directory does not contain images, or too few (at least 2), the process will not be able to start.

- Then the user sets a timer which will determine how often the wallpaper should change. The unit of time can be in minutes or seconds.

- Once the process has been launched (indicated by a green LED), the program randomly chooses the images in the directory choosen by the user. Note : only the .jpg, .jpeg and .png images are taken into account.

- A countdown announces the display of the next wallpaper, a counter of wallpapers already displayed is also available.

- The user can stop the process at any time by pressing STOP.

# Screenshots
## Setting the timer after choosing the directory
![cap1](https://user-images.githubusercontent.com/11463619/109429962-03a99980-79ff-11eb-9b9f-86431c5b3674.png)

## The process is launched
![cap2](https://user-images.githubusercontent.com/11463619/109429963-04423000-79ff-11eb-9e0a-802e1452e4bb.png)

# Requirements
- `PyQt5`
- `py-wallpaper` (Only compatible with Windows and Mac)

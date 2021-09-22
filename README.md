# Customizable NASA's Picture of the Day Wallpaper for KDE Plasma

KDE Plasma has an option to set your wallpaper as NASA's Picture of the Day and it's really nice.  
But I was facing 2 problems with this:
1. Unfortunately you can't really understand the image without the explanation provided on NASA's page.  
2. Using a triple monitor setup, I wanted 3 different images for the last 3 days (including today)
KDE by default did not provide this functionality and I didn't want to spend too much 
time (yet) into building a plugin for KDE.

So here's my solution to these problems:
1. Use conky to display the explanation
2. Use a plugin called HTML Wallpaper and create a page that can display NASA's POTD for a particular day offset.
The `nasa_potd_desc.py` file solves both of these problems. It prints out the output for conky to display on my screen 
and saves the image to be displayed on a HTML page using HTML Viewer.

### How to use
1. Clone the repository
2. Add the following line to your conky config replacing `[offset]` with the number of days you want to offset the results by:
   ```
   ${execpi 300 python /home/kartikay/Programming/nasa-wp/nasa_potd_desc.py -d [offset]}
   ```
3. Install the HTML Wallpaper plugin and set the path to replacing `[offset]` as before and subsituting your 
monitor's height and width for `[height]` and `[width]`:
   ```
   file:///location/of/repository/day.html?diff=[offset]&height=[height]&width=[width]
   ```

Final Results:
![Screenshot_20210923_043900](https://user-images.githubusercontent.com/19384906/134433664-696068fa-4034-46af-af3a-c296d6563235.png)

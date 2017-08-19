# Important imports for all the features
from __future__ import print_function
from PIL import Image as pImg
from PIL import ImageFont
from PIL import ImageDraw
from tkinter import *
import os
import random

# Class for the TK library.
class Application(Frame):
    # Create master window
    def __init__(mFrame, master=None):
        super().__init__(master)
        mFrame.pack()
        mFrame.create_widgets()

    # Define the widgets in the frame
    def create_widgets(mFrame):
        # Reads the TopImages folder for "Options" to present to user
        OPTIONS = os.listdir('TopImages')
        variable = StringVar(mFrame)
        variable.set(OPTIONS[0])
        OptionMenu(mFrame, variable, *OPTIONS).pack(side="right")

        # Once an option is selected above, this button allows users to
        # run the MyFavoriteColorsIs application and get a result
        mFrame.hi_there = Button(mFrame)
        mFrame.hi_there["text"] = "Run"
        mFrame.hi_there["command"] = lambda: mFrame.imgGen(variable.get())
        mFrame.hi_there.pack(side="top")

        # This button allows users to quit out of the application
        mFrame.quit = Button(mFrame, text="QUIT", fg="red",
                              command=root.destroy)
        mFrame.quit.pack(side="bottom")

    def imgGen(ignore, directory):
        # Count is used to prevent unlimited options being presented.
        count = 1

        # Creates a blank image to copy the iterations into. Each iteration is
        # 300x300 and so we have a 3X2 Grid with this size (900, 600)
        master = pImg.new('RGBA', (900, 600))

        while count <= 6:

            # Gets the cup image
            bi = pImg.open("BaseImages\cup.png")

            # Gets color splotch randomly
            # Color splotches should be PNGs with a transparent background
            # AND Color Splotches should be approxamitely: 150 (w) x 150 (h)
            colorFiles = os.listdir('ColorImages')
            cifName = colorFiles[random.randint(1, len(colorFiles)) - 1]
            ci = pImg.open("ColorImages\\" + cifName)

            # Gets two subject files randomly
            # Subject images should also be PNGs with transparent backgrounds
            # AND TopImages should be approxamitely: 55(w) X 75 (h)
            catFiles = os.listdir('TopImages\\' + directory)
            imgRange = len(catFiles)

            tifName = catFiles[random.randint(1, imgRange) - 1]
            ti = pImg.open('TopImages\\' + directory + '\\' + tifName)

            ti2fName = catFiles[random.randint(1, imgRange) - 1 ]
            ti2 = pImg.open('TopImages\\' + directory + '\\' + ti2fName)

            # Sets the font and size
            font = ImageFont.truetype("Fonts\SCRIPTBL.TTF", 15)

            # Combine the images
            bi.paste(ci, (45, 65), mask=ci)
            bi.paste(ti, (145, 50), mask=ti)
            bi.paste(ti2, (60, 150), mask=ti2)

            # Add text to file
            draw = ImageDraw.Draw(bi)
            draw.text((53, 130), "My Favorite Color: " + directory, (0,0,0), \
                font=font)

            # Move it to file
            if count == 1:
                master.paste(bi, (0,0))
            if count == 2:
                master.paste(bi, (300,0))
            if count == 3:
                master.paste(bi, (600,0))
            if count == 4:
                master.paste(bi, (0,300))
            if count == 5:
                master.paste(bi, (300,300))
            if count == 6:
                master.paste(bi, (600,300))

            # Increase Count to limit loop
            count += 1

        master.save('master.png', 'PNG')
        master.show()

root = Tk()
app = Application(master=root)
app.mainloop()

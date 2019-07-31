#initial commit
import imageio
import os

clip = os.path.abspath('sc-vid-to-gif.mp4')

def gifmaker(inputPath, targetFormat):
    outputPath = os.path.splitext(inputPath)[0] + targetFormat

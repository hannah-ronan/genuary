from PIL import Image
import glob
import os

folder = r"C:/Users/hanna/OneDrive/Documents/Programming_Projects/genuary/lenia/output_frames"

print(f"saving frames from {folder} as gif...")

frame_paths = sorted(glob.glob(os.path.join(folder, "*.png")))

frames = [Image.open(image) for image in frame_paths]

# Save as GIF
frames[0].save(
    "output.gif",
    format="GIF",
    append_images=frames[1:],
    save_all=True,
    duration=25,
    loop=0
)

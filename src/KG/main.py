from KG.image import Image
from KG.downsampler import *

# ближайший сосед
image_object = Image("src/KG/input/test_logo.png")
new_size = (200, 200)
downsample_neighbour(*new_size, img=image_object)
image_object.save_image("src/KG/output_2/neighbour.png")

# интерполяция
image_object = Image("src/KG/input/test_logo.png")
new_size = (100, 100)
downsample_interpoll(*new_size, img=image_object)
image_object.save_image("src/KG/output_2/interpoll.png")
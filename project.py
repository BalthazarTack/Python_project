"""This file have  functions that allow one to convert an image to an hexagonal one 
, and to save it as svg"""

import PIL.Image
import PIL.ImageDraw
import numpy as np
import matplotlib.pyplot as plt

image = PIL.Image.open("screenshot.jpg")
pixel = image.load()

outer_wilds=PIL.Image.open("outer_wilds.jpg")


def hex_iteration(img, hex_size):
    """This creates the center of the hexagones of the image

    Args:
        img (Image): The image you want to compute the center of the hexagones
        hex_size (float): The size of the hexagones

    Returns:
        coord (2D array of tuple): The coordinates of the centers of the hexagones
    """
    img_array = np.array(img)
    height, width, _ = img_array.shape

    # Calculate the number of hexagons in both dimensions
    num_rows = int(height // (np.sqrt(3) * hex_size)) + 1
    num_cols = int(width // (1.5 * hex_size)) + 1

    # Initialize the coordinate array
    coord = np.zeros((num_rows, num_cols), dtype=object)

    for i in range(num_rows):
        for j in range(num_cols):
            # Calculate the x and y coordinates
            x_hex = j * 1.5 * hex_size
            if j % 2 == 0:
                y_hex = i * (np.sqrt(3) * hex_size)
            else:
                y_hex = i * (np.sqrt(3) * hex_size) + (hex_size * np.sqrt(3) / 2)
            coord[i][j] = (x_hex, y_hex)
    return coord


def plot_hexagons_on_image(img, hex_size):
    """Draw the image on the hexagonal grid

    Args:
        img (Image): The input image
        hex_size (Float): The size of the hexagones
    """
    # Get the hexagon centers
    centers = hex_iteration(img, hex_size)

    # Plotting the image
    _, axis = plt.subplots(figsize=(10, 10))
    axis.imshow(img)

    img_np = np.array(img)
    # Loop through the centers and plot them
    for row in centers:
        for center in row:
            if center is not None:
                y_coord, x_coord = center
                hex_corners = [flat_hex_corner(center, hex_size, i) for i in range(6)]
                colors=average_color_in_hex(img,hex_corners=hex_corners)
                color_normalized = [c / 255 for c in colors]
                hexagon = plt.Polygon(
                    hex_corners,
                    closed=True,
                    edgecolor="none",
                    facecolor=color_normalized,
                    linewidth=0.1,
                )
                axis.add_patch(hexagon)
    plt.axis("off")
    plt.savefig("hexagones.svg", format="svg")
    plt.show()


def flat_hex_corner(center, size, i):
    """Draws an equilateral triangle

    Args:
        center (Array): The coordinates of the center point of the hexagone
        size (Float): The size of the hexagones
        i (Int): Used to set the direction of the angle of the triangle
            with regard to the center of the hexagone

    Returns:
        points (Tuple): The coordinates of the 2 other points of the triangle
    """
    angle_deg = 60 * i
    angle_rad = np.pi / 180 * angle_deg
    points = (
        center[0] + size * np.cos(angle_rad),
        center[1] + size * np.sin(angle_rad),
    )
    return points

def average_color_in_hex(image, hex_corners):
    np_image = np.array(image)
    

    mask = PIL.Image.new("L", (image.width, image.height), 0)
    draw = PIL.ImageDraw.Draw(mask)
    draw.polygon(hex_corners, fill=255)
    

    mask_np = np.array(mask)
    

    hex_pixels = np_image[mask_np == 255]


    avg_color = hex_pixels[:, :3].mean(axis=0)

    return tuple(avg_color.astype(int))



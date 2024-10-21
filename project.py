"""This file have  functions that allow one to convert an image to an hexagonal one 
, and to save it as svg"""

import PIL.Image
import numpy as np
import matplotlib.pyplot as plt

image = PIL.Image.open("screenshot.jpg")
pixel = image.load()


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

    img = np.array(img)
    # Loop through the centers and plot them
    for row in centers:
        for center in row:
            if center is not None:
                y_coord, x_coord = center
                if int(x_coord) == img.shape[0]:
                    x_coord = img.shape[0] - 1
                if int(x_coord) == 0:
                    x_coord = 1
                if int(y_coord) == 0:
                    y_coord = 1
                red_hex = img[int(x_coord)][int(y_coord)][0] / 255
                green_hex = img[int(x_coord) - 1][int(y_coord)][1] / 255
                blue_hex = img[int(x_coord) - 1][int(y_coord)][2] / 255
                hex_corners = [flat_hex_corner(center, hex_size, i) for i in range(6)]
                hexagon = plt.Polygon(
                    hex_corners,
                    closed=True,
                    edgecolor="none",
                    facecolor=(red_hex, green_hex, blue_hex),
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
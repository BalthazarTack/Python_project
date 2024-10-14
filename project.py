import PIL.Image
import numpy as np
import matplotlib.pyplot as plt

image=PIL.Image.open("screenshot.jpg")
pixel=image.load()


def hex_iteration(img, hex_size):
    img_array = np.array(img)
    h,w, _ = img_array.shape
    
    # Calculate the number of hexagons in both dimensions
    num_rows = int(h // (np.sqrt(3) * hex_size)) + 1
    num_cols = int(w // (1.5 * hex_size)) + 1
    
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
    # Get the hexagon centers
    centers = hex_iteration(img, hex_size)

    # Plotting the image
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(img)

    # Loop through the centers and plot them
    for row in centers:
        for center in row:
            if center is not None:
                x, y = center
                hex_corners = [flat_hex_corner(center, hex_size, i) for i in range(6)]
                hexagon = plt.Polygon(hex_corners, closed=True, edgecolor='black', facecolor='none', linewidth=0.1)
                ax.add_patch(hexagon)
    plt.axis('off')  # Hide axes
    plt.show()

def flat_hex_corner(center, size, i):
    angle_deg = 60 * i
    angle_rad = np.pi / 180 * angle_deg
    return (center[0] + size * np.cos(angle_rad),
            center[1] + size * np.sin(angle_rad))


plot_hexagons_on_image(image,13)
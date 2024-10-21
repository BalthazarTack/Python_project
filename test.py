
import PIL.Image
import numpy as np
import matplotlib.pyplot as plt
from project import hex_iteration
from project import flat_hex_corner

def test_hex_iteration():
    img = PIL.Image.new('RGB', (300, 200), color='white')

    hex_size = 10.0
    expected_num_rows = int(200 // (np.sqrt(3) * hex_size)) + 1
    expected_num_cols = int(300 // (1.5 * hex_size)) + 1
    

    result = hex_iteration(img, hex_size)


    assert result.shape == (expected_num_rows, expected_num_cols), (
        f"Expected result shape to be {(expected_num_rows, expected_num_cols)} but got {result.shape}"
    )


    assert result[0][0] == (0, 0), f"Expected (0, 0), but got {result[0][0]}"

    expected_y_offset = 0*(np.sqrt(3) * hex_size) + (hex_size * np.sqrt(3) / 2)

    assert result[0][1] == (1.5 * hex_size, expected_y_offset), f"Expected ({1.5 * hex_size}, {expected_y_offset}), but got {result[0][1]}"


    assert result[1][0] == (0, np.sqrt(3) * hex_size), f"Expected (0, {np.sqrt(3) * hex_size}), but got {result[1][0]}"


    expected_y_offset = (np.sqrt(3) * hex_size) + (hex_size * np.sqrt(3) / 2)
    assert result[1][1] == (1.5 * hex_size, expected_y_offset), (
        f"Expected ({1.5 * hex_size}, {expected_y_offset}), but got {result[1][1]}"
    )

def test_flat_hex_corner():

        center = (0, 0)
        size = 1

        expected_points = [
            (1.0, 0.0), 
            (0.5, np.sqrt(3) / 2),  
            (-0.5, np.sqrt(3) / 2),  
            (-1.0, 0.0),  
            (-0.5, -np.sqrt(3) / 2),  
            (0.5, -np.sqrt(3) / 2)   
        ]

        for i in range(6):
            assert np.allclose(flat_hex_corner(center, size, i)[0], expected_points[i][0]) ,f"Expected {expected_points[i][0]} , but got {flat_hex_corner(center, size, i)[0]}"
            assert np.allclose(flat_hex_corner(center, size, i)[1],expected_points[i][1]) , f"Expected {expected_points[i][1]} , but got {flat_hex_corner(center, size, i)[1]}"

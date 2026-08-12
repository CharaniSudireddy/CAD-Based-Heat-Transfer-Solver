# CAD-Based Heat Transfer Solver

## About the Project

This project is a Python program that takes a 2D CAD drawing in DXF format and uses it to study how temperature is distributed across the shape.

The idea was to connect a CAD model with a numerical heat-transfer calculation. The program reads the geometry, creates a computational grid over it, applies temperatures at the boundaries, and then calculates the temperature at the internal points.

## What the Program Does

* Reads 2D geometry directly from DXF files
* Handles lines, polylines, splines, and circles
* Creates a user-defined computational grid
* Allows different temperatures to be assigned to the four boundaries
* Calculates temperatures at the internal grid points iteratively
* Calculates the temperature gradient
* Displays the final temperature distribution as a contour plot

The DXF geometry is processed using `ezdxf`, while `NumPy` is used for numerical calculations and `Matplotlib` is used to visualize the results.

## How It Works

1. The program asks for a DXF file and reads its geometry.
2. The geometry is converted into points that can be used for the calculation.
3. A computational grid is created based on the dimensions of the CAD shape.
4. Boundary temperatures are provided by the user.
5. The temperature at the internal nodes is updated repeatedly using the temperatures of neighboring nodes.
6. The temperature gradient is calculated from the resulting temperature field.
7. A contour plot is generated to show how temperature varies across the shape.

## Technologies Used

* **Python** — Main programming language
* **ezdxf** — Reading and processing DXF CAD files
* **NumPy** — Numerical calculations and grid operations
* **Matplotlib** — Temperature distribution visualization

## Project Files

* `HMT_project.py` — Main Python program
* `Part1.DXF` — Sample CAD geometry
* `Part2.DXF` — Sample CAD geometry
* `Part3.DXF` — Sample CAD geometry

## Running the Project

Install the required Python libraries:

```bash
pip install ezdxf numpy matplotlib
```

Then run:

```bash
python HMT_project.py
```

The program will ask for the DXF filename, grid size, and boundary temperatures before performing the calculation.

## What I Learned

Working on this project helped me understand how a real CAD model can be converted into data that a computer can work with. It also gave me practical experience with Python file processing, numerical methods, arrays, iterative computation, and visualizing computational results.

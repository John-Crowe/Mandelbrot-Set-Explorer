# Mandelbrot Set Explorer

About This Project
This project is a Mandelbrot Set plot explorer built using Python's Tkinter and PIL libraries. It allows users to interactively explore the Mandelbrot Set by zooming in on any point within the plot by clicking on the area of interest.

Key Features
Interactive Exploration: Click anywhere on the plot to zoom in and explore the intricate details of the Mandelbrot Set.
Dynamic Plotting: The plot updates in real-time as you zoom, providing a smooth exploration experience.
Color-Coded Iterations: Points within the Mandelbrot Set are colored black, while points outside are color-coded based on the number of iterations required to escape.
Technical Details

Zoom Mechanism: The zoom factor doubles with each click, centering on the clicked point.

Iteration Limit: The Mandelbrot Set calculation iterates up to 50 times for each point to determine membership.

How It Works
Initialization: The canvas is initialized as a white image.
Mandelbrot Calculation: The is_mandelbrot function checks whether a point belongs to the Mandelbrot Set.
Plot Creation: The make_mand function generates the Mandelbrot plot based on the current zoom level and position.
User Interaction: Clicking on the plot updates the origin, zooms in, and refreshes the plot.
Getting Started

# Relevant Libraries
* tkinter
* PIL
* numpy

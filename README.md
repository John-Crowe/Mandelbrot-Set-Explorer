# Mandelbrot Set Explorer

This project is a Mandelbrot explorer built using Python's Tkinter and PIL libraries. It allows users to interactively explore the Mandelbrot Set by zooming in on any point within the plot by clicking on the area of interest.

Key Features:

Click anywhere on the plot to zoom in and explore the intricate details of the Mandelbrot Set. The plot updates in real-time as you zoom, providing a smooth exploration experience. Points within the Mandelbrot Set are colored black, while points outside are color-coded based on the number of iterations required to escape.

Technical Details:

The zoom factor doubles with each click, centering on the clicked point. The Mandelbrot Set calculation iterates up to 50 times for each point to determine membership.

How It Works:

The canvas is initialized as a white image. The is_mandelbrot function checks whether a point belongs to the Mandelbrot Set. The make_mand function generates the Mandelbrot plot based on the current zoom level and position. Clicking on the plot updates the origin, zooms in, and refreshes the plot.

# Relevant Libraries
* tkinter
* PIL
* numpy

# I found this code in github, it's not mine!!!
import numpy as np
import matplotlib.pyplot as plt


# Plotting function creates a heatmap - Relied on by main.
def fn_plotting(values, tolerance, x_min, x_max, y_min, y_max):
	plt.xlabel("Real Axis")
	plt.ylabel("Imaginary Axis")
	plt.title("The Mandelbrot Set. Tolerance: %s" % tolerance)
	plt.grid(True)
	plt.imshow(values, origin="0,0", interpolation="none", extent=[x_min, x_max, y_min, y_max])
	plt.savefig("MandelBrot.png", bbox_inches="tight")
	plt.show()


# Algorithm to compute if point is within set - Relied on by main
def fn_mandel_calc(point, tolerance):
	z = 0
	for i in range(1, tolerance):
		if abs(z) > 2:
			return i
		z = z*z + point
	return 0


# Main function intialises & creates grid.  Dependent on _mandel_calc & _plotting.
def fn_mandelbrot_main(x_min, x_max, y_min, y_max, num_grid_pts, tolerance):
	real = np.linspace(x_min, x_max, num_grid_pts)
	imag = np.linspace(y_min, y_max, num_grid_pts)
	values = np.empty((num_grid_pts, num_grid_pts))
	for i in range(num_grid_pts):
		for j in range(num_grid_pts):
			values[j, i] = fn_mandel_calc(real[i] + 1j*imag[j], tolerance)
	fn_plotting(values, tolerance, x_min, x_max, y_min, y_max)
	return


G_x_min = float(input("Input x_min:"))
G_x_max = float(input("Input x_max:"))
G_y_min = float(input("Input y_min:"))
G_y_max = float(input("Input y_max:"))
G_num_grid_pts = int(input("Input num_grid_pts:"))
G_tolerance = int(input("Input tolerance:"))

print('Computing set ...')
fn_mandelbrot_main(G_x_min, G_x_max, G_y_min, G_y_max, G_num_grid_pts, G_tolerance)

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import numpy as np

class PolynomialPlotter(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("\Users\marco\OneDrive\Dokumente\Geomatik\1060Progamieren\Kapitel1\Abgaben\AbgabenPython\Uebung8\polynom2.ui", self)
        self.setWindowTitle("Polynomial Plotter")

        # Connect button and input field signals to handler methods
        self.plot_button.clicked.connect(self.plot_polynomial)
        self.coefficients_input.textChanged.connect(self.update_input_range)
        self.range_min_input.textChanged.connect(self.update_input_range)
        self.range_max_input.textChanged.connect(self.update_input_range)
        self.num_points_input.textChanged.connect(self.update_input_range)
        self.color_selector.currentTextChanged.connect(self.update_plot_color)

        # Set up the matplotlib figure and canvas for displaying plots
        self.figure = plt.figure(figsize=(8, 6))
        self.canvas = FigureCanvas(self.figure)
        self.plot_layout.addWidget(self.canvas)

        # Set initial input range and plot color
        self.update_input_range()
        self.update_plot_color(self.color_selector.currentText())

        self.show()

    def plot_polynomial(self):
        # Parse input values and generate polynomial function
        try:
            coeffs = [float(c.strip()) for c in self.coefficients_input.text().split(',')]
            x_min = float(self.range_min_input.text())
            x_max = float(self.range_max_input.text())
            num_points = int(self.num_points_input.text())
            x_vals = np.linspace(x_min, x_max, num_points)
            f = np.poly1d(coeffs)
            y_vals = f(x_vals)
        except ValueError:
            QMessageBox.warning(self, "Invalid input", "One or more input values are not valid numbers.")
            return

        # Clear any previous plot and generate new plot with current values
        self.figure.clear()
        plt.plot(x_vals, y_vals, self.plot_color)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.title("Polynomial Plot")
        self.canvas.draw()

    def update_input_range(self):
        # Validate input values and update input range display
        try:
            coeffs = [float(c.strip()) for c in self.coefficients_input.text().split(',')]
            x_min = float(self.range_min_input.text())
            x_max = float(self.range_max_input.text())
            num_points = int(self.num_points_input.text())
            x_range = f"({x_min:.2f}, {x_max:.2f})"
            self.input_range_label.setText(f"Input range: x {x_range}, num points: {num_points}")
        except ValueError:
            self.input_range_label.setText("Input range: N/A")

    def update_plot_color(self, color):
        # Update plot color based on user selection
        if color == "Black":
            self.plot_color = "k"
        elif color == "Blue":
            self.plot_color = "b"
        elif color == "Red":
            self.plot_color = "r"
        elif color == "Green":
            self.plot_color = "g"
        elif color == "Purple":
            self.plot_color = "m"

        #Update the plot with the new color
        if hasattr(self, "plot_color"):
            self.plot_polynomial()

if __name__ == '__main__':
    app = QApplication([])
    window = PolynomialPlotter()
    app.exec()

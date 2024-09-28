from PyQt6.QtWidgets import QApplication, QComboBox, QLineEdit, QWidget, QGridLayout, QLabel, QPushButton
import sys


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance (km):")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours):")
        self.time_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_speed)

        self.combo = QComboBox()
        self.combo.addItems(["Metric (km)", "Imperial (miles)"])

        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(calculate_button, 3, 1)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.time_edit, 1, 1)
        grid.addWidget(self.combo, 0, 3)
        grid.addWidget(self.output_label, 4, 0, 1, 3)

        self.setLayout(grid)

    def calculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_edit.text())
        if self.combo.currentText() == "Metric (km)":
            unit = "km/h"
            speed = round((distance / time), 2)
        if self.combo.currentText() == "Imperial (miles)":
            unit = "mph"
            speed = round((distance / time) * 0.621371, 2)

        self.output_label.setText(f"Avarage Speed: {speed} {unit}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()

sys.exit(app.exec())

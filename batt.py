import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import tkinter as tk

def generate_grid_layout(x_dim, y_dim, spacing, cell_size):
    radius = cell_size / 2
    positions = []
    x_start = radius + spacing
    y_start = radius + spacing
    y = y_start

    while y + radius + spacing <= y_dim:
        x = x_start
        while x + radius + spacing <= x_dim:
            positions.append((x, y))
            x += cell_size + spacing
        y += cell_size + spacing

    return positions

def generate_honeycomb_layout(x_dim, y_dim, spacing, cell_size):
    radius = cell_size / 2
    positions = []
    x_start = radius + spacing
    y_start = radius + spacing
    y = y_start

    row = 0
    while y + radius + spacing <= y_dim:
        x = x_start + (row % 2) * ((cell_size + spacing) / 2)
        while x + radius + spacing <= x_dim:
            positions.append((x, y))
            x += cell_size + spacing
        y += np.sqrt(3) * (radius + spacing / 2)
        row += 1

    return positions

def generate_vertical_honeycomb_layout(x_dim, y_dim, spacing, cell_size):
    radius = cell_size / 2
    positions = []
    x_start = radius + spacing
    y_start = radius + spacing
    x = x_start

    col = 0
    while x + radius + spacing <= x_dim:
        y = y_start + (col % 2) * ((cell_size + spacing) / 2)
        while y + radius + spacing <= y_dim:
            positions.append((x, y))
            y += cell_size + spacing
        x += np.sqrt(3) * (radius + spacing / 2)
        col += 1

    return positions

def close_window(root, canvas):
    canvas.get_tk_widget().destroy()
    root.quit()
    root.destroy()

def plot_layouts(x_dim, y_dim, grid_positions, honeycomb_positions, vertical_honeycomb_positions, cell_size, spacing):
    root = tk.Tk()
    root.title("Cell Layouts Viewer")
    root.geometry("1200x800")  # Set initial size of the main window

    fig, axs = plt.subplots(3, 1, figsize=(8, 18), tight_layout=True)

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    root.protocol("WM_DELETE_WINDOW", lambda: close_window(root, canvas))  # Handle window close

    def get_max_dimensions(positions):
        if positions:
            max_x = max(x for x, y in positions) + cell_size / 2
            max_y = max(y for x, y in positions) + cell_size / 2
        else:
            max_x, max_y = 0, 0
        return max_x, max_y

    for i, (positions, title, color) in enumerate([
        (grid_positions, "Grid Layout", ('blue', 'lightblue')),
        (honeycomb_positions, "Honeycomb Layout", ('green', 'lightgreen')),
        (vertical_honeycomb_positions, "Vertical Honeycomb", ('red', 'salmon'))
    ]):
        max_x, max_y = get_max_dimensions(positions)
        cell_count = len(positions)
        axs[i].set_xlim(0, x_dim)
        axs[i].set_ylim(0, y_dim)
        axs[i].set_aspect('equal', adjustable='box')
        axs[i].set_title(f"{title} ({cell_count} Cells, Max X: {max_x:.2f} mm, Max Y: {max_y:.2f} mm, Dim: {x_dim:.2f}x{y_dim:.2f} mm, Dia: {cell_size:.2f} mm)")
        for x, y in positions:
            circle = Circle((x, y), cell_size / 2, edgecolor=color[0], facecolor=color[1], alpha=0.7)
            axs[i].add_artist(circle)
        axs[i].grid(visible=True, linestyle="--", alpha=0.5)

    canvas.draw()
    root.mainloop()

def main():
    if len(sys.argv) != 5:
        print("Usage: python3 layout.py <x_dim> <y_dim> <spacing> <cell_size>")
        sys.exit(1)

    x_dim = float(sys.argv[1])
    y_dim = float(sys.argv[2])
    spacing = float(sys.argv[3])
    cell_size = float(sys.argv[4])

    grid_positions = generate_grid_layout(x_dim, y_dim, spacing, cell_size)
    honeycomb_positions = generate_honeycomb_layout(x_dim, y_dim, spacing, cell_size)
    vertical_honeycomb_positions = generate_vertical_honeycomb_layout(x_dim, y_dim, spacing, cell_size)

    plot_layouts(x_dim, y_dim, grid_positions, honeycomb_positions, vertical_honeycomb_positions, cell_size, spacing)

if __name__ == "__main__":
    main()

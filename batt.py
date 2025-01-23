import sys
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np


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


def plot_layouts(x_dim, y_dim, grid_positions, honeycomb_positions, cell_size, spacing):
    radius = cell_size / 2
    grid_count = len(grid_positions)
    honeycomb_count = len(honeycomb_positions)

    fig, axs = plt.subplots(2, 1, figsize=(8, 12))

    fig.canvas.manager.set_window_title(f"Grid: {grid_count} cells | Honeycomb: {honeycomb_count} cells")

    axs[0].set_xlim(0, x_dim)
    axs[0].set_ylim(0, y_dim)
    axs[0].set_aspect('equal', adjustable='box')
    for x, y in grid_positions:
        circle = Circle((x, y), radius, edgecolor='blue', facecolor='lightblue', alpha=0.7)
        axs[0].add_artist(circle)
    axs[0].set_title(f"Grid Layout (Total Circles: {grid_count}, Spacing: {spacing})")
    axs[0].set_xlabel("Width")
    axs[0].set_ylabel("Height")
    axs[0].grid(visible=True, linestyle="--", alpha=0.5)

    axs[1].set_xlim(0, x_dim)
    axs[1].set_ylim(0, y_dim)
    axs[1].set_aspect('equal', adjustable='box')
    for x, y in honeycomb_positions:
        circle = Circle((x, y), radius, edgecolor='green', facecolor='lightgreen', alpha=0.7)
        axs[1].add_artist(circle)
    axs[1].set_title(f"Honeycomb Layout (Total Circles: {honeycomb_count}, Spacing: {spacing})")
    axs[1].set_xlabel("Width")
    axs[1].set_ylabel("Height")
    axs[1].grid(visible=True, linestyle="--", alpha=0.5)

    plt.tight_layout()
    plt.show()

    print(f"Grid Layout: {grid_count} circles (Spacing: {spacing})")
    print(f"Honeycomb Layout: {honeycomb_count} circles (Spacing: {spacing})")


def main():
    if len(sys.argv) != 5:
        print("Usage: python3 batt.py <x_dim> <y_dim> <spacing> <cell_size>")
        sys.exit(1)

    x_dim = float(sys.argv[1])
    y_dim = float(sys.argv[2])
    spacing = float(sys.argv[3])
    cell_size = float(sys.argv[4])

    grid_positions = generate_grid_layout(x_dim, y_dim, spacing, cell_size)
    honeycomb_positions = generate_honeycomb_layout(x_dim, y_dim, spacing, cell_size)

    plot_layouts(x_dim, y_dim, grid_positions, honeycomb_positions, cell_size, spacing)


if __name__ == "__main__":
    main()

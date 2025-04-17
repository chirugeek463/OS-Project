import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import matplotlib.pyplot as plt
import time  # To measure execution time with higher precision
from algorithms import fifo_page_replacement, lru_page_replacement, optimal_page_replacement
from analysis import compare_algorithms, export_results
import numpy as np

def visualize_algorithm(history, title):
    """ Improved visualization for memory allocation over time """
    plt.figure(figsize=(10, 6))

    num_frames = max(len(state) for state in history)  # Maximum number of frames
    colors = plt.cm.get_cmap('tab10', num_frames)  # Different colors for each frame slot
    
    for i, state in enumerate(history):
        x_values = [i] * len(state)
        y_values = list(state)

        # Assign distinct colors for each page based on its value
        plt.scatter(x_values, y_values, color=[colors(p % num_frames) for p in state], label=f"Step {i+1}" if i == 0 else "")
        plt.plot(x_values, y_values, color='gray', alpha=0.5, linestyle='dashed')  # Dashed lines for better tracking

    plt.xlabel("Steps (Time)", fontsize=12)
    plt.ylabel("Pages in Frames", fontsize=12)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xticks(range(len(history)))
    plt.yticks(sorted(set(sum(history, []))))  # Unique page numbers
    plt.grid(True, linestyle="--", alpha=0.6)

    plt.legend(["Page Changes"], loc="upper right")
    plt.show()


def run_simulation(entry_pages, entry_frames, algo_var, result_label):
    """Runs the selected page replacement algorithm"""
    try:
        pages = list(map(int, entry_pages.get().split()))  # Get pages from user input
        frame_size = int(entry_frames.get())  # Get number of frames

        if frame_size <= 0:
            messagebox.showerror("Error", "Frame size must be greater than 0")
            return

        algo = algo_var.get()
        
        start_time = time.perf_counter()  # Start time with high precision
        if algo == "FIFO":
            history, faults, _ = fifo_page_replacement(pages, frame_size)
        elif algo == "LRU":
            history, faults, _ = lru_page_replacement(pages, frame_size)
        elif algo == "Optimal":
            history, faults, _ = optimal_page_replacement(pages, frame_size)
        else:
            messagebox.showerror("Error", "Invalid Algorithm Selected")
            return
        exec_time = time.perf_counter() - start_time  # Stop time

        # Calculate hits (Total Requests - Page Faults)
        total_requests = len(pages)
        hits = total_requests - faults

        visualize_algorithm(history, f"{algo} Page Replacement")

        # Update the result label
        result_label.config(
            text=f"Algorithm: {algo}\nPage Faults: {faults}\nHits: {hits}\nExecution Time: {exec_time:.10f} sec"
        )
        result_label.update_idletasks()  # Ensure fast UI update

    except ValueError:
        messagebox.showerror("Error", "Invalid input! Please enter space-separated numbers.")


def run_comparison(entry_pages, entry_frames):
    try:
        pages = list(map(int, entry_pages.get().split()))
        frame_size = int(entry_frames.get())
        compare_algorithms(pages, frame_size)  # Pass user input for comparison
    except ValueError:
        messagebox.showerror("Error", "Invalid input! Enter space-separated numbers.")


def start_gui():
    """Creates the GUI for the page replacement simulator with a modern dark theme and centered layout"""
    root = tk.Tk()
    root.title("Page Replacement Simulator")
    root.geometry("450x350")
    root.configure(bg="#1e1e2e")  # Dark background

    # Styling
    fg_color = "#cdd6f4"  # Light text color
    entry_bg = "#313244"  # Entry background
    button_bg = "#89b4fa"  # Blue buttons
    button_fg = "#1e1e2e"  # Dark text on buttons
    highlight_color = "#94e2d5"  # Green highlight

    style = ttk.Style()
    style.configure("TButton", background=button_bg, foreground=button_fg, font=("Arial", 11), padding=5)
    style.map("TButton", background=[("active", highlight_color)])

    # Center Frame for Better Alignment
    frame = tk.Frame(root, bg=root["bg"])
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Centering the frame

    # Labels and Inputs
    tk.Label(frame, text="Enter Page Reference String:", fg=fg_color, bg=root["bg"], font=("Arial", 11)).grid(row=0, column=0, pady=5, sticky="w")
    entry_pages = tk.Entry(frame, bg=entry_bg, fg=fg_color, insertbackground=fg_color, font=("Arial", 11))
    entry_pages.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(frame, text="Enter Number of Frames:", fg=fg_color, bg=root["bg"], font=("Arial", 11)).grid(row=1, column=0, pady=5, sticky="w")
    entry_frames = tk.Entry(frame, bg=entry_bg, fg=fg_color, insertbackground=fg_color, font=("Arial", 11))
    entry_frames.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(frame, text="Choose Algorithm:", fg=fg_color, bg=root["bg"], font=("Arial", 11)).grid(row=2, column=0, pady=5, sticky="w")
    algo_var = tk.StringVar(value="FIFO")
    algo_menu = ttk.Combobox(frame, textvariable=algo_var, values=["FIFO", "LRU", "Optimal"], font=("Arial", 11), state="readonly")
    algo_menu.grid(row=2, column=1, padx=10, pady=5)

    # Buttons
    ttk.Button(frame, text="Run Simulation", command=lambda: run_simulation(entry_pages, entry_frames, algo_var, result_label)).grid(row=3, columnspan=2, pady=5)
    ttk.Button(frame, text="Compare Algorithms", command=lambda: run_comparison(entry_pages, entry_frames)).grid(row=4, columnspan=2, pady=5)
    ttk.Button(frame, text="Export Results", command=export_results).grid(row=5, columnspan=2, pady=5)

    # Result Label for displaying faults, hits, and execution time
    result_label = tk.Label(frame, text="", fg="#fab387", bg=root["bg"], font=("Arial", 11, "bold"), justify="left")
    result_label.grid(row=6, columnspan=2, pady=10)

    root.mainloop()

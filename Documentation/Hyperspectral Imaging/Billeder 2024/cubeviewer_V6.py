import re
from textwrap import fill
import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import threading
from typing import Literal

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import os

from mpltoolbar import NavigationToolbar2Ttk


# Create a class that inherits from the tkinter.Tk class
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Setup the window
        self.title("Cube Viewer")
        self.geometry("1200x800")
        self.protocol("WM_DELETE_WINDOW", self.quit)
        self.configure(bg='black')
        self.apply_styling()

        self.create_menu()

        # initialize notebook
        self.initialize_notebook()

        # Bind keyboard shortcuts
        self.bind_shortcuts()

    def apply_styling(self):
        style = ttk.Style()
        style.theme_use('default')

        self.style_color = "white"  # Use default background color for TFrame
        self.text_color = 'black'
        # Configure the style for different widget types
        style.configure('TNotebook', background=self.style_color, foreground=self.text_color)
        style.configure('TNotebook.Tab', background=self.style_color, foreground=self.text_color)
        style.configure('TFrame', background=self.style_color)
        style.configure('TLabel', background=self.style_color, foreground=self.text_color)
        style.configure('TButton', background=self.style_color, foreground=self.text_color)
        style.configure('TScale', background=self.style_color, foreground=self.text_color)
        style.configure('TMenu', background=self.style_color, foreground=self.text_color)

        # Configure the style for the selected tab
        style.map('TNotebook.Tab', 
            background=[('selected', self.text_color)],
            foreground=[('selected', self.style_color)])

    def create_menu(self):
        # Create a menu bar
        menubar = tk.Menu(self)
        self.config(menu=menubar)

        # Create a File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open File...", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save as...", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit, accelerator="Ctrl+Q")
        menubar.add_cascade(label="File", menu=file_menu)

        # Create tools menu
        tools_menu = tk.Menu(menubar, tearoff=0)
        tools_menu.add_command(label="Transpose", command=self.transpose)
        tools_menu.add_command(label="Reshape", command=self.reshape)
        tools_menu.add_separator()
        tools_menu.add_command(label="Apply Filter", command=self.apply_filter)
        tools_menu.add_separator()
        # Create a submenu for ROI options
        roi_menu = tk.Menu(tools_menu, tearoff=0)
        roi_menu.add_command(label="Horizontal ROI", command=lambda: self.plot_spectrum(roi_type="Horizontal"))
        roi_menu.add_command(label="Vertical ROI", command=lambda: self.plot_spectrum(roi_type="Vertical"))
        roi_menu.add_command(label="Custom ROI", command=lambda: self.plot_spectrum(roi_type="Custom"))

        # Add the ROI submenu to the tools menu
        tools_menu.add_cascade(label="Plot Spectrum", menu=roi_menu)
        menubar.add_cascade(label="Tools", menu=tools_menu)

        # Add other menus if needed (e.g., Help, Edit)
        help_menu = tk.Menu(menubar, tearoff=0)
        help_menu.add_command(label="About", command=self.show_about)
        menubar.add_cascade(label="Help", menu=help_menu)

    def initialize_notebook(self):
        self.tabs = {}

        # Create a notebook widget
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True)

        # create a context menu that opens when a tab is right clicked
        self.tab_menu = tk.Menu(self.notebook, tearoff=0)

        # Bind the right-click event to the notebook
        self.notebook.bind("<Button-3>", self.on_tab_right_click)

    def on_tab_right_click(self, event):
        # Identify the tab under the cursor
        tab_index = event.widget.index(f"@{event.x},{event.y}")

        # Update the context menu command to delete the right-clicked tab
        self.tab_menu.delete(0, tk.END)  # Clear previous commands
        self.tab_menu.add_command(label="Close", command=lambda: self.delete_tab(tab_index))
        self.tab_menu.add_command(label="Rename", command=lambda: self.rename_tab(tab_index))

        # Display the tab menu when right-clicking on a tab
        self.tab_menu.post(event.x_root, event.y_root)
    
    ##########################################################
    # The following methods are utility methods for the app #
    ##########################################################

    def delete_tab(self, tab_id):
        # Get the text of the tab
        tab_name = self.notebook.tab(tab_id, "text")

        # Destroy the tab
        self.notebook.forget(tab_id)

        # Remove the tab from the tabs dictionary
        self.tabs.pop(tab_name)
    
    def rename_tab(self, tab_id):
        # Get the text of the tab
        tab_name = self.notebook.tab(tab_id, "text")

        # Create a dialog to get the new tab name
        new_tab_name = simpledialog.askstring("Rename Tab", "Enter a new name for the tab", initialvalue=tab_name)

        # check if the user clicked cancel or the string is empyt
        if new_tab_name is None or new_tab_name == "":
            return

        # check if the new tab name already exists
        if new_tab_name in self.tabs:
            tk.messagebox.showerror("Error", f"A tab with the name '{new_tab_name}' already exists.")
            return

        # Update the tab name
        self.notebook.tab(tab_id, text=new_tab_name)
        self.tabs[new_tab_name] = self.tabs.pop(tab_name)
    
    def select_tab(self, tab_name):
        # get tab index by tab name
        tab_index = list(self.tabs.keys()).index(tab_name)
        self.notebook.select(tab_index)

    #########################################################################
    # The following methods are utility methods for generating various tabs #
    #########################################################################
    def add_datacube_tab(self, datacube, tab_name):
        # create a Matplotlib figure
        fig = Figure(figsize=(5, 5), facecolor=self.style_color)
        ax = fig.add_subplot(111)
        
        # display the middle channel as an image
        middle_channel = datacube.shape[2] // 2
        image = ax.imshow(datacube[:, :, middle_channel], cmap='gray', vmin=0, vmax=255)

        # create a Frame to hold the matplotlib figure and a slider widget for channel selection
        tab_frame = ttk.Frame(self.notebook)
        
        # create a close ("X") button to remove the tab
        close_button = ttk.Button(tab_frame, text="X", command=lambda: self.delete_tab(self.notebook.index(tab_frame)))
        close_button.pack(side='top', anchor='e')

        # create a canvas to display the matplotlib figure
        canvas = FigureCanvasTkAgg(fig, master=tab_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)

        # generate the toolbar for the canvas
        toolbar = NavigationToolbar2Ttk(canvas, tab_frame, pack_toolbar=True)
        # apply the custom styling to the toolbar
        toolbar.configure(background=self.style_color)
        toolbar.update()
        
        # create a label to display the current channel value
        channel_value_label = ttk.Label(tab_frame, text=f"Channel: {middle_channel}")
        channel_value_label.pack()

        # create a slider widget to select the channel if the 
        def update_channel(value):
            channel = int(float(value))
            image.set_data(datacube[:, :, channel])
            canvas.draw_idle()
            channel_value_label.config(text=f"Channel: {channel}")
        
        channel_slider = ttk.Scale(tab_frame, from_=0, to=datacube.shape[2] - 1, orient='horizontal', command=lambda value: update_channel(value))
        channel_slider.set(middle_channel)
        channel_slider.pack(fill='x')

        # add the tab to the notebook
        # check if the tab name already exists and if it does at a number to the end
        name, ext = os.path.splitext(tab_name)
        number = 1
        while tab_name in self.tabs:
            tab_name = f"{name} ({number}){ext}"
            number += 1

        self.notebook.add(tab_frame, text=tab_name)
        self.tabs[tab_name] = {'data': datacube, 'fig': fig, 'ax': ax, 'canvas': canvas, 'channel_slider': channel_slider}

        self.notebook.select(tab_frame)
    
    ##########################################################
    # The following methods are callbacks for the tools menu #
    ##########################################################
    def transpose(self):
        # Get the currently selected tab
        tab_index = self.notebook.index(self.notebook.select())
        tab_name = self.notebook.tab(tab_index, "text")
        tab_data = self.tabs[tab_name]

        # Check if the tab is a datacube tab by checking if the if the value for 'data' is at least a 2D numpy array
        if not isinstance(tab_data['data'], np.ndarray) or len(tab_data['data'].shape) < 2:
            tk.messagebox.showerror("Error", "The selected tab does not contain transposable data.")
            return
        
        # Create a pop-up window
        popup = tk.Toplevel(self)
        popup.title("Transpose Dimensions")
        popup.geometry("400x150")
        popup.resizable(False, False)
        popup.configure(bg=self.style_color)

        # Create a label to explain the user how to transpose the data
        instructions = ttk.Label(popup, text="Drag and drop the dimension labels to transpose the data", background=self.style_color)
        instructions.pack(expand=True)

        # Create a frame to hold the dimension labels
        frame = ttk.Frame(popup)
        frame.pack(padx=10, pady=10, expand=True)

        # Create a list to hold the dimension labels
        labels = []

        # Create labels for each dimension
        for i, dim in enumerate(tab_data['data'].shape):
            label = ttk.Label(frame, text=f"axis{i}: {dim}", borderwidth=2, relief="solid")
            label.grid(row=0, column=i, padx=5, pady=5)
            labels.append(label)

        # Make the labels draggable
        def on_drag_start(event, label):
            label.lift()
            self._drag_data = {"x": event.x, "y": event.y, "label": label}
        
        def on_drag_motion(event, label):
            delta_x = event.x - self._drag_data["x"]
            delta_y = event.y - self._drag_data["y"]
            label.place(x=label.winfo_x() + delta_x, y=label.winfo_y() + delta_y)
        
        def on_drag_end(event, label, labels):
            # Get the x position of the dragged label
            label_x = label.winfo_x()

            # Get the x positions of other labels
            grid_positions = [(lbl, lbl.winfo_x()) for lbl in labels if lbl != label]

            # Find the closest position to snap the dragged label
            closest_label, closest_position = min(grid_positions, key=lambda pos: abs(pos[1] - label_x))

            # Get the index of the closest label and move the dragged label there
            closest_index = labels.index(closest_label)

            # Remove the dragged label from its original position
            labels.remove(label)

            # Insert the dragged label into the new position
            labels.insert(closest_index, label)

            # Re-grid all labels according to their new positions
            for i, lbl in enumerate(labels):
                lbl.grid(row=0, column=i, padx=5, pady=5)

            # Reset the placement of the dragged label (if it was placed manually during drag)
            label.place_forget()

        for label in labels:
            label.bind("<Button-1>", lambda e, lbl=label: on_drag_start(e, lbl))
            label.bind("<B1-Motion>", lambda e, lbl=label: on_drag_motion(e, lbl))
            label.bind("<ButtonRelease-1>", lambda e, lbl=label: on_drag_end(e, lbl, labels))

        # Create a button to apply the transpose
        def apply_transpose(tab_name, tab_data, labels, popup):
            # Get the new order of dimensions by extracting the index from the label text
            new_order = [int(label.cget("text").split(":")[0].replace("axis", "")) for label in labels]

            # Transpose the datacube
            transposed_datacube = np.transpose(tab_data['data'], new_order)

            # Add a new tab with the transposed datacube
            self.add_datacube_tab(transposed_datacube, f"{tab_name} (Transposed)")
            self.select_tab(f"{tab_name} (Transposed)")
            popup.destroy()

        apply_button = ttk.Button(popup, text="Apply Transpose", command=lambda: apply_transpose(tab_name, tab_data, labels, popup))
        apply_button.pack(pady=10)

    def reshape(self):
        # Get the currently selected tab
        tab_index = self.notebook.index(self.notebook.select())
        tab_name = self.notebook.tab(tab_index, "text")
        tab_data = self.tabs[tab_name]

        # Check if the tab is a datacube tab by checking if the if the value for 'data' is at least a 2D numpy array
        if not isinstance(tab_data['data'], np.ndarray) or len(tab_data['data'].shape) < 2:
            tk.messagebox.showerror("Error", "The selected tab does not contain reshappable data.")
            return
        
        # Create a pop-up window
        popup = tk.Toplevel(self)
        popup.title("Reshape Data")
        # popup.geometry("400x150")
        # popup.resizable(False, False)
        popup.configure(bg=self.style_color)

        # Create a label to explain the user how to reshape the data
        instructions = ttk.Label(popup, text="Enter the new shape for the data", background=self.style_color)
        instructions.pack(expand=True)

        # Create a frame to hold the entry widgets
        frame = ttk.Frame(popup)
        frame.pack(padx=10, pady=10, expand=True)

        # Create entry widgets for each dimension
        entries = []
        for i, dim in enumerate(tab_data['data'].shape):
            entry = ttk.Entry(frame)
            entry.insert(0, str(dim))
            entry.grid(row=0, column=i, padx=5, pady=5)
            entries.append(entry)

        # Create frame for holding buttons
        button_frame = ttk.Frame(popup)
        button_frame.pack(pady=10)

        # Create a button to add a new axis
        def add_axis():
            entry = ttk.Entry(frame)
            entry.insert(0, "1")  # Default new axis size is 1
            entry.grid(row=0, column=len(entries), padx=5, pady=5)
            entries.append(entry)

        add_axis_button = ttk.Button(button_frame, text="Add Axis", command=add_axis)
        add_axis_button.grid(row=0, column=0, padx=5, pady=5)

        # create a button to remove the last axis
        def remove_axis():
            if len(entries) > 1:
                entry = entries.pop()
                entry.destroy()

        remove_axis_button = ttk.Button(button_frame, text="Remove Axis", command=remove_axis)
        remove_axis_button.grid(row=0, column=1, padx=5, pady=5)


        # Create a button to apply the reshape
        def apply_reshape(tab_name, tab_data, entries, popup):
            # Get the new shape from the entry widgets
            new_shape = tuple(int(entry.get()) for entry in entries)

            # check if the new shape is valid by computing the original size and the new size and comparing them
            original_size = np.prod(tab_data['data'].shape)
            if -1 in new_shape:
                # numpy will automatically calculate the size of the dimension with -1 hence to check if it is valid we need to remove the -1 and check if the modulus (%) of the original size and the new size (ignoring -1) is 0
                new_size = np.prod([dim for dim in new_shape if dim != -1])
                if original_size % new_size != 0:
                    tk.messagebox.showerror("Error", "Invalid shape. The new shape must be compatible with the original shape.")
                    return
            else:
                if original_size != np.prod(new_shape):
                    tk.messagebox.showerror("Error", "Invalid shape. The new shape must have the same number of elements as the original shape.")
                    return


            
            # Reshape the datacube
            reshaped_datacube = np.reshape(tab_data['data'], new_shape)

            print(f"Reshaped datacube shape: {reshaped_datacube.shape}")

            # Add a new tab with the reshaped datacube
            self.add_datacube_tab(reshaped_datacube, f"{tab_name} (Reshaped)")
            self.select_tab(f"{tab_name} (Reshaped)")
            popup.destroy()

        apply_button = ttk.Button(popup, text="Apply Reshape", command=lambda: apply_reshape(tab_name, tab_data, entries, popup))
        apply_button.pack(pady=10)

    def apply_filter(self):
        print("Apply Filter")

    def plot_spectrum(self, roi_type: Literal["Custom", "Horizontal", "Vertical"] = "Custom"):
        print(f"Plot Spectrum ({roi_type})")

    ##########################################################
    # The following methods are callbacks for the File menu  #
    ##########################################################
    def open_file(self, file_path=None):
        if file_path is None:
            # Open a file dialog to select a file. Start in the current directory and allow multiple file types but default is numpy files
            file_path = filedialog.askopenfilename(initialdir='.', filetypes=[('Numpy files', '*.npy'), ('All files', '*.*')])

        if not file_path:
            return
        
        # Process the opened file
        self.process_opened_file(file_path)
    
    def process_opened_file(self, filepath):
        # get the filename and the extension
        filename, file_extension = os.path.splitext(os.path.basename(filepath))
        
        # check the file extension
        match file_extension:
            case '.npy':
                # Load the numpy file
                data = np.load(filepath)
                
                self.add_datacube_tab(data, filename+file_extension)
            case _:
                print(f"Unsupported file type: {file_extension}")
        
    
    def save_file(self):
        # get the currently selected tab
        tab_index = self.notebook.index(self.notebook.select())
        tab_name = self.notebook.tab(tab_index, "text")
        tab_data = self.tabs[tab_name]

        # split the tab name by " " to get rid of any additional information such as (transposed)
        tab_name = tab_name.split(" ")[0]


        # Open a file dialog to select a file
        file_path = filedialog.asksaveasfilename(initialdir='.', initialfile=tab_name, filetypes=[('Numpy files', '*.npy'), ('All files', '*.*')])
        if not file_path:
            return
        
        # Save the data to the selected file in a separate thread
        def save_data(file_path, data):
            np.save(file_path, data)
            print(f"Data saved to {file_path}")
        thread = threading.Thread(target=save_data, args=(file_path, tab_data['data']))
        thread.start()


    def show_about(self):
        # Show an About dialog (placeholder)
        messagebox.showinfo("About", "Cube Viewer v1.0")

    def quit(self):
        # Quit the application
        self.destroy()

    def bind_shortcuts(self):
        # Bind keyboard shortcuts
        self.bind("<Control-s>", lambda event: self.save_file())
        self.bind("<Control-o>", lambda event: self.open_file())
        self.bind("<Control-q>", lambda event: self.quit())

if __name__ == '__main__':
    app = App()
    app.mainloop()

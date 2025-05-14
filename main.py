from tkinter import *
from tkinter import PhotoImage
import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import colorchooser

def resize_image(path, width, height):
    img = Image.open(path).convert("RGBA")
    resized = img.resize((width, height), Image.Resampling.LANCZOS)
    return ImageTk.PhotoImage(resized)

window = Tk()
window.title("Laboratory #5")
window.geometry("1024x768")
window.configure(bg="#000082")
window.resizable(False,False)

def open_fake_app():
    print("Launching app...")

def open_calculator():
    calc_window = Toplevel()
    calc_window.title("Calculator")
    calc_window.geometry("240x400")
    calc_window.resizable(False, False)

    expression = ""

    def press(num):
        nonlocal expression
        expression += str(num)
        equation.set(expression)

    def clear():
        nonlocal expression
        expression = ""
        equation.set("")

    def equalpress():
        nonlocal expression
        try:
            total = str(eval(expression))
            equation.set(total)
            expression = total
        except:
            equation.set("error")
            expression = ""

    equation = StringVar()

    entry_field = Entry(calc_window, textvariable=equation, font=("Tahoma", 20), bd=10, insertwidth=2, width=14, borderwidth=4, relief="ridge", justify="right")
    entry_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ]

    for (text, row, col) in buttons:
        action = equalpress if text == '=' else lambda t=text: press(t)
        Button(calc_window, text=text, padx=20, pady=20, font=("Tahoma", 12), command=action).grid(row=row, column=col)

    Button(calc_window, text='C', padx=20, pady=20, font=("Tahoma", 12), command=clear).grid(row=5, column=0, columnspan=4, sticky="we")

def open_explorer():
    explorer_window = Toplevel()
    explorer_window.title("File Explorer")
    explorer_window.geometry("800x600")
    explorer_window.configure(bg="white")

    # Create a frame for tabs
    tab_frame = Frame(explorer_window, bg="#f0f0f0", height=30)
    tab_frame.pack(side=TOP, fill=X)

    # Create tabs
    tabs = ["Documents", "Pictures", "Downloads", "Music"]
    active_tab = StringVar(value=tabs[0])

    for i, tab in enumerate(tabs):
        if tab == active_tab.get():
            tab_button = Label(
                tab_frame,
                text=tab,
                bg="white",
                padx=15,
                pady=5,
                borderwidth=1,
                relief="solid"
            )
        else:
            tab_button = Label(
                tab_frame,
                text=tab,
                bg="#f0f0f0",
                padx=15,
                pady=5
            )
            tab_button.bind("<Button-1>", lambda e, t=tab: change_tab(t))
        tab_button.pack(side=LEFT)

    # Create a frame for navigation buttons
    nav_frame = Frame(explorer_window, bg="#f0f0f0", height=40)
    nav_frame.pack(side=TOP, fill=X)

    # Back, Forward, Up buttons
    back_btn = Button(nav_frame, text="←", width=3, bg="#f0f0f0", relief="flat")
    back_btn.pack(side=LEFT, padx=5, pady=5)

    forward_btn = Button(nav_frame, text="→", width=3, bg="#f0f0f0", relief="flat")
    forward_btn.pack(side=LEFT, padx=5, pady=5)

    up_btn = Button(nav_frame, text="↑", width=3, bg="#f0f0f0", relief="flat")
    up_btn.pack(side=LEFT, padx=5, pady=5)

    # Address bar
    address_var = StringVar(value="C:\\Users\\User\\Documents")
    address_bar = Entry(nav_frame, textvariable=address_var, bg="white", relief="solid", bd=1)
    address_bar.pack(side=LEFT, fill=X, expand=True, padx=5, pady=5)

    # Create a frame for sidebar and content
    main_frame = Frame(explorer_window, bg="white")
    main_frame.pack(side=TOP, fill=BOTH, expand=True)

    # Create sidebar
    sidebar_frame = Frame(main_frame, bg="#f0f0f0", width=200)
    sidebar_frame.pack(side=LEFT, fill=Y)
    sidebar_frame.pack_propagate(False)

    # Sidebar items
    sidebar_items = [
        ("Quick access", ""),
        ("This PC", ""),
        ("Network", ""),
        ("OneDrive", "")
    ]

    for item, _ in sidebar_items:
        btn = Label(sidebar_frame, text=item, bg="#f0f0f0", anchor="w", padx=10, pady=8)
        btn.pack(side=TOP, fill=X)
        btn.bind("<Enter>", lambda e, b=btn: b.config(bg="#e0e0e0"))
        btn.bind("<Leave>", lambda e, b=btn: b.config(bg="#f0f0f0"))

    # Create content area
    content_frame = Frame(main_frame, bg="white")
    content_frame.pack(side=LEFT, fill=BOTH, expand=True)

    # Sample files data
    files_data = {
        "Documents": [
            {"name": "Project_Report.docx", "type": "Word Document", "size": "45 KB", "date": "2025-04-15"},
            {"name": "Budget_2025.xlsx", "type": "Excel Spreadsheet", "size": "28 KB", "date": "2025-04-10"},
            {"name": "Meeting_Notes.txt", "type": "Text Document", "size": "3 KB", "date": "2025-04-22"},
            {"name": "Presentation.pptx", "type": "PowerPoint", "size": "1.2 MB", "date": "2025-04-05"},
            {"name": "ReadMe.md", "type": "Markdown", "size": "2 KB", "date": "2025-04-18"}
        ],
        "Pictures": [
            {"name": "Vacation.jpg", "type": "JPEG Image", "size": "2.5 MB", "date": "2025-03-15"},
            {"name": "Screenshot.png", "type": "PNG Image", "size": "340 KB", "date": "2025-04-20"},
            {"name": "Profile_Picture.jpg", "type": "JPEG Image", "size": "450 KB", "date": "2025-02-10"},
            {"name": "Wallpaper.jpg", "type": "JPEG Image", "size": "1.8 MB", "date": "2025-01-05"}
        ],
        "Downloads": [
            {"name": "Setup.exe", "type": "Application", "size": "15.6 MB", "date": "2025-04-23"},
            {"name": "Music_Album.zip", "type": "ZIP Archive", "size": "45.2 MB", "date": "2025-04-18"},
            {"name": "E-book.pdf", "type": "PDF Document", "size": "3.4 MB", "date": "2025-04-05"}
        ],
        "Music": [
            {"name": "Song1.mp3", "type": "MP3 Audio", "size": "4.5 MB", "date": "2025-03-12"},
            {"name": "Album.mp3", "type": "MP3 Audio", "size": "12.8 MB", "date": "2025-02-28"},
            {"name": "Podcast.mp3", "type": "MP3 Audio", "size": "25.7 MB", "date": "2025-04-01"}
        ]
    }

    # File list header
    header_frame = Frame(content_frame, bg="#f0f0f0", height=30)
    header_frame.pack(side=TOP, fill=X)

    # Headers
    headers = ["Name", "Type", "Size", "Date modified"]
    weights = [3, 2, 1, 2]  # Relative widths

    for i, header in enumerate(headers):
        header_label = Label(header_frame, text=header, bg="#f0f0f0", anchor="w", padx=10)
        header_label.grid(row=0, column=i, sticky="ew")
        header_frame.grid_columnconfigure(i, weight=weights[i])

    # Files listbox with scrollbar
    list_frame = Frame(content_frame, bg="white")
    list_frame.pack(side=TOP, fill=BOTH, expand=True)

    # Create a canvas for scrolling
    canvas = Canvas(list_frame, bg="white", highlightthickness=0)
    scrollbar = Scrollbar(list_frame, orient="vertical", command=canvas.yview)
    scrollable_frame = Frame(canvas, bg="white")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Add files to the list
    current_files = files_data[active_tab.get()]

    for i, file in enumerate(current_files):
        row_bg = "#f9f9f9" if i % 2 == 0 else "white"
        row_frame = Frame(scrollable_frame, bg=row_bg)
        row_frame.pack(fill=X, expand=True)

        # File name with icon (using emoji as placeholder)
        icon = "📄" if not file["name"].endswith((".jpg", ".png")) else "🖼️"
        if file["name"].endswith(".mp3"):
            icon = "🎵"
        elif file["name"].endswith((".zip", ".rar")):
            icon = "🗜️"
        elif file["name"].endswith(".exe"):
            icon = "⚙️"

        name_label = Label(row_frame, text=f"{icon} {file['name']}", bg=row_bg, anchor="w", padx=10, pady=5)
        name_label.grid(row=0, column=0, sticky="ew")

        # Bind double-click to open file
        name_label.bind("<Double-1>", lambda e, f=file: open_file(explorer_window, f))

        # Type
        type_label = Label(row_frame, text=file["type"], bg=row_bg, anchor="w", padx=10, pady=5)
        type_label.grid(row=0, column=1, sticky="ew")

        # Size
        size_label = Label(row_frame, text=file["size"], bg=row_bg, anchor="w", padx=10, pady=5)
        size_label.grid(row=0, column=2, sticky="ew")

        # Date
        date_label = Label(row_frame, text=file["date"], bg=row_bg, anchor="w", padx=10, pady=5)
        date_label.grid(row=0, column=3, sticky="ew")

        # Configure grid columns to match header
        for j, weight in enumerate(weights):
            row_frame.grid_columnconfigure(j, weight=weight)

        # Highlight on hover
        widgets = [name_label, type_label, size_label, date_label, row_frame]
        for widget in widgets:
            widget.bind("<Enter>", lambda e, rf=row_frame, w=widgets: highlight_row(rf, w, "#e5f3ff"))
            widget.bind("<Leave>", lambda e, rf=row_frame, w=widgets, bg=row_bg: highlight_row(rf, w, bg))

    # Define functions to use in the file explorer
    def highlight_row(row_frame, widgets, color):
        """Highlight an entire row"""
        row_frame.config(bg=color)
        for widget in widgets:
            if isinstance(widget, Label):
                widget.config(bg=color)

    def change_tab(tab_name):
        """Change the active tab and update file list"""
        active_tab.set(tab_name)
        # In a real implementation, this would update the file list
        # For now, we just print the tab change
        print(f"Changed to tab: {tab_name}")

        # Clear the current file list
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        # Reload with new tab's files
        new_files = files_data[tab_name]

        # Update address bar
        address_var.set(f"C:\\Users\\User\\{tab_name}")

        # Repopulate file list
        for i, file in enumerate(new_files):
            row_bg = "#f9f9f9" if i % 2 == 0 else "white"
            row_frame = Frame(scrollable_frame, bg=row_bg)
            row_frame.pack(fill=X, expand=True)

            # File name with icon
            icon = "📄" if not file["name"].endswith((".jpg", ".png")) else "🖼️"
            if file["name"].endswith(".mp3"):
                icon = "🎵"
            elif file["name"].endswith((".zip", ".rar")):
                icon = "🗜️"
            elif file["name"].endswith(".exe"):
                icon = "⚙️"

            name_label = Label(row_frame, text=f"{icon} {file['name']}", bg=row_bg, anchor="w", padx=10, pady=5)
            name_label.grid(row=0, column=0, sticky="ew")

            # Bind double-click
            name_label.bind("<Double-1>", lambda e, f=file: open_file(explorer_window, f))

            # Type
            type_label = Label(row_frame, text=file["type"], bg=row_bg, anchor="w", padx=10, pady=5)
            type_label.grid(row=0, column=1, sticky="ew")

            # Size
            size_label = Label(row_frame, text=file["size"], bg=row_bg, anchor="w", padx=10, pady=5)
            size_label.grid(row=0, column=2, sticky="ew")

            # Date
            date_label = Label(row_frame, text=file["date"], bg=row_bg, anchor="w", padx=10, pady=5)
            date_label.grid(row=0, column=3, sticky="ew")

            # Configure grid
            for j, weight in enumerate(weights):
                row_frame.grid_columnconfigure(j, weight=weight)

            # Highlight on hover
            widgets = [name_label, type_label, size_label, date_label, row_frame]
            for widget in widgets:
                widget.bind("<Enter>", lambda e, rf=row_frame, w=widgets: highlight_row(rf, w, "#e5f3ff"))
                widget.bind("<Leave>", lambda e, rf=row_frame, w=widgets, bg=row_bg: highlight_row(rf, w, bg))

    def open_file(parent, file):
        """Open a mock file in a new window"""
        file_window = Toplevel(parent)
        file_window.title(file["name"])
        file_window.geometry("600x400")
        file_window.configure(bg="white")

        # Menu bar for the file window
        menu_bar = Frame(file_window, bg="#f0f0f0", height=30)
        menu_bar.pack(side=TOP, fill=X)

        menu_items = ["File", "Edit", "View", "Help"]
        for item in menu_items:
            menu_btn = Label(menu_bar, text=item, bg="#f0f0f0", padx=10, pady=5)
            menu_btn.pack(side=LEFT)
            menu_btn.bind("<Enter>", lambda e, b=menu_btn: b.config(bg="#e0e0e0"))
            menu_btn.bind("<Leave>", lambda e, b=menu_btn: b.config(bg="#f0f0f0"))

        # Toolbar
        toolbar = Frame(file_window, bg="#f9f9f9", height=40)
        toolbar.pack(side=TOP, fill=X)

        tool_buttons = ["Save", "Print", "Find"]
        for btn_text in tool_buttons:
            tool_btn = Button(toolbar, text=btn_text, bg="#f9f9f9", relief="flat")
            tool_btn.pack(side=LEFT, padx=5, pady=5)

        # Content based on file type
        content_frame = Frame(file_window, bg="white", padx=10, pady=10)
        content_frame.pack(side=TOP, fill=BOTH, expand=True)

        if file["name"].endswith((".txt", ".md")):
            # Text file
            text_content = Text(content_frame, wrap=WORD, bg="white", relief="flat")
            text_content.pack(fill=BOTH, expand=True)

            # Sample content based on file name
            if "Meeting" in file["name"]:
                sample_text = """# Meeting Notes - April 22, 2025

Attendees:
- John Smith
- Jane Doe
- Michael Johnson
- Sarah Williams

## Agenda
1. Project Status Update
2. Budget Review
3. Timeline Adjustments
4. Open Discussion

## Key Points
- Project is currently on track for June delivery
- Budget is within 5% of projections
- Need to address potential delay in UI components
- Team morale is good, but workload concerns noted

## Action Items
- John to follow up with dev team about UI timeline
- Sarah to prepare revised budget for next meeting
- Michael to coordinate with external vendors
- All to review project documents by Friday

Next meeting scheduled for April 29, 2025."""
            elif "ReadMe" in file["name"]:
                sample_text = """# Project Documentation

## Overview
This project aims to create an intuitive mini operating system interface using Python and Tkinter.

## Features
- Desktop environment with icons
- Mock file explorer
- Simple applications
- Window management

## Requirements
- Python 3.8+
- Tkinter
- Pillow library for image processing

## Installation
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run main.py: `python main.py`

## Usage
Click on desktop icons to launch applications. Files can be browsed through the explorer.

## Development
This is a work in progress. Contributions welcome!"""
            else:
                sample_text = f"This is the content of {file['name']}.\n\nThis is a read-only mock file for demonstration purposes.\n\nDouble-click on other files to see different content formats."

            text_content.insert("1.0", sample_text)
            text_content.config(state=DISABLED)  # Make read-only

        elif file["name"].endswith((".docx", ".xlsx", ".pptx")):
            # Office document
            canvas = Canvas(content_frame, bg="white", highlightthickness=0)
            canvas.pack(fill=BOTH, expand=True)

            # Display placeholder content
            canvas.create_text(
                300, 50,
                text=f"{file['name']} - {file['type']}",
                font=("Tahoma", 16, "bold")
            )

            if "Excel" in file["type"]:
                # Mock spreadsheet
                cell_width = 80
                cell_height = 25

                # Draw grid
                for i in range(15):  # Rows
                    canvas.create_text(20, 100 + i * cell_height, text=str(i + 1), anchor="w")
                    for j in range(6):  # Columns
                        if i == 0:
                            # Column headers
                            canvas.create_text(
                                60 + j * cell_width,
                                100,
                                text=chr(65 + j),
                                font=("Tahoma", 10, "bold")
                            )

                        # Cell borders
                        canvas.create_rectangle(
                            40 + j * cell_width,
                            110 + i * cell_height,
                            40 + (j + 1) * cell_width,
                            110 + (i + 1) * cell_height,
                            outline="#d0d0d0"
                        )

                # Sample data
                budget_data = [
                    ["Category", "Q1", "Q2", "Q3", "Q4", "Total"],
                    ["Hardware", "$2,500", "$1,800", "$3,200", "$2,000", "=SUM(B2:E2)"],
                    ["Software", "$1,200", "$1,500", "$1,000", "$1,800", "=SUM(B3:E3)"],
                    ["Services", "$3,000", "$2,500", "$2,800", "$3,500", "=SUM(B4:E4)"],
                    ["Other", "$500", "$600", "$450", "$700", "=SUM(B5:E5)"],
                    ["Total", "=SUM(B2:B5)", "=SUM(C2:C5)", "=SUM(D2:D5)", "=SUM(E2:E5)", "=SUM(F2:F5)"]
                ]

                # Display sample data
                for i, row in enumerate(budget_data):
                    for j, cell in enumerate(row):
                        cell_color = "#f0f0f0" if i == 0 or j == 0 or i == len(budget_data) - 1 or j == len(
                            row) - 1 else "white"

                        # Fill cell background
                        canvas.create_rectangle(
                            40 + j * cell_width,
                            110 + i * cell_height,
                            40 + (j + 1) * cell_width,
                            110 + (i + 1) * cell_height,
                            fill=cell_color,
                            outline="#d0d0d0"
                        )

                        # Cell text
                        canvas.create_text(
                            50 + j * cell_width,
                            120 + i * cell_height,
                            text=cell,
                            anchor="w",
                            font=("Tahoma", 9, "bold" if i == 0 or j == 0 else "normal")
                        )

            elif "PowerPoint" in file["type"]:
                # Mock presentation
                canvas.create_rectangle(50, 100, 550, 350, fill="#f9f9f9", outline="#d0d0d0")
                canvas.create_text(300, 150, text="Presentation Title", font=("Tahoma", 18, "bold"))
                canvas.create_text(300, 200, text="Subtitle or additional information", font=("Tahoma", 14))
                canvas.create_text(300, 250, text="• Bullet point 1", font=("Tahoma", 12), anchor="w")
                canvas.create_text(300, 280, text="• Bullet point 2", font=("Tahoma", 12), anchor="w")
                canvas.create_text(300, 310, text="• Bullet point 3", font=("Tahoma", 12), anchor="w")

                # Slide navigation
                canvas.create_rectangle(250, 380, 350, 400, fill="#e0e0e0", outline="#c0c0c0")
                canvas.create_text(300, 390, text="Slide 1 / 5")

            else:  # Word document
                canvas.create_rectangle(50, 100, 550, 380, fill="white", outline="#d0d0d0")

                # Mock Word document content
                canvas.create_text(
                    300, 150,
                    text="Project Report",
                    font=("Tahoma", 18, "bold"),
                    anchor="center"
                )

                report_text = """
                This document contains the project report for Q1 2025.

                The team has made significant progress on all major milestones
                and is currently ahead of schedule. Budget utilization is at 45%,
                which is in line with projections.

                Key achievements:
                • Completed core architecture design
                • Deployed test environment
                • Finalized vendor contracts
                • Conducted initial user testing

                Next steps include finalizing the database schema and 
                beginning development of the user interface components.
                """

                canvas.create_text(
                    300, 250,
                    text=report_text,
                    width=450,
                    font=("Tahoma", 11),
                    anchor="center",
                    justify="left"
                )

        elif file["name"].endswith((".jpg", ".png")):
            # Image file
            canvas = Canvas(content_frame, bg="white", highlightthickness=0)
            canvas.pack(fill=BOTH, expand=True)

            # Draw placeholder image
            if "Vacation" in file["name"]:
                canvas.create_rectangle(100, 50, 500, 350, fill="#87CEEB", outline="")
                # Sun
                canvas.create_oval(400, 80, 450, 130, fill="#FFD700", outline="")
                # Sand
                canvas.create_rectangle(100, 250, 500, 350, fill="#F4A460", outline="")
                # Sea
                canvas.create_rectangle(100, 180, 500, 250, fill="#1E90FF", outline="")
                # Palm tree
                canvas.create_rectangle(150, 180, 170, 250, fill="#8B4513", outline="")
                canvas.create_oval(120, 140, 200, 200, fill="#32CD32", outline="")
                # Caption
                canvas.create_text(300, 380, text="Vacation.jpg - Tropical Beach Scene", font=("Tahoma", 12))

            elif "Screenshot" in file["name"]:
                # Simulate a screenshot
                canvas.create_rectangle(100, 50, 500, 350, fill="#f0f0f0", outline="#d0d0d0")

                # Mock toolbar
                canvas.create_rectangle(100, 50, 500, 80, fill="#e0e0e0", outline="#d0d0d0")
                for i in range(5):
                    canvas.create_oval(120 + i * 30, 65, 135 + i * 30, 80, fill="#c0c0c0", outline="")

                # Mock content
                canvas.create_rectangle(120, 100, 480, 140, fill="white", outline="#d0d0d0")
                canvas.create_rectangle(120, 160, 480, 200, fill="white", outline="#d0d0d0")
                canvas.create_rectangle(120, 220, 480, 260, fill="white", outline="#d0d0d0")
                canvas.create_rectangle(120, 280, 480, 320, fill="white", outline="#d0d0d0")

                # Caption
                canvas.create_text(300, 380, text="Screenshot.png - Application Interface", font=("Tahoma", 12))

            else:
                # Generic image placeholder
                canvas.create_rectangle(150, 100, 450, 300, fill="#f0f0f0", outline="#d0d0d0")
                canvas.create_line(150, 100, 450, 300, fill="#d0d0d0")
                canvas.create_line(450, 100, 150, 300, fill="#d0d0d0")
                canvas.create_text(300, 200, text="Image Preview", font=("Tahoma", 14))
                canvas.create_text(300, 380, text=f"{file['name']} - {file['size']}", font=("Tahoma", 12))

        elif file["name"].endswith(".pdf"):
            # PDF document
            canvas = Canvas(content_frame, bg="white", highlightthickness=0)
            canvas.pack(fill=BOTH, expand=True)

            # PDF icon
            canvas.create_rectangle(250, 50, 350, 110, fill="#FF0000", outline="")
            canvas.create_text(300, 80, text="PDF", fill="white", font=("Tahoma", 20, "bold"))

            # Mock PDF content
            y_pos = 150
            for i in range(5):
                # Page outline
                canvas.create_rectangle(100, y_pos, 500, y_pos + 60, fill="white", outline="#d0d0d0")

                # Text lines
                for j in range(3):
                    line_length = 350 - (j * 50) if i < 4 else 200
                    canvas.create_line(120, y_pos + 15 + j * 15, 120 + line_length, y_pos + 15 + j * 15, fill="#d0d0d0")

                y_pos += 70

            # Page numbers
            canvas.create_text(300, 380, text="Page 1 of 15", font=("Tahoma", 10))

        elif file["name"].endswith(".mp3"):
            # Audio file
            canvas = Canvas(content_frame, bg="white", highlightthickness=0)
            canvas.pack(fill=BOTH, expand=True)

            # Audio player interface
            canvas.create_rectangle(100, 150, 500, 250, fill="#f0f0f0", outline="#d0d0d0")

            # Play button
            canvas.create_oval(140, 185, 170, 215, fill="#4CAF50", outline="")
            canvas.create_polygon(150, 190, 150, 210, 165, 200, fill="white", outline="")

            # Track info
            track_name = file["name"].replace(".mp3", "")
            canvas.create_text(300, 180, text=track_name, font=("Tahoma", 14, "bold"))
            canvas.create_text(300, 200, text="00:00 / 03:45", font=("Tahoma", 10))

            # Progress bar
            canvas.create_rectangle(200, 220, 400, 230, fill="white", outline="#d0d0d0")
            canvas.create_rectangle(200, 220, 250, 230, fill="#1E90FF", outline="")

            # Volume
            canvas.create_text(450, 195, text="Volume", font=("Tahoma", 8))
            canvas.create_rectangle(420, 210, 480, 215, fill="white", outline="#d0d0d0")
            canvas.create_rectangle(420, 210, 460, 215, fill="#1E90FF", outline="")

        elif file["name"].endswith((".zip", ".rar")):
            # Archive file
            scrollable_text = Text(content_frame, wrap=WORD, bg="white", relief="flat")
            scrollable_text.pack(fill=BOTH, expand=True)

            # Sample archive contents
            archive_contents = """Archive: Music_Album.zip
Size: 45.2 MB
Modified: 2025-04-18

Contents:
---------
Track01.mp3      4.5 MB
Track02.mp3      4.2 MB
Track03.mp3      5.1 MB
Track04.mp3      3.9 MB
Track05.mp3      4.7 MB
Track06.mp3      4.0 MB
Track07.mp3      4.8 MB
Track08.mp3      5.2 MB
Track09.mp3      4.3 MB
Track10.mp3      4.5 MB
album_info.txt   12 KB
cover.jpg        420 KB

Compression ratio: 1.8:1
"""
            scrollable_text.insert("1.0", archive_contents)
            scrollable_text.config(state=DISABLED)  # Make read-only

        elif file["name"].endswith(".exe"):
            # Executable file
            frame = Frame(content_frame, bg="white")
            frame.pack(expand=True)

            # Application icon
            app_icon_frame = Frame(frame, bg="white", padx=20, pady=20)
            app_icon_frame.pack()

            app_icon = Label(app_icon_frame, text="⚙️", font=("Tahoma", 48))
            app_icon.pack()

            Label(frame, text="Setup.exe", font=("Tahoma", 16, "bold")).pack(pady=10)
            Label(frame, text="Application Installer", font=("Tahoma", 12)).pack()
            Label(frame, text="Version: 1.0.5", font=("Tahoma", 10)).pack(pady=5)
            Label(frame, text="Size: 15.6 MB", font=("Tahoma", 10)).pack()

            # Mock installation buttons
            button_frame = Frame(frame, bg="white", pady=20)
            button_frame.pack()

            Button(button_frame, text="Install", width=10, bg="#4CAF50", fg="white").pack(side=LEFT, padx=5)
            Button(button_frame, text="Cancel", width=10).pack(side=LEFT, padx=5)

            # Installation options
            options_frame = Frame(frame, bg="white", pady=10)
            options_frame.pack()

            Label(options_frame, text="Installation Options:", font=("Tahoma", 10, "bold")).pack(anchor="w")

            # Checkboxes
            var1 = IntVar(value=1)
            var2 = IntVar(value=1)
            var3 = IntVar(value=0)

            Checkbutton(options_frame, text="Create Desktop Shortcut", variable=var1, bg="white").pack(anchor="w")
            Checkbutton(options_frame, text="Add to Start Menu", variable=var2, bg="white").pack(anchor="w")
            Checkbutton(options_frame, text="Run at Startup", variable=var3, bg="white").pack(anchor="w")

        # Status bar for the file window
        status_bar = Frame(file_window, bg="#f0f0f0", height=25)
        status_bar.pack(side=BOTTOM, fill=X)

        Label(status_bar, text=f"File info: {file['name']} • {file['size']} • Last modified: {file['date']}",
              bg="#f0f0f0", anchor="w", padx=10, pady=3).pack(side=LEFT)

    # Status bar for explorer window
    status_bar = Frame(explorer_window, bg="#f0f0f0", height=25)
    status_bar.pack(side=BOTTOM, fill=X)

    files_count = len(current_files)
    Label(status_bar, text=f"{files_count} items", bg="#f0f0f0", anchor="w", padx=10, pady=3).pack(side=LEFT)

    # Make explorer window responsive
    explorer_window.update_idletasks()
    explorer_window.focus_set()

    # Recalculate canvas scroll region
    canvas.configure(scrollregion=canvas.bbox("all"))

def open_paint():
    from tkinter import colorchooser

    paint_window = Toplevel()
    paint_window.title("Paint")
    paint_window.geometry("800x600")
    paint_window.configure(bg="#f0f0f0")

    # Variables for the paint program
    current_color = "#000000"  # Default color is black
    brush_size = 2  # Default brush size
    last_x, last_y = None, None
    is_drawing = False

    # Define functions first so they can be referenced
    def start_drawing(event):
        nonlocal last_x, last_y, is_drawing
        last_x, last_y = event.x, event.y
        is_drawing = True

    def draw(event):
        nonlocal last_x, last_y
        if is_drawing:
            x, y = event.x, event.y
            # Draw line from last position to current position
            drawing_canvas.create_line(
                last_x, last_y, x, y,
                fill=current_color,
                width=brush_size,
                capstyle=ROUND,  # Round ends of lines
                smooth=TRUE,  # Smooth lines
                splinesteps=36  # More steps = smoother curve
            )
            # Update last position
            last_x, last_y = x, y

            # Update cursor position in status bar
            cursor_position_label.config(text=f"Position: {x}, {y}")

    def stop_drawing(event):
        nonlocal is_drawing
        is_drawing = False
        last_x, last_y = None, None

    def change_color(new_color):
        nonlocal current_color
        current_color = new_color
        color_indicator.config(bg=current_color)

    def change_brush_size(size):
        nonlocal brush_size
        brush_size = int(float(size))

    def clear_canvas():
        drawing_canvas.delete("all")  # Clear all drawings

    def pick_custom_color():
        # Using a simple color chooser dialog
        color = colorchooser.askcolor(initialcolor=current_color)
        if color[1]:  # If a color was selected (not canceled)
            change_color(color[1])

    def update_cursor_position(event):
        cursor_position_label.config(text=f"Position: {event.x}, {event.y}")

    # Create main frames
    top_frame = Frame(paint_window, bg="#f0f0f0", height=50)
    top_frame.pack(side=TOP, fill=X)

    # Create canvas for drawing
    canvas_frame = Frame(paint_window, bg="white")
    canvas_frame.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=10)

    drawing_canvas = Canvas(canvas_frame, bg="white", highlightthickness=1, highlightbackground="#d0d0d0")
    drawing_canvas.pack(fill=BOTH, expand=True)

    # Color picker frame
    color_frame = Frame(top_frame, bg="#f0f0f0")
    color_frame.pack(side=LEFT, padx=10, pady=5)

    Label(color_frame, text="Colors:", bg="#f0f0f0").pack(side=LEFT, padx=5)

    # Common colors
    colors = [
        "#000000",  # Black
        "#FFFFFF",  # White
        "#FF0000",  # Red
        "#00FF00",  # Green
        "#0000FF",  # Blue
        "#FFFF00",  # Yellow
        "#FF00FF",  # Magenta
        "#00FFFF",  # Cyan
        "#FFA500",  # Orange
        "#800080",  # Purple
        "#A52A2A",  # Brown
        "#808080",  # Gray
    ]

    # Current color indicator
    color_indicator = Canvas(color_frame, width=30, height=30, bg=current_color, highlightthickness=1,
                             highlightbackground="#000000")
    color_indicator.pack(side=LEFT, padx=10)

    # Color buttons
    color_buttons_frame = Frame(color_frame, bg="#f0f0f0")
    color_buttons_frame.pack(side=LEFT)

    color_swatches = []

    # Create a grid of color buttons
    for i, color in enumerate(colors):
        row, col = divmod(i, 6)

        # Create a small canvas to represent the color
        swatch = Canvas(color_buttons_frame, width=15, height=15, bg=color, highlightthickness=1,
                        highlightbackground="#000000")
        swatch.grid(row=row, column=col, padx=2, pady=2)
        swatch.bind("<Button-1>", lambda event, c=color: change_color(c))

        color_swatches.append(swatch)

    # Tools frame
    tools_frame = Frame(top_frame, bg="#f0f0f0")
    tools_frame.pack(side=LEFT, padx=20, pady=5)

    Label(tools_frame, text="Brush Size:", bg="#f0f0f0").pack(side=LEFT, padx=5)

    # Brush size slider
    size_slider = Scale(
        tools_frame,
        from_=1,
        to=20,
        orient=HORIZONTAL,
        length=100,
        bg="#f0f0f0",
        highlightthickness=0,
        command=lambda val: change_brush_size(val)
    )
    size_slider.set(brush_size)
    size_slider.pack(side=LEFT, padx=5)

    # Custom color button
    custom_color_button = Button(color_frame, text="Custom Color", command=pick_custom_color)
    custom_color_button.pack(side=LEFT, padx=10)

    # Clear button
    clear_button = Button(top_frame, text="Clear Canvas", command=clear_canvas)
    clear_button.pack(side=RIGHT, padx=20, pady=10)

    # Status bar for cursor position
    status_bar = Frame(paint_window, bg="#f0f0f0", height=25)
    status_bar.pack(side=BOTTOM, fill=X)

    cursor_position_label = Label(status_bar, text="Position: 0, 0", bg="#f0f0f0", anchor="w", padx=10, pady=3)
    cursor_position_label.pack(side=LEFT)

    # Bind mouse events to the canvas
    drawing_canvas.bind("<Button-1>", start_drawing)
    drawing_canvas.bind("<B1-Motion>", draw)
    drawing_canvas.bind("<ButtonRelease-1>", stop_drawing)
    drawing_canvas.bind("<Motion>", update_cursor_position)

    # Make sure the window gets focus
    paint_window.focus_set()

    # Prevent the window from being resized below minimum dimensions
    paint_window.update_idletasks()
    paint_window.minsize(400, 300)

def open_wordpad():
    wordpad_window = Toplevel()
    wordpad_window.title("WordPad")
    wordpad_window.geometry("600x500")
    wordpad_window.resizable(False, False)

    text_area = Text(wordpad_window, wrap="word", font=("Tahoma", 12))
    text_area.pack(expand=True, fill="both", padx=5, pady=5)

def power_toggle():
    lock_frame = Frame(window, bg="#003399", width=1024, height=768)  # Windows XP blue
    lock_frame.place(x=0, y=0)

    Label(lock_frame, text="Welcome", fg="white", bg="#003399",
          font=("Segoe UI", 28, "bold")).place(x=440, y=150)

    Label(lock_frame, text="Username:", fg="white", bg="#003399",
          font=("Segoe UI", 14)).place(x=360, y=250)
    username_entry = Entry(lock_frame, font=("Segoe UI", 14), width=20)
    username_entry.place(x=470, y=250)

    Label(lock_frame, text="Password:", fg="white", bg="#003399",
          font=("Segoe UI", 14)).place(x=360, y=300)
    password_entry = Entry(lock_frame, show="*", font=("Segoe UI", 14), width=20)
    password_entry.place(x=470, y=300)

    def attempt_login():
        if username_entry.get() == "johnnywvu" and password_entry.get() == "laboratory5":
            lock_frame.destroy()

    Button(lock_frame, text="Log On", command=attempt_login,
           font=("Segoe UI", 12), bg="white", fg="black", width=10).place(x=470, y=350)




icons = [
    {"text": "Calculator", "image": "assets\\Calculator.png", "command": open_calculator},
    {"text": "Explorer", "image": "assets\\Explorer.png", "command": open_explorer},
    {"text": "Paint", "image": "assets\\Paint.png", "command": open_paint},
    {"text": "Wordpad", "image": "assets\\Wordpad.png", "command": open_wordpad},

]

start_x = 50
start_y = 50
x_spacing = 100
y_spacing = 110
icons_per_column = 5

for i, icon in enumerate(icons):
    row = i % icons_per_column
    col = i // icons_per_column
    x = start_x + col * x_spacing
    y = start_y + row * y_spacing

    img = ctk.CTkImage(Image.open(icon["image"]), size=(64, 64))
    btn = ctk.CTkButton(
        window,
        image=img,
        text=icon["text"],
        compound="top",
        fg_color="transparent",
        hover_color="#0000a8",
        font=("Tahoma", 12, "bold"),
        corner_radius=0,
        width=80,
        height=90,
        command=icon["command"]
    )
    btn.image = img
    btn.place(x=x, y=y)

power_img = ctk.CTkImage(Image.open("assets\\Power.png"), size=(64,64))
powerbtn = ctk.CTkButton(
    window,
    image=power_img,
    compound="top",
    fg_color="transparent",
    hover_color="#0000a8",
    font=("Tahoma", 12, "bold"),
    corner_radius=0,
    width=80,
    height=90,
    text='Power',
    command=power_toggle
)
powerbtn.place(x=925,y=650)

window.mainloop()

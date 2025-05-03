# Software Name: Bootable USB
# Author: Luca Bocaletto

import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import win32file
import win32com.client
import tkinter.ttk as ttk

# Function to get USB drives
def get_usb_drives():
    drives = []
    wmi = win32com.client.GetObject("winmgmts:")
    for disk in wmi.InstancesOf("Win32_DiskDrive"):
        if "USB" in disk.InterfaceType:
            partitions = disk.Associators_("Win32_DiskDriveToDiskPartition")
            for partition in partitions:
                logical_disks = partition.Associators_("Win32_LogicalDiskToPartition")
                for logical_disk in logical_disks:
                    drives.append(logical_disk.DeviceID)
    return drives

# Function to select an ISO file
def select_iso():
    file_path = filedialog.askopenfilename(filetypes=[("ISO files", "*.iso")])
    if file_path:
        iso_entry.delete(0, tk.END)
        iso_entry.insert(0, file_path)

# Function to create a bootable USB
def create_bootable_usb():
    iso_file = iso_entry.get()
    selected_drive = usb_combobox.get()

    if not iso_file:
        result_label.config(text="Please select the ISO file.")
        return

    if not selected_drive:
        result_label.config(text="Please select a USB drive.")
        return

    try:
        # Check if the selected USB drive path is valid
        if not os.path.exists(selected_drive):
            raise Exception("The selected USB drive path is not valid.")

        # Check if the selected device is a USB drive
        drive_type = win32file.GetDriveType(selected_drive)
        if drive_type != win32file.DRIVE_REMOVABLE:
            raise Exception("The selected device is not a USB drive.")

        # Format the USB drive (make sure you have the necessary privileges to do this)
        format_command = f"format {selected_drive} /FS:FAT32 /Q"
        subprocess.run(format_command, shell=True, check=True)

        # Write the ISO to the USB drive
        write_command = f"xcopy {iso_file} {selected_drive} /s /e /f"
        subprocess.run(write_command, shell=True, check=True)

        result_label.config(text="The bootable USB support has been created successfully!")
    except Exception as e:
        result_label.config(text=f"Error: {str(e)}")

# Create the main window
window = tk.Tk()
window.title("Create Bootable USB Drive")

# Explanation of usage
usage_label = tk.Label(window, text="Usage:\n\n"
                                  "1. Select the ISO file using the 'Browse' button.\n"
                                  "2. Choose a USB drive from the list.\n"
                                  "3. Click 'Create Bootable USB Drive' to start the process.")
usage_label.pack()

# Label and entry field for ISO file path
iso_label = tk.Label(window, text="Select the ISO file:")
iso_label.pack()
iso_entry = tk.Entry(window)
iso_entry.pack()
browse_button = tk.Button(window, text="Browse", command=select_iso)
browse_button.pack()

# Label and ComboBox for selecting a USB drive
usb_label = tk.Label(window, text="Select a USB drive:")
usb_label.pack()
usb_drives = get_usb_drives()
usb_combobox = ttk.Combobox(window, values=usb_drives)
usb_combobox.pack()

# Button to start the process of creating a bootable USB drive
create_button = tk.Button(window, text="Create Bootable USB Drive", command=create_bootable_usb)
create_button.pack()

# Progress bar
progress = ttk.Progressbar(window, length=200, mode="indeterminate")
progress.pack()

# Label to display the results
result_label = tk.Label(window, text="")
result_label.pack()

# Run the main GUI loop
window.mainloop()

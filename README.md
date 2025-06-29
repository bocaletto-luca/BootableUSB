# Bootable USB Creator

**Author:** Bocaletto Luca

**Language:** Python

Bootable USB Creator is a Python script that provides a simple graphical user interface for creating bootable USB drives from ISO files. This tool is authored by Luca Bocaletto.

![Screenshot 2023-10-14 010259](https://github.com/elektronoide/BootableUSB/assets/134635227/ef667f27-ef19-4b3c-b7cb-3a1a0a680a63)

## Features

- **Select ISO File**: Choose an ISO file to create a bootable USB drive.
- **Automatic USB Detection**: Automatically detect available USB drives.
- **Drive Validation**: Check if the selected device is a valid USB drive.
- **USB Drive Formatting**: Format the USB drive with the FAT32 file system.
- **ISO File Copying**: Copy the contents of the selected ISO file to the USB drive.

## Prerequisites

To use Bootable USB Creator, you need the following prerequisites:

- Python 3 installed on your system.
- Required Python packages: `tkinter`, `win32file`, `win32com.client`.

## Usage

1. Run the script using Python 3.
2. Select the ISO file by clicking the "Browse" button.
3. Choose a USB drive from the list of available drives.
4. Click the "Create Bootable USB Drive" button to start the process.

## How It Works

Bootable USB Creator uses Windows Management Instrumentation (WMI) and Win32 APIs to identify USB drives and manage the process of creating a bootable USB drive.

Here's how it works:

- The script uses WMI to identify USB drives by checking the `InterfaceType`.
- It validates the selected USB drive path and ensures it is a removable device.
- The script formats the USB drive using the FAT32 file system.
- It then copies the contents of the selected ISO file to the USB drive using the `xcopy` command.

Please note that you should have the necessary privileges to format the USB drive.

*Disclaimer: Be cautious when using this script, as it may modify your storage devices. Ensure that you have a backup of important data on your USB drives before creating a bootable USB.*

---

**Maintainer Update**

All legacy projects from the old `@Elektronoide` GitHub account are now officially maintained by **@bocaletto-luca**. Please direct any issues, pull requests, and stars to **@bocaletto-luca** for all future updates.

---

# Software Name: Bootable USB
# Author: Luca Bocaletto
# Website: https://www.elektronoide.it

import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import win32file
import win32com.client
import tkinter.ttk as ttk

# Funzione per prendere la USB
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

# Funzione per la selezione del file ISO
def select_iso():
    file_path = filedialog.askopenfilename(filetypes=[("ISO files", "*.iso")])
    if file_path:
        iso_entry.delete(0, tk.END)
        iso_entry.insert(0, file_path)

# Funzione per crea la USB Bootable
def create_bootable_usb():
    iso_file = iso_entry.get()
    selected_drive = usb_combobox.get()

    if not iso_file:
        result_label.config(text="Per favore, seleziona il file ISO.")
        return

    if not selected_drive:
        result_label.config(text="Per favore, seleziona una chiavetta USB.")
        return

    try:
        # Verifica se il percorso della chiavetta USB è valido
        if not os.path.exists(selected_drive):
            raise Exception("Il percorso della chiavetta USB selezionata non è valido.")

        # Verifica se il dispositivo selezionato è una chiavetta USB
        drive_type = win32file.GetDriveType(selected_drive)
        if drive_type != win32file.DRIVE_REMOVABLE:
            raise Exception("Il dispositivo selezionato non è una chiavetta USB.")

        # Formattazione della chiavetta USB (assicurati di avere i privilegi per farlo)
        format_command = f"format {selected_drive} /FS:FAT32 /Q"
        subprocess.run(format_command, shell=True, check=True)

        # Scrittura dell'ISO sulla chiavetta USB
        write_command = f"xcopy {iso_file} {selected_drive} /s /e /f"
        subprocess.run(write_command, shell=True, check=True)

        result_label.config(text="Il supporto USB avviabile è stato creato con successo!")
    except Exception as e:
        result_label.config(text=f"Errore: {str(e)}")

# Creazione della finestra principale
window = tk.Tk()
window.title("Crea Supporto USB Avviabile")

# Spiegazione dell'utilizzo
usage_label = tk.Label(window, text="Utilizzo:\n\n"
                                  "1. Seleziona il file ISO utilizzando il pulsante 'Sfoglia'.\n"
                                  "2. Scegli una chiavetta USB dalla lista.\n"
                                  "3. Fai clic su 'Crea Supporto USB Avviabile' per avviare il processo.")
usage_label.pack()

# Etichetta e campo di inserimento per il percorso ISO
iso_label = tk.Label(window, text="Seleziona il file ISO:")
iso_label.pack()
iso_entry = tk.Entry(window)
iso_entry.pack()
browse_button = tk.Button(window, text="Sfoglia", command=select_iso)
browse_button.pack()

# Etichetta e ComboBox per la selezione del dispositivo USB
usb_label = tk.Label(window, text="Seleziona una chiavetta USB:")
usb_label.pack()
usb_drives = get_usb_drives()
usb_combobox = ttk.Combobox(window, values=usb_drives)
usb_combobox.pack()

# Pulsante per avviare il processo di creazione del supporto USB avviabile
create_button = tk.Button(window, text="Crea Supporto USB Avviabile", command=create_bootable_usb)
create_button.pack()

# Barra di avanzamento
progress = ttk.Progressbar(window, length=200, mode="indeterminate")
progress.pack()

# Etichetta per visualizzare i risultati
result_label = tk.Label(window, text="")
result_label.pack()

# Esegui il ciclo principale della GUI
window.mainloop()

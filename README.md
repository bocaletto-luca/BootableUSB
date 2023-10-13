# Bootable USB Creator

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

## Author

- **Author:** Luca Bocaletto
- **Website:** [https://www.elektronoide.it](https://www.elektronoide.it)

For more information, issues, or contributions, please visit the project's [repository](https://github.com/elektronoide/bootable-usb-creator).

*Disclaimer: Be cautious when using this script, as it may modify your storage devices. Ensure that you have a backup of important data on your USB drives before creating a bootable USB.*

# Creatore di USB Avviabile

Il Creatore di USB Avviabile è uno script Python che fornisce un'interfaccia utente grafica semplice per creare unità USB avviabili da file ISO. Questo strumento è stato creato da Luca Bocaletto.

## Funzionalità

- **Seleziona File ISO**: Scegli un file ISO per creare un'unità USB avviabile.
- **Rilevamento Automatico USB**: Rileva automaticamente le unità USB disponibili.
- **Convalida dell'Unità**: Verifica se il dispositivo selezionato è un'unità USB valida.
- **Formattazione dell'Unità USB**: Formatta l'unità USB con il sistema di file FAT32.
- **Copia del File ISO**: Copia il contenuto del file ISO selezionato sull'unità USB.

![Screenshot 2023-10-14 005906](https://github.com/elektronoide/BootableUSB/assets/134635227/12cc7393-01c7-4674-9b37-22c41aa56e49)

## Requisiti

Per utilizzare il Creatore di USB Avviabile, sono necessari i seguenti requisiti:

- Python 3 installato nel sistema.
- Pacchetti Python necessari: `tkinter`, `win32file`, `win32com.client`.

## Utilizzo

1. Esegui lo script utilizzando Python 3.
2. Seleziona il file ISO facendo clic sul pulsante "Sfoglia".
3. Scegli un'unità USB dalla lista delle unità disponibili.
4. Fai clic sul pulsante "Crea Unità USB Avviabile" per avviare il processo.

## Come Funziona

Il Creatore di USB Avviabile utilizza la Windows Management Instrumentation (WMI) e le API Win32 per identificare le unità USB e gestire il processo di creazione di un'unità USB avviabile.

Ecco come funziona:

- Lo script utilizza la WMI per identificare le unità USB verificando il campo `InterfaceType`.
- Convalida il percorso dell'unità USB selezionata e si assicura che sia un dispositivo rimovibile.
- Lo script formatta l'unità USB utilizzando il sistema di file FAT32.
- Successivamente, copia il contenuto del file ISO selezionato sull'unità USB utilizzando il comando `xcopy`.

Si prega di notare che è necessario disporre dei privilegi necessari per formattare l'unità USB.

## Autore

- **Autore:** Luca Bocaletto
- **Sito Web:** [https://www.elektronoide.it](https://www.elektronoide.it)

Per ulteriori informazioni, problemi o contributi, visita il [repository](https://github.com/elektronoide/bootable-usb-creator) del progetto.

*Nota: Si prega di fare attenzione nell'utilizzo di questo script, poiché potrebbe modificare i dispositivi di archiviazione. Assicurarsi di disporre di un backup dei dati importanti sulle unità USB prima di creare un'unità USB avviabile.*

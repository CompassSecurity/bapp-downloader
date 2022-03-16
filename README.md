# Burp Extension Downloader
When working with Burp Suite on customer machines the BApp Store is often blocked and the analyst has to manually install extensions. Keeping a local copy of Bapp files manually is painful. This script can be used to download the latest versions of the most common Burp extensions from the BApp store.

## Installation

Create and activate Python venv (this step is optional but highly recommended)
```
$ python3 -m venv ~/venv
$ source ~/venv/bin/activate
```

Install dependencies
```
(venv) $ python3 -m pip install -r requirements.txt
```

## Usage
```
(venv) $ python3 bapp_downloader.py 
[*] Downloading Active Scan++...
[*] Downloading Add Custom Header...
[CUT]
[*] Downloading Turbo Intruder...
[*] Downloading Uplaod Scanner...
[*] Creting ZIP archive...
[*] Creting GZTAR archive...
```
The individual files are written to `./bapps` and two archives are created:
* bapps.tar.gz
* bapps.zip

## Contributions
Please feel free to add extensions you like :)

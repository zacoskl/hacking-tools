import os
import requests
from tqdm import tqdm
from colorama import Fore, init
import time

init(autoreset=True)

downloads = [
    {"name": "passwords/python pips", "url": "https://github.com/zacoskl/data/archive/refs/heads/main.zip", "filename": "data-main.zip"},
    {"name": "Python Installer", "url": "https://www.python.org/ftp/python/3.11.0/python-3.11.0-amd64.exe", "filename": "python-3.11.0-amd64.exe"},
    {"name": "Nmap Installer", "url": "https://nmap.org/dist/nmap-7.95-setup.exe", "filename": "nmap-7.95-setup.exe"},
    {"name": "Git Installer", "url": "https://github.com/git-for-windows/git/releases/download/v2.47.1.windows.1/Git-2.47.1-64-bit.exe", "filename": "Git-2.47.1-64-bit.exe"},
    {"name": "Wireshark Installer", "url": "https://2.na.dl.wireshark.org/win64/Wireshark-4.4.2-x64.exe", "filename": "Wireshark-4.4.2-x64.exe"},
    {"name": "Tor Browser Installer", "url": "https://www.torproject.org/dist/torbrowser/14.0.3/tor-browser-windows-x86_64-portable-14.0.3.exe", "filename": "tor-browser-windows-x86_64-portable-14.0.3.exe"},
    {"name": "GitHub Desktop Installer", "url": "https://central.github.com/deployments/desktop/desktop/latest/win32", "filename": "GitHubDesktop-installer.exe"},
    {"name": "Metasploit Installer", "url": "https://downloads.metasploit.com/data/releases/metasploit-latest-windows-x64-installer.exe", "filename": "metasploit-latest-windows-x64-installer.exe"},
    {"name": "Cyberduck Installer", "url": "https://update.cyberduck.io/windows/Cyberduck-Installer-9.0.3.42112.exe", "filename": "Cyberduck-installer.exe"},
    {"name": "Notepad++ Installer", "url": "https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.9/npp.8.4.9.Installer.exe", "filename": "npp.8.4.9.Installer.exe"}
]

def download_file(url, filename):
    try:
        response = requests.get(url, stream=True)
        total_size = int(response.headers.get('content-length', 0))

        with open(filename, "wb") as file, tqdm(
                desc=f"{filename} Downloading...",
                total=total_size,
                unit='B', unit_scale=True,
                bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{percentage:3.0f}%]",
                ncols=100,
                colour='yellow',
                dynamic_ncols=True,
                ascii=False) as bar:

            start_time = time.time()
            last_update_time = start_time
            download_speed = 0
            total_downloaded = 0

            for data in response.iter_content(chunk_size=1024):
                file.write(data)
                bar.update(len(data))
                total_downloaded += len(data)

                current_time = time.time()
                elapsed_time = current_time - last_update_time
                if elapsed_time >= 1:
                    download_speed = total_downloaded / elapsed_time
                    last_update_time = current_time
                    remaining_time = (total_size - total_downloaded) / download_speed

                    bar.set_postfix_str(f"Speed: {download_speed / 1024:.2f} KB/s | ETA: {remaining_time:.2f} s", refresh=True)

            total_time = time.time() - start_time
            print(f"\n{Fore.GREEN}[SUCCESS] {filename} downloaded successfully!")
            print(f"Total download time: {total_time:.2f} seconds")

    except Exception as e:
        print(f"\n{Fore.RED}[ERROR] Failed to download {filename}: {str(e)}")

def show_loading(message):
    spinner = ["|", "/", "-", "\\"]
    for _ in range(30):
        for frame in spinner:
            print(f"\r{Fore.CYAN}{message} {frame}", end="")
            time.sleep(0.1)
    print()

def display_welcome_message():
    os.system('cls' if os.name == 'nt' else 'clear')

    border_length = 60
    welcome_text = "Welcome to the Ethical Hacking Tools by vuln_horizon"

    border = "*" * border_length
    padding = (border_length - len(welcome_text) - 4) // 2

    print(Fore.GREEN + border)
    print(Fore.YELLOW + "*" * padding + "  " + Fore.CYAN + welcome_text + "  " + "*" * padding)
    print(Fore.GREEN + border)
    print()

def main():
    display_welcome_message()

    print("\nPlease select a file to download:")

    for idx, download in enumerate(downloads, 1):
        print(f"{Fore.YELLOW}{idx}. {download['name']}")

    try:
        choice = int(input(f"\n{Fore.WHITE}Enter the number of the file you want to download: "))

        if 1 <= choice <= len(downloads):
            selected_download = downloads[choice - 1]
            print(f"\n{Fore.CYAN}Starting download of {selected_download['name']}...")
            show_loading("Preparing the download")
            download_file(selected_download['url'], selected_download['filename'])
        else:
            print(f"{Fore.RED}[ERROR] Invalid choice. Please select a valid number from the list.")
    except ValueError:
        print(f"{Fore.RED}[ERROR] Invalid input. Please enter a number.")

    restart = input(f"{Fore.WHITE}Do you want to go back to the main menu? (y/n): ").lower()
    if restart == 'y':
        main()
    else:
        print(f"{Fore.GREEN}Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()

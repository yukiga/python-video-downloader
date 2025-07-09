import os
import shutil
import time
from yt_dlp import YoutubeDL

language = 'es'

textos = {
    'es': {
        'banner': """
 ▌ ▐·▪  ·▄▄▄▄  ▄▄▄ .        ·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄ ▄▄▌         ▄▄▄· ·▄▄▄▄  ▄▄▄ .▄▄▄  
▪█·█▌██ ██· ██ ▀▄.▀· ▄█▀▄   ██· ██  ▄█▀▄ ██· █▌▐█•█▌▐███•   ▄█▀▄ ▐█ ▀█ ██· ██ ▀▄.▀·▀▄ █·
▐█▐█•▐█·▐█▪ ▐█▌▐▀▀▪▄▐█▌.▐▌  ▐█▪ ▐█▌▐█▌.▐▌██▪▐█▐▐▌▐█▐▐▌██ ▪ ▐█▌.▐▌▄█▀▀█ ▐█▪ ▐█▌▐▀▀▪▄▐▀▀▄ 
 ███ ▐█▌██. ██ ▐█▄▄▌▐█▌.▐▌  ██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌▐█▌ ▄▐█▌.▐▌▐█▪ ▐▌██. ██ ▐█▄▄▌▐█•█▌
. ▀  ▀▀▀▀▀▀▀▀•  ▀▀▀  ▀█▄▀▪  ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪.▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀
""",
        'menu': "\n=== DESCARGADOR DE VIDEOS SIMPLE ===",
        'opciones': [
            "1. Calidad máxima disponible",
            "2. Resolución 1080p",
            "3. Resolución 720p",
            "4. Solo audio (MP3)",
            "5. Salir"
        ],
        'url': "Ingresa la URL del video: ",
        'folder': "¿Dónde quieres guardarlo? (vacío = carpeta actual): ",
        'invalid': "Opción no válida. Presiona Enter para continuar...",
        'exit': "Gracias por usar el descargador. ¡Hasta la próxima!",
        'downloading': "Iniciando descarga: ",
        'done': "Descarga finalizada correctamente.",
        'error': "Ha ocurrido un error: ",
        'continue': "Presiona Enter para volver al menú principal...",
        'lang_switch': "Press L to switch to English"
    },
    'en': {
        'banner': """
 ▌ ▐·▪  ·▄▄▄▄  ▄▄▄ .        ·▄▄▄▄        ▄▄▌ ▐ ▄▌ ▐ ▄ ▄▄▌         ▄▄▄· ·▄▄▄▄  ▄▄▄ .▄▄▄  
▪█·█▌██ ██· ██ ▀▄.▀· ▄█▀▄   ██· ██  ▄█▀▄ ██· █▌▐█•█▌▐███•   ▄█▀▄ ▐█ ▀█ ██· ██ ▀▄.▀·▀▄ █·
▐█▐█•▐█·▐█▪ ▐█▌▐▀▀▪▄▐█▌.▐▌  ▐█▪ ▐█▌▐█▌.▐▌██▪▐█▐▐▌▐█▐▐▌██ ▪ ▐█▌.▐▌▄█▀▀█ ▐█▪ ▐█▌▐▀▀▪▄▐▀▀▄ 
 ███ ▐█▌██. ██ ▐█▄▄▌▐█▌.▐▌  ██. ██ ▐█▌.▐▌▐█▌██▐█▌██▐█▌▐█▌ ▄▐█▌.▐▌▐█▪ ▐▌██. ██ ▐█▄▄▌▐█•█▌
. ▀  ▀▀▀▀▀▀▀▀•  ▀▀▀  ▀█▄▀▪  ▀▀▀▀▀•  ▀█▄▀▪ ▀▀▀▀ ▀▪▀▀ █▪.▀▀▀  ▀█▄▀▪ ▀  ▀ ▀▀▀▀▀•  ▀▀▀ .▀  ▀
""",
        'menu': "\n=== SIMPLE VIDEO DOWNLOADER ===",
        'opciones': [
            "1. Maximum available quality",
            "2. 1080p resolution",
            "3. 720p resolution",
            "4. Audio only (MP3)",
            "5. Exit"
        ],
        'url': "Enter video URL: ",
        'folder': "Save to folder (empty = current): ",
        'invalid': "Invalid option. Press Enter to continue...",
        'exit': "Thanks for using the downloader. See you soon!",
        'downloading': "Starting download: ",
        'done': "Download completed successfully.",
        'error': "An error occurred: ",
        'continue': "Press Enter to return to main menu...",
        'lang_switch': "Presiona L para cambiar a Español"
    }
}

def ffmpeg_available():
    return shutil.which("ffmpeg") and shutil.which("ffprobe")

def get_format_string(quality):
    return {
        'max': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
        '1080': 'bestvideo[height<=1080]+bestaudio/best[height<=1080]',
        '720': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
        'audio': 'bestaudio[ext=m4a]'
    }.get(quality, 'best')

def build_options(quality, folder):
    options = {
        'format': get_format_string(quality),
        'outtmpl': os.path.join(folder, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'quiet': False,
        'ignoreerrors': False,
        'http_headers': {'User-Agent': 'Mozilla/5.0'}
    }

    if os.path.exists('cookies.txt'):
        options['cookiefile'] = 'cookies.txt'

    if ffmpeg_available():
        if quality == 'audio':
            options['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192'
            }]
        else:
            options['merge_output_format'] = 'mp4'
            options['postprocessors'] = [{
                'key': 'FFmpegVideoRemuxer',
                'preferedformat': 'mp4'
            }]
        options['prefer_ffmpeg'] = True

    return options

def download_video(url, quality, folder):
    try:
        with YoutubeDL(build_options(quality, folder)) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'video')
            print(f"\n{textos[language]['downloading']}{title}\n")
            ydl.download([url])
            print(f"\n{textos[language]['done']}\n")
    except Exception as error:
        print(f"\n{textos[language]['error']}{error}\n")

def show_banner_animado(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    for linea in texto.strip("\n").split("\n"):
        print(linea)
        time.sleep(0.05)  

def show_menu():
    show_banner_animado(textos[language]['banner'])
    print(textos[language]['menu'] + "\n")
    for line in textos[language]['opciones']:
        print(line)
    print("\n" + textos[language]['lang_switch'])

def main():
    global language
    quality_map = {'1': 'max', '2': '1080', '3': '720', '4': 'audio'}

    while True:
        show_menu()
        choice = input("\n> ").strip().lower()

        if choice == '5':
            print(f"\n{textos[language]['exit']}\n")
            break
        elif choice == 'l':
            language = 'en' if language == 'es' else 'es'
            continue
        elif choice in quality_map:
            url = input(f"\n{textos[language]['url']}").strip()
            folder = input(f"{textos[language]['folder']}").strip() or os.getcwd()
            os.makedirs(folder, exist_ok=True)
            download_video(url, quality_map[choice], folder)
            input(textos[language]['continue'])
        else:
            print(f"\n{textos[language]['invalid']}")
            input()

if __name__ == '__main__':
    main()

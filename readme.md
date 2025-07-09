# Descarga todo tipo de vídeos (YouTube 8K, 4K, 1080p, 720p / Shorts / MP3 / TikTok / Reels Instagram / Reddit / X | Twitter / Etc.) – Solo para Windows

Este proyecto permite descargar videos desde múltiples páginas compatibles usando Python, `yt-dlp` y `FFmpeg`. Instalar FFmpeg es muy fácil: más abajo tienes un tutorial en video y un paso a paso escrito.

---

## Requisitos

- Python 3.7 o superior
- [`FFmpeg`](https://ffmpeg.org)
- `yt-dlp` (se instala automáticamente con pip)

---

## Instalación de dependencias

### Opción 1: Automática

1. Ejecuta `instalar_dependencias.bat` (como administrador).
2. Se instalará `yt-dlp` y sus dependencias.

### Opción 2: Manual

1. Abre CMD como administrador.
2. Ve a la carpeta del proyecto:
   ```cmd
   cd "C:\Users\TU_USUARIO\Ruta\download"
   ```
3. Ejecuta:
   ```cmd
   pip install -r requirements.txt
   ```

---

## Cómo se usa la herramienta

1. Ejecuta `main.py`.
2. Elige una opción:
   1. Calidad máxima disponible (recomendado para todo)
   2. Resolución 1080p
   3. Resolución 720p
   4. Solo audio (MP3)
   5. Salir
3. Ingresa la URL del video.
4. Elige la carpeta donde guardarlo (enter = carpeta actual).
5. Presiona **L** para cambiar entre español e inglés.

---

## Siguiente paso

Después de elegir opción y URL, espera a que termine la descarga y encontrarás tu archivo en formato MP4 o MP3.

---

## Instalación de FFmpeg

FFmpeg es obligatrio, Primero explicaré el proceso de forma escrita. Abajo dejé dos links de videos útiles en inglés y español por si no quieres leer.

1. [Se dirigen a la página](https://www.gyan.dev/ffmpeg/builds/) bajan hasta donde dice "release builds".

2. Haz clic en `ffmpeg-release-essentials.7z` o `ffmpeg-release-essentials.zip`, la que gustes; es lo mismo. La descarga comenzará.

3. Extrae el archivo y mueve la carpeta hacia el disco local C (o donde prefieras), pero es importante no perderla. Ubica la carpeta `bin` y copia la ruta, por ejemplo: `C:\ffmpeg\bin`.

4. `Presiona Win + S y busca "Editar las variables de entorno del sistema". En "Variables de entorno", haz doble clic en la variable "Path"`.

5. Haz clic en "Nuevo", pega la ruta, da aceptar a todo y cierra.

6. Verifica si se instaló correctamente abriendo una consola CMD y ejecutando `ffmpeg -version`. Debería mostrarse la versión instalada.

### Links

[Video Tutorial En Español, créditos "Software Simplificado"](https://www.youtube.com/watch?v=WNjEISfzcYM)`

[Video Tutorial En inglés, créditos "Koolac"](https://www.youtube.com/watch?v=JR36oH35Fgg)


## Consideraciones Importantes

Cada plataforma maneja formatos y calidades distintas. YouTube ofrece 4K/8K/60fps y MP3 sin problemas; TikTok y Twitter a veces no entregan audio separado, Instagram (Reels) puede bajar bitrate, Reddit suele dar buen resultado. Usa VLC para reproducir los videos, el reproductor de Windows a veces no reconoce los códecs de FFmpeg.

Esta herramienta fue hecha para probar y cubrir casos generales, si encuentras algún video que no descarga como esperas, puedes probar otra opción o herramienta, pero para uso habitual en YouTube funciona de maravilla.

---

Si llegaste hasta aquí, muchas gracias, espero que lo disfrutes y te sirva :)!


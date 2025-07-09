# Download all types of videos (YouTube 8K, 4K, 1080p, 720p / Shorts / MP3 / TikTok / Instagram Reels / Reddit / X | Twitter / Etc.) – Windows only

This project allows you to download videos from multiple supported sites using Python, `yt-dlp`, and `FFmpeg`. Installing FFmpeg is very easy: below you have a video tutorial and written step-by-step instructions.

---

## Requirements

- Python 3.7 or higher
- [`FFmpeg`](https://ffmpeg.org)
- `yt-dlp` (installed automatically with pip)

---

## Dependency Installation

### Option 1: Automatic

1. Run `instalar_dependencias.bat` (as administrator).
2. `yt-dlp` and its dependencies will be installed.

### Option 2: Manual

1. Open CMD as administrator.
2. Go to the project folder:
```cmd
cd "C:\Users\YOUR_USER\Path\download"
```
3. Run:
```cmd
pip install -r requirements.txt
```

---

## How to use the tool

1. Run `main.py`.
2. Choose an option:
1. Highest available quality (recommended for all)
2. 1080p resolution
3. 720p resolution
4. Audio only (MP3)
5. Exit
3. Enter the video URL.
4. Choose the folder to save it to (enter = current folder).
5. Press **L** to switch between Spanish and English.

---

## Next Step

After choosing the option and URL, wait for the download to finish and you'll find your file in MP4 or MP3 format.

---

## Installing FFmpeg

FFmpeg is mandatory. I'll first explain the process in writing. Below, I've included two useful video links in English and Spanish in case you don't want to read.

1. Go to the page [https://www.gyan.dev/ffmpeg/builds/] and scroll down to where it says "release builds".

2. Click on `ffmpeg-release-essentials.7z` or `ffmpeg-release-essentials.zip`, whichever you prefer; it's the same. The download will begin.

3. Extract the file and move the folder to your local drive C (or wherever you prefer), but it's important not to lose it. Locate the `bin` folder and copy the path, for example: `C:\ffmpeg\bin`.

4. Press Win + S and search for "Edit system environment variables." Under "Environment Variables," double-click the "Path" variable.

5. Click "New," paste the path, click OK, and close.

6. Check if it installed correctly by opening a CMD console and running "ffmpeg -version." The installed version should be displayed.

### Links

[Video Tutorial in Spanish, credits "Software Simplificado"](https://www.youtube.com/watch?v=WNjEISfzcYM)

[Video Tutorial in English, credits "Koolac"](https://www.youtube.com/watch?v=JR36oH35Fgg)

## Important Considerations

Each platform handles different formats and qualities. YouTube offers 4K/8K/60fps and MP3 without problems; TikTok and Twitter sometimes don't deliver separate audio, Instagram (Reels) can lower the bitrate, and Reddit usually works well. Use VLC to play the videos; Windows Media Player sometimes doesn't recognize FFmpeg codecs.

This tool was created for testing and general use. If you find a video that doesn't download as expected, you can try another option or tool, but for regular use on YouTube, it works great.

---

If you made it this far, thank you very much. I hope you enjoy it and find it useful :)!
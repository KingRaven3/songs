from yt_dlp import YoutubeDL
from pyrogram import Client
import time

ITEM_COUNT = 64

bot = Client(
  "uploader",
  api_id=6,
  api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
  bot_token="5667720219:AAFK0EOKlXTyW9vnXwwIBRL3x1OBzf_kd8g"
)


# Channel URL (replace with the actual URL)
playlist_url = "https://www.youtube.com/playlist?list=PL_XQX1_zerr3PqqXRWuC7LFeLze6Z1CXI"

# Download options
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
    }],
    'verbose': True,  # Optional, shows download progress
    'playlistend': ITEM_COUNT,  # Optional, download limit (replace with number)
    'download_archive': 'downloaded.txt',  # Optional, download archive filename
}

downloaded_filenames = []  # Add an empty list to store filenames

try:
  with YoutubeDL(ydl_opts) as ydl:
    # Extract video information from the channel URL (playlist)
    playlist_info = ydl.extract_info(playlist_url, download=False)

    # Loop through each video entry in the playlist
    for video in playlist_info["entries"]:
      # Download the audio for each video
      ydl.download([video["url"]])
      # Extract filename from the downloaded video information
      filename = ydl.prepare_filename(video)  # Uses YoutubeDL method
      downloaded_filenames.append(filename)

  print("Download complete!")
  print(f"Downloaded filenames: {downloaded_filenames}")
  print("uploading to telegram...")

  with bot:
    for x in downloaded_filenames:
      print(f"UPLOADING {x}")
      bot.send_audio(-1002094180732 , x)
      print("SLEEPING FOR 5 SECONDS....")
      time.sleep(5)
except Exception as e:
  print(f"An error occurred: {e}")

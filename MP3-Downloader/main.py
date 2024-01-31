# import youtube_dl  # client to many multimedia portals
import yt_dlp


# downloads yt_url to the same directory from which the script runs
def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])


def main():
    yt_url = "https://www.youtube.com/watch?v=8OAPLk20epo"
    # yt_url = "https: // www.youtube.com / watch?v = hceNBCnOx44"
    download_audio(yt_url)


main()

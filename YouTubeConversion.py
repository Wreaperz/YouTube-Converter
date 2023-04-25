import os
import yt_dlp


def download_video(url, output_format):
    ydl_opts = {
        'format': 'bestaudio/best' if output_format == 'mp3' else 'bestvideo+bestaudio',
        'outtmpl': f'videos/%(title)s.%(ext)s',
        'merge_output_format': 'mp4',
        'quiet': True,
        'ffmpeg_location': 'ffmpeg/bin/',  # Specify the path to the ffmpeg folder
    }

    if output_format == 'mp3':
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


def main():
    url = input("Enter the YouTube video URL: ")
    os.makedirs("videos", exist_ok=True)

    output_format = ""
    while output_format not in ["mp3", "mp4"]:
        output_format = input("Enter the desired output format (mp3 or mp4): ").lower()

    download_video(url, output_format)
    print(f"Downloaded and converted to {output_format} in the 'videos' directory.")


if __name__ == "__main__":
    main()

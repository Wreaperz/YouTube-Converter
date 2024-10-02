import os
from pytubefix import YouTube # IMPORTANT - USES THE PYTUBEFIX FORK
import sys
import logging

# Enable logging for pytube
logging.basicConfig(level=logging.DEBUG)

def download_video(url, output_format, save_folder):
    os.makedirs(save_folder, exist_ok=True)

    try:
        video = YouTube(url)
        print(f"Video title: {video.title}")

        if output_format == 'mp3':
            best_audio = video.streams.get_audio_only()
            out_file = best_audio.download(output_path=save_folder, filename=f"{video.title}.mp4")

            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(f"Downloaded and converted to mp3: {new_file}")

        elif output_format == 'mp4':
            best_video = video.streams.get_highest_resolution()
            out_file = best_video.download(output_path=save_folder, filename=f"{video.title}.mp4")
            print(f"Downloaded video: {out_file}")

    except Exception as e:
        print(f"An error occurred: {type(e).__name__}: {e}")


def main():
    while True:
        url = input("Enter the YouTube video URL >> ")

        # If the url request is empty, exit the program
        if url == "":
            sys.exit()

        output_format = ""
        while output_format not in ["mp3", "mp4"]:
            output_format = input("Enter the desired output format (mp3 or mp4): ").lower()

        save_folder = input("Enter the folder where you want to save the file: ")

        # Run the function to actually download and save the file
        download_video(url, output_format, save_folder)
        
        print(f"Downloaded and converted to {output_format} in the '{save_folder}' directory.")
        print()
        print()

if __name__ == "__main__":
    main()

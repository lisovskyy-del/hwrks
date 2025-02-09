from pytubefix import YouTube

def user_input():
    choice = input("Do you want to download audio or video? (audio/video): ").strip().lower()
    video_url = input("Enter the Youtube video URL: ")
    return choice, video_url


def download_video(url, output_path=''):
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        print(f"Downloading video from: {yt.title}")
        video_stream.download(output_path=output_path)
        print("Download completed!")
    except Exception as exception:
        print(f"Error: {exception}")

def download_audio(url, output_path=''):
    try:
        yt = YouTube(url)
        audio_stream = yt.streams.filter(only_audio=True).first()
        print(f"Downloading audio from: {yt.title}")
        audio_stream.download(output_path=output_path)
        print("Download completed!")
    except Exception as exception:
        print(f"Error: {exception}")

while True:
    choice, video_url = user_input()
    if choice == "audio":
        download_audio(video_url)
    elif choice == "video":
        download_video(video_url)
    else:
        print("Invalid choice.")

# https://www.youtube.com/watch?v=LGcECozNXEw&t
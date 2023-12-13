from pytube import YouTube, Playlist

URL = input("Enter Youtube URL (Playlist or Single Video): ")
if "https://www.youtube.com/playlist?" not in URL.lower():
    video = YouTube(URL)
    video.streams.get_highest_resolution().download()
else:
    playlist = Playlist(URL)
    for video_url in playlist:
        video = YouTube(video_url)
        video.streams.get_highest_resolution().download()
        print(f"Downloaded: {video.title}")

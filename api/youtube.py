import yt_dlp


def get(video_url):
  ydl_opts = {'format': 'best'}
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    return info_dict
    
def music(video_url):
  ydl_opts = {'format': 'bestaudio/best'}
  with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    info_dict = ydl.extract_info(video_url, download=False)
    return info_dict["url"]

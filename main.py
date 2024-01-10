from flask import Flask, request
from api import youtube, tikdou, facebook, instagram

app = Flask('app')

@app.route('/')
def home_info():
  return """<meta name="viewport" content="width=device-width, initial-scale=1.0">
    <b>Selenium Download API</b>"""

@app.route('/youtube')
def youtube_download():
  url = request.args.get('url')
  if url:
    try:
      return {"url": youtube.get(url)["url"]}
    except Exception as e:
      return {"error": f"{e}"}
  else:
    return {"error": "no url found"}

@app.route('/music')
def music_download():
  url = request.args.get('url')
  if url:
    try:
      return {"url": youtube.music(url)}
    except Exception as e:
      return {"error": f"{e}"}
  else:
    return {"error": "no url found"}

@app.route('/tikdou')
def tiktokdouyin_download():
  url = request.args.get('url')
  if url:
    try:
      dl_url, music_url, is_video = tikdou.get(url)
    except Exception as e:
      return {"error": f"{e}"}
    return {"url": dl_url, "music": music_url, "is_video": is_video}
  else:
    return {"error": "no url found"}

@app.route('/facebook')
def facebook_download():
  url = request.args.get('url')
  if url:
    try:
      return {"url": facebook.get(url)}
    except Exception as e:
      return {"error": f"{e}"}
  else:
    return {"error": "no url found"}

@app.route('/instagram')
def instagram_download():
  url = request.args.get('url')
  if url:
    try:
      is_video, download_url = instagram.get(url)
      return {"is_video": is_video, "url": download_url}
    except Exception as e:
      return {"error": f"{e}"}
  else:
    return {"error": "no url found"}

@app.route('/other')
def other_download():
  url = request.args.get('url')
  if url:
    try:
      return youtube.get(url)
    except Exception as e:
      return {"error": f"{e}"}
  else:
    return {"error": "no url found"}

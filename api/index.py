from flask import Flask, render_template, request, redirect
from pytubefix import YouTube
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form.get('video_url')

    if not video_url:
        return 'Error: Please provide a YouTube URL.'

    try:
        yt = YouTube(video_url, use_po_token=True)

        video_stream = yt.streams.get_highest_resolution()

        '''if not video_stream:
            return 'Error: Could not find a suitable progressive MP4 stream.'

        buffer = BytesIO()
        video_stream.stream_to_buffer(buffer)
        buffer.seek(0)

        return send_file(buffer, as_attachment=True, download_name=f"{yt.title}.mp4", mimetype='video/mp4')'''

        direct_link = video_stream.url

        return redirect(direct_link, code=302)
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/about')
def about():
    return 'About'
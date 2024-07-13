from django.shortcuts import render, redirect
from pytube import YouTube
import os

def download_video(request):
    if request.method == 'POST':
        video_url = request.POST.get('youtube_url')
        try:
            yt = YouTube(video_url)
            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
            output_path = 'downloaded_videos'
            video_stream.download(output_path=output_path)
            video_path = os.path.join(output_path, video_stream.default_filename)
            return render(request, 'videos/download_form.html', {
                'video_path': video_path,
                'message': 'Video downloaded successfully!'
            })
        except Exception as e:
            return render(request, 'videos/download_form.html', {'message': str(e)})
    else:
        return render(request, 'videos/download_form.html')


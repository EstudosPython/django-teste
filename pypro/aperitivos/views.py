from django.shortcuts import render


def video(request, slug):
    videos = {
        'motivacao':{'titulo': 'Video aperitivo: inicial', 'vimeo_id': 577177067},
        'instalacao-windows':{'titulo': 'instalação Windows', 'vimeo_id': 251497668},
    }
    video = videos[slug]
    return render(request, 'aperitivos/video.html', context={'video': video})

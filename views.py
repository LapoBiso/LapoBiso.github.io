from django.http import HttpResponse
from .models import Post
from django.template import loader


def index(request):
    posts = Post.objects.all()
    template = loader.get_template('blog/index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))

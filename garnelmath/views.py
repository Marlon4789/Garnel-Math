from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.

# Inicio
def home(request):
    return render(request, 'layouts/home.html')

# Layout del panel para contenido
def math_content_panel(request):
    return render(request, 'layouts/math_content_panel.html')

# Vistas del contenido a mostrar
# def introduccion(request):
#     return render(request, 'content/introduccion.html')

# detalles del post
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.all()
    return render(request, 'content/post_detail.html', {'post':post, 'posts':posts})

# def posts_list(request):
#     posts = Post.objects.all()
#     return render(request, 'layouts/math_content_panel.html', {'posts':posts})

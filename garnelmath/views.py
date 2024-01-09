from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.urls import reverse
from .forms import SubscriptionForm, FeedbackForm



# Create your views here.

# Inicio
def home(request):
    #return render(request, 'layouts/home.html')

    # form subscripción
    if request.method == 'GET':
        return render(request, 'layouts/home.html', {'form': SubscriptionForm})
    else:
        try:
            form = SubscriptionForm(request.POST)
            new_sub = form.save(commit=False)
            new_sub.save()
            return render(request, 'layouts/home.html', {
                'success': 'todo va bien.',
            })
        except ValueError:
            return render(request, 'layouts/home.html', {
                'form': SubscriptionForm,
                'error': 'Este correo ya existe.'
            })

# Layout del panel para contenido
def math_content_panel(request):    
    return render(request, 'layouts/math_content_panel.html')

# detalles del post
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    posts = Post.objects.all()

    # Formulario feedback
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            new_feedback = form.save()
    else:
        form = FeedbackForm()

    return render(request, 'content/post_detail.html', {'post':post, 'posts':posts})




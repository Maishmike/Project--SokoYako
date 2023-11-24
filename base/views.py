from django.shortcuts import render, redirect
from item.models import Item, Category
from .forms import SignUpForm
from django.contrib import messages
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)
    featured = Item.objects.order_by('-is_featured')
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
        'featured': featured})


def contact(request):
    return render(request, 'contact.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account was created successfully. Kindly log in.')
            return redirect('base:login')
    else:
        form = SignUpForm()

    return render(request, 'signup.html', {'form': form})


def about(request):
    return render(request, 'about.html')

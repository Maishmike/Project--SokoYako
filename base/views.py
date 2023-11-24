from django.shortcuts import render, redirect
from item.models import Item, Category
from .forms import SignUpForm
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
            return redirect('login')
    else:
        form = SignUpForm()

    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})




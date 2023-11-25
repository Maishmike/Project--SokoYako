from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item, Category
from .forms import SignUpForm
from django.contrib import messages
from django.utils import timezone
from .models import ContactCard
from .forms import ContactCardForm
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    featured = Item.objects.order_by('-is_featured')
    featured_items = Item.objects.filter(is_featured=True)
    categories = Category.objects.all()
    current_time = timezone.now()
    last_24_hours = current_time - timezone.timedelta(days=1)
    new_items = Item.objects.filter(created_at__gte=last_24_hours)
    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
        'featured': featured,
        'featured_items': featured_items,
        'new_items': new_items
    })


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


@login_required
def view_contact_card(request):
    contact_card = get_object_or_404(ContactCard, user=request.user)
    return render(request, 'view_contact_card.html', {'contact_card': contact_card})


def create_contact_card(request):
    if request.method == 'POST':
        form = ContactCardForm(request.POST)
        if form.is_valid():
            contact_card = form.save(commit=False)
            contact_card.user = request.user
            contact_card.save()
            return redirect('base:view_contact_card')
    else:
        form = ContactCardForm()
    return render(request, 'create_contact_card.html', {'form': form})


def view_seller_contact_card(request, seller_id):
    seller = get_object_or_404(User, id=seller_id)
    contact_card = get_object_or_404(ContactCard, user=seller)
    return render(request, 'view_seller_contact_card.html', {'contact_card': contact_card})




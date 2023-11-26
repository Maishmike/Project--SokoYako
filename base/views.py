from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item, Category
from .forms import SignUpForm
from django.contrib import messages
from django.utils import timezone
from .models import ContactCard
from .forms import ContactCardForm, EditContactCardForm
# Create your views here.


def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    featured = Item.objects.order_by('-is_featured')
    featured_items = Item.objects.filter(is_featured=True)
    categories = Category.objects.all()
    contact_card = get_object_or_404(ContactCard, user=request.user)
    current_time = timezone.now()
    latest = current_time - timezone.timedelta(days=1)
    new_items = Item.objects.filter(created_at__gte=latest)
    return render(request, 'index.html', {
        'categories': categories,
        'items': items,
        'featured': featured,
        'featured_items': featured_items,
        'new_items': new_items,
        'contact_card': contact_card
    })


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
    contact_card = get_object_or_404(ContactCard, user=request.user)
    return render(request, 'about.html',{
        'contact_card': contact_card
    })


@login_required
def view_contact_card(request):
    contact_card = get_object_or_404(ContactCard, user=request.user)
    return render(request, 'view_contact_card.html', {'contact_card': contact_card})


def create_contact_card(request):
    contact_card = None
    if request.method == 'POST':
        form = ContactCardForm(request.POST)
        if form.is_valid():
            contact_card = form.save(commit=False)
            contact_card.user = request.user
            contact_card.save()
            messages.success(request, 'Contact Card created successfully.')
            return redirect('base:view_contact_card')
    else:
        form = ContactCardForm()
    return render(request, 'create_contact_card.html', {
        'form': form,
        'contact_card': contact_card,
    })


def view_seller_contact_card(request, seller_id):
    seller = get_object_or_404(User, id=seller_id)
    contact_card = get_object_or_404(ContactCard, user=seller)
    return render(request, 'view_seller_contact_card.html', {'contact_card': contact_card})


def edit_contact_card(request):
    contact_card = get_object_or_404(ContactCard, user=request.user)

    if request.method == 'POST':
        form = EditContactCardForm(request.POST, instance=contact_card)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact Card updated successfully.')
            return redirect('base:view_contact_card')
    else:
        form = EditContactCardForm(instance=contact_card)

    return render(request, 'create_contact_card.html', {
        'form': form,
        'title': 'Edit Contact Card',
        'contact_card': contact_card
    })

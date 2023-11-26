from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect
from base.models import ContactCard
from .models import Item, Category
from django.contrib import messages
from base.forms import ContactCardForm
from base.models import ContactCard
from django.contrib.auth.decorators import login_required
from .forms import NewItemForm, EditItemForm
from django.db.models import Q

# Create your views here.


def detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)
    seller = item.created_by
    contact_card = get_object_or_404(ContactCard, user=request.user)
    return render(request, 'detail.html', {
        'item': item,
        'related_items': related_items,
        'seller': seller,
        'contact_card': contact_card
    })


@login_required
def new(request):
    try:
        contact_card = ContactCard.objects.get(user=request.user)
    except ContactCard.DoesNotExist:
        # If the user doesn't have a contact card, redirect them to create one
        messages.warning(request, 'You need to create a contact card before adding an item.')
        return redirect('base:create_contact_card')

    if request.method == 'POST':
        form = NewItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            messages.success(request, 'Item added successfully.')
            return redirect('item:detail', pk=item.id)
    else:
        form = NewItemForm()
    return render(request, 'form.html', {
        'form': form,
        'title': 'New Item',
        'contact_card': contact_card
    })


@login_required
def delete(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    item.delete()
    messages.error(request, 'Item deleted successfully.')
    return redirect('dashboard:dashboard')


@login_required
def edit(request, pk):
    item = get_object_or_404(Item, pk=pk, created_by=request.user)
    contact_card = get_object_or_404(ContactCard, user=request.user)
    if request.method == 'POST':
        form = EditItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item.save()
            messages.success(request, 'Item updated successfully.')
            return redirect('item:detail', pk=item.id)
    else:
        form = EditItemForm(instance=item)
    return render(request, 'form.html', {
        'form': form,
        'title': 'Edit Item',
        'contact_card': contact_card
    })


def items(request):
    query = request.GET.get('query', '')
    categories = Category.objects.all()
    category_id = request.GET.get('category', 0)
    contact_card = get_object_or_404(ContactCard, user=request.user)
    items = Item.objects.filter(is_sold=False)
    if category_id:
        items = items.filter(category_id=category_id)

    if query:
        items = items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    items = items[:4]
    return render(request, 'items.html', {
        'items': items,
        'query': query,
        'categories': categories,
        'category_id': int(category_id),
        'search_performed': bool(query),
        'contact_card': contact_card
    })


def items_by_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    contact_card = get_object_or_404(ContactCard, user=request.user)
    items = Item.objects.filter(category=category)

    return render(request, 'items_by_category.html', {
        'category': category,
        'items': items,
        'contact_card': contact_card
    })




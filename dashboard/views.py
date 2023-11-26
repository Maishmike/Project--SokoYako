from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from base.models import ContactCard
from item.models import Item


# Create your views here.


@login_required
def dash_index(request):
    items = Item.objects.filter(created_by=request.user)
    contact_card = get_object_or_404(ContactCard, user=request.user)
    return render(request, 'dash_index.html', {
        'items': items,
        'contact_card': contact_card
    })


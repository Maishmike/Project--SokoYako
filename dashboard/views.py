from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from base.models import ContactCard
from item.models import Item


# Create your views here.


@login_required
def dash_index(request):
    items = Item.objects.filter(created_by=request.user)
    if request.user.is_authenticated:
        try:
            contact_card = ContactCard.objects.get(user=request.user)
        except ContactCard.DoesNotExist:
            # Handle the case where the user doesn't have a contact card
            contact_card = None
    else:
        contact_card = None
    return render(request, 'dash_index.html', {
        'items': items,
        'contact_card': contact_card
    })


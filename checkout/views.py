from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': ' pk_test_51USCiaAHvthR4ZqECdI8H3JPgqIjhip8HdYBDgSLmh6OSCqrlSxZ0NWb0uP0EPfvXEV1dHWntyN5Q9lyBXToloK600ZBOkxdtl',
        'client_secret': 'test client secret',
       
    }

    return render(request, template, context)

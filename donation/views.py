from django.shortcuts import render, redirect
from authentications.models import User
from .models import DonationTransaction
# Create your views here.
def donation(request):
    if not 'email' in request.session.keys():
        return redirect('login')
    if request.method == 'POST':
        card_no = request.POST.get('card-no')
        card_expiry = request.POST.get('card-expiry')
        card_cvv = request.POST.get('card-cvv')
        amount = request.POST.get('donation-amount')

        user = User.objects.get(email = request.session['email'])
        DonationTransaction.objects.create(user = user, amount=amount, card_no = card_no)
    return render(request, 'donation.html', {})
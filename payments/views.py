from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import transaction, Wallet
from .utils import Payment
from django.views import View
import json
# Create your views here.


@login_required
def AddMoney(request):
    context = {}
    has_transaction = transaction.objects.filter(status=2, wallet=request.user.wallet).exists()
    if has_transaction == False:
        context['no_transaction_done'] = 1
    return render(request, 'payments/addmoney.html', context=context)


class Transaction(View):
    def post(self, request):
        data = json.loads(request.body)
        payobj = Payment()
        session_id, product_id = payobj.createSession(
            (int(data['amount'])*100), request.user)
        t = transaction(ID=product_id,
                        wallet=request.user.wallet, amount=float(data['amount']))
        t.save()
        return JsonResponse({'id': session_id})


def paymentSuccessful(request, transactionId):
    t = transaction.objects.filter(ID=transactionId).first()
    if t is not None:
        t.status = 2
        t.save()
        amount = t.amount
        amount += t.wallet.balanceamt
        t.wallet.balanceamt = amount
        amt_str = str(round((amount/1000),1))+'k'
        t.wallet.amt_str = amt_str
        t.save()
        t.wallet.save()
        return render(request, 'payments/successfull.html')
    return HttpResponse('<h1>Page Nont Found</h1>')


def paymentCancel(request, transactionId):
    t = transaction.objects.filter(ID=transactionId).first()
    if t is not None:
        t.status = 3
        t.save()
        return render(request, 'payments/cancel.html')
    return HttpResponse('<h1>Page Nont Found</h1>')

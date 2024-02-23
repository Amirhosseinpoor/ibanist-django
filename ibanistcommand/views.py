from django.shortcuts import render
from .Main import Ibanist


def ibanisthesabtosheba(request):
    if request.method == "POST":
        an1 = request.POST["an_h"]
        bank1 = request.POST["bank_h"]
        iban_output = Ibanist(an=an1, bank=bank1).__str__()['iban']
        an_output = Ibanist(an=an1, bank=bank1).__str__()['an']
        bank_output = Ibanist(an=an1, bank=bank1).__str__()['bank']
        return render(request, "output.html", {"iban": iban_output, "bank": bank_output, "an": an_output})
    return render(request, f'banks.html')


def ibanistshebatohesab(request):
    if request.method == "POST":
        iban1 = request.POST["iban_h"]

        iban_output = Ibanist(iban1).__str__()['iban']
        an_output = Ibanist(iban1).__str__()['an']
        bank_output = Ibanist(iban1).__str__()["bank"]
        return render(request, "output.html", {"iban": iban_output, "bank": bank_output, "an": an_output})
    return render(request, 'shebatohesab.html')


def ibanisthesabtosheba_keshavarzi(request):
    if request.method == "POST":
        an1 = request.POST["an_h"]
        bank1 = request.POST["bank_h"]
        iban_output = Ibanist(an=an1, bank=bank1).__str__()['iban']
        an_output = Ibanist(an=an1, bank=bank1).__str__()['an']
        bank_output = Ibanist(an=an1, bank=bank1).__str__()['bank']
        return render(request, "output.html", {"iban": iban_output, "bank": bank_output, "an": an_output})
    return render(request, f'benk_hesab_to_sheba/keshavarzi.html')


def ibanisthesabtosheba_tejarat(request):
    if request.method == "POST":
        an1 = request.POST["an_h"]
        bank1 = request.POST["bank_h"]
        iban_output = Ibanist(an=an1, bank=bank1).__str__()['iban']
        an_output = Ibanist(an=an1, bank=bank1).__str__()['an']
        bank_output = Ibanist(an=an1, bank=bank1).__str__()['bank']
        return render(request, "output.html", {"iban": iban_output, "bank": bank_output, "an": an_output})
    return render(request, f'benk_hesab_to_sheba/tejarat.html')



def ibanisthesabtosheba_refah(request):
    if request.method == "POST":
        an1 = request.POST["an_h"]
        bank1 = request.POST["bank_h"]
        iban_output = Ibanist(an=an1, bank=bank1).__str__()['iban']
        an_output = Ibanist(an=an1, bank=bank1).__str__()['an']
        bank_output = Ibanist(an=an1, bank=bank1).__str__()['bank']
        return render(request, "output.html", {"iban": iban_output, "bank": bank_output, "an": an_output})
    return render(request, f'benk_hesab_to_sheba/refah.html')

# Create your views here.

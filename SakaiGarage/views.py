
from django.shortcuts import render, redirect
from .models import SakaiGarage





def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        logbook = request.POST.get('logbook')
        make = request.POST.get('make')
        model = request.POST.get('model')
        chasis = request.POST.get('chasis')
        damages = request.POST.get('damages')
        insuarance = request.POST.get('insuarance')

        query = SakaiGarage.objects.create(name=name, email=email, phone=phone, logbook=logbook, make=make, model=model,  chasis=chasis, damages=damages, insuarance=insuarance)

        query.save()
        return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        logbook = request.POST.get('logbook')
        make = request.POST.get('make')
        model = request.POST.get('model')
        chasis = request.POST.get('chasis')
        damages = request.POST.get('damages')
        insuarance = request.POST.get('insuarance')

        edit_data = SakaiGarage.objects.get(id=id)
        edit_data.name = name
        edit_data.email = email
        edit_data.phone = phone
        edit_data.logbook = logbook
        edit_data.make = make
        edit_data.model = model
        edit_data.chasis = chasis
        edit_data.damages = damages
        edit_data.insuarance = insuarance
        edit_data.save()
        return redirect("/")

    dta = SakaiGarage.objects.get(id=id)
    context = {"dta": dta}
    return render(request, "edit.html", context)


def deleteData(request, id):
    d = SakaiGarage.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")

def indexpage(request):
    data = SakaiGarage.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)


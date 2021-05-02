from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Customers
# Create your views here.


def index(request):
    return render(request, 'index.html')


def emp(request):
    button = request.POST["b1"]
    if button == "Insert":
        name = request.POST["t2"]
        addr = request.POST["t3"]
        age = request.POST["t4"]
        gender = request.POST["gender"]
        location = request.POST["location"]
        try:
            chennai = request.POST['chennai']
        except:
            chennai = 0
        try:
            delhi = request.POST['delhi']
        except:
            delhi = 0
        try:
            bangalore = request.POST['bangalore']
        except:
            bangalore = 0
        try:
            jaipur = request.POST['jaipur']
        except:
            jaipur = 0
        dob = request.POST["dob"]
        covid = request.POST["positive"]
        pic = (request.FILES["picture"])
        budget = request.POST["budget"]

        obj = Customers.objects.create(
            name=name, address=addr, age=age, gender=gender, location=location, dob=dob, covid=covid, pic=pic, budget=budget, chennai=chennai, delhi=delhi, bangalore=bangalore, jaipur=jaipur)

        msg = "Record Inserted"
        return render(request, 'result.html', {'msg': msg})

    elif button == "Select":
        id = request.POST['t1']
        obj = Customers.objects.get(pk=id)
        return render(request, 'result.html', {'obj': obj})

    elif button == "Update":

        id = request.POST["t1"]
        name = request.POST["t2"]
        addr = request.POST["t3"]
        age = request.POST["t4"]
        gender = request.POST["gender"]
        location = request.POST["location"]
        dob = request.POST["dob"]
        pic = (request.FILES["picture"])
        budget = request.POST["budget"]
        try:
            chennai = request.POST['chennai']
        except:
            chennai = 0
        try:
            delhi = request.POST['delhi']
        except:
            delhi = 0
        try:
            bangalore = request.POST['bangalore']
        except:
            bangalore = 0
        try:
            jaipur = request.POST['jaipur']
        except:
            jaipur = 0

        obj = Customers.objects.get(pk=id)
        obj.name = name
        obj.address = addr
        obj.age = age
        obj.gender = gender
        obj.location = location
        obj.dob = dob
        obj.pic = pic
        obj.chennai = chennai
        obj.delhi = delhi
        obj.bangalore = bangalore
        obj.jaipur = jaipur

        obj.budget = budget

        obj.save()
        msg = "record updated"
        return render(request, 'result.html', {'msg': msg})

    elif button == "Delete":
        id = request.POST['t1']
        obj = Customers.objects.get(pk=id)
        obj.delete()
        msg = "record deleted"
        return render(request, 'result.html', {'msg': msg})

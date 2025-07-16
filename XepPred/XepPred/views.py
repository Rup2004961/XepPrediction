from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse
import pickle 
import os
from django.conf import settings

model_path = os.path.join(settings.BASE_DIR,"rfc.pkl")


with open(model_path,"rb") as file :
   model = pickle.load(file)

#model_path = os.path.join(settings.BASE_DIR,"rfc.pkl") 
#with open("rfc.pkl","rb") as file:
#  model = pickle.load(file)


def home(request):
    pred = None
    if request.method == "POST":
        temp = request.POST['temp']
        humidity = request.POST['humidity']
        ph = request.POST['ph']
        water = request.POST['water']

        #model_path =os.path.join(settings.BASE_DIR,"rfc.pkl") 
        #print(model_path)
       #print(temp)
       #print(humidity)
       #print(ph)
       #print(water)

        env = [[temp,humidity,ph,water]] 

        pred = model.predict(env)
        print(pred)
        
    return render(request,"home.html", {"prediction": pred})



def about(request):
    return render(request,"about.html")

def contact(request):
    return render(request,"contact.html")
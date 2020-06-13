from django.shortcuts import render
import requests   #3 библиотека для парсинга
from .models import City
from .form import CityForm

def index(request):
    appID='f76fb4214da5a35aa7be9c394408a478' #взято из сайта weather 
    url='https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+appID #ссылка для того чтобы брать инфу 
     #город с рогодой
    
    citis=City.objects.all()
    
    if(request.method=='POST'):
        form = CityForm(request.POST)
        form.save()

    form=CityForm()

    allcitys =[] #пустой список 

    for city in citis:
        res=requests.get(url.format(city.name)).json()#url.format() вставляет в ссылку город requests.get() функция для парсинга json() переброзования в колекцию  
        city_info={  #массив для всех єлементов 
            'city':city.name,
            'temp':res['main']['temp'],
            'icon':res['weather'][0]['icon']
        }
        allcitys.append(city_info)

    
    context={'all_info':allcitys,'form':form}
 
    #res2 = requests.get('https://api.github.com/user', auth=('user', 'pass'))
    #print(res2.text)
    


 

    return render(request,'weather/index.html',context)  
# Create your views here.

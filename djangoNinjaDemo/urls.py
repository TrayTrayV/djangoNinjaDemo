from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

api = NinjaAPI()

#Addition
@api.get("/add")
def add(request, a:float, b:float):
    result = int(a) + int(b)
    return {"result": result}


#Substraction
@api.get("/sub")
def add(request, a:float, b:float):
    result = int(a) - int(b)
    return {"result": result}

#Multiplication
@api.get("/mul")
def add(request, a:float, b:float):
    result = int(a) * int(b)
    return {"result": result}

#Division
@api.get("/div")
def add(request, a:float, b:float):
    result = int(a) / int(b)
    return {"result": result}


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", api.urls),
]

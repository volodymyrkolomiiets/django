from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Menu


# def index(request, name):
#     return HttpResponse(f"<h1> Hello  {name}</h1>")

def my_view(request, name):
    template = loader.get_template("hello.html")
    # context = {}
    # return HttpResponse(template.render(context, request))
    return render(request, "hello.html", {
                                        "name":name,
                                        "nums": [1, 2, 3, 4, 5, 6, 7, 8, 9],
                                        "my_string": "Simple is better then complex",
                                        })

def about(request):
    about_content = {"about": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."}
    return render(request, "about.html", about_content)

def index(request, name):
    # person = {"name": name,
    #            "profession": "Teacher"}
    # return render(request, "index.html", {"person": person})
    
    context = {"user": "admin"}
    return render(request, "index.html", context)
    
    

def myview(request):
    langs = ["python", "Java", "PHP", "Ruby", "Rust"]
    return render(request, "langs.html", {"langs": langs})

def menu(request):
    # menuitem = {"name": "Greek Salad"}
    new_menu = {"mains": [
        {"name": "falafel", "price": "12"},
        {"name": "shawarna", "price": "15"},
        {"name": "gyro", "price": "10"},
        {"name": "humus", "price": "5"},
    ]}
    return render(request, "menu.html", new_menu)

def menu_by_id(request):
    newmenu = Menu.objects.all()
    new_menu_dict = {"menu": newmenu}
    return render(request, "menu_cards.html", new_menu_dict)
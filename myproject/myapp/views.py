from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request, name):
    return HttpResponse(f"<h1> Hello  {name}</h1>")

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
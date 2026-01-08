from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    # name = input("Enter your name: ")
    # return HttpResponse("Hello, {}! <br> This is coming from HttpResponse".format(name))

    return HttpResponse(
        """<h2>Hello, Pratham! <br></h2>
                         This is coming from HttpResponse 
                         <br><hr>
                        <h2>How's it going brother?</h2>"""
    )


def template_response(request):
    return render(request, "home/index.html")

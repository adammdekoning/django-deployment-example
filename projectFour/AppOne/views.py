from django.shortcuts import render


# Create your views here.
def base(request):
    return render(request, 'AppOne/base.html')


def other(request):
    return render(request, 'AppOne/other.html')

def index(request):
    context_dict = {'text':'hello, world', 'number':100}
    return render(request, 'AppOne/index.html', context_dict)



def relative(request):
    return render(request, 'AppOne/relative_url.html')

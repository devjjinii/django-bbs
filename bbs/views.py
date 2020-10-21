from django.shortcuts import render
from bbs.forms import Form


# Create your views here.
def write(request):
    form = Form()
    return render(request, 'write.html', {'form': form})

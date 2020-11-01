from django.shortcuts import render
from bbs.forms import Form
from bbs.models import Article

# Create your views here.
def write(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()

    return render(request, 'write.html', {'form': form})


def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList': articleList})

def view(request, id):
    article = Article.objects.get(pk=id)
    return render(request, 'view.html', {'article': article})
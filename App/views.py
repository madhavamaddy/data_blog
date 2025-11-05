from django.db import IntegrityError
from django.shortcuts import render,redirect
from . models import Post,Author

def test(request):


    if request.method == 'POST':

        title = request.POST.get('title')
        content = request.POST.get('content')
        name = request.POST.get('name')
        email_id = request.POST.get('email')


        if Author.objects.filter(name = name,email=email_id).exists():
            return render(request, 'form.html', {'error': 'Email already exists. Try a different one.'})
        # try:
        #     author = Author.objects.create(id = author_id,email=email_id)
        # except IntegrityError:
        #     return render(request,'form.html',{'err':'email already exits'})
        else:
            author = Author.objects.create(name=name,email=email_id)
            Post.objects.create(title=title,content = content,author=author)
            return redirect('success')
    
    return render(request,'form.html')

def success(request):
    return render(request,'succes.html')
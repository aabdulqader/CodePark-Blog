from django.shortcuts import render, HttpResponse
from blog.models import Blog,Contact
from django.core.paginator import Paginator
import math
def home(request):
    return render(request, "index.html")
def blog(request):
    num_of_posts = 4
    page = request.GET.get('page')
    if page == None:
        page=1
    else:
        page = int(page)
    blogs = Blog.objects.all()
    length = len(blogs)
    blogs = blogs[(page- 1)*num_of_posts:page*num_of_posts]
    if page>1:
        prev = page-1
    else:
        prev = None
    if page<math.ceil(length/num_of_posts):
        nxt= page+1
    else:
        nxt = None   
    context = {'blogs': blogs,'prev':prev, 'nxt':nxt}
    return render(request, "bloghome.html", context)
def blogpost(request, slug):
    blog = Blog.objects.filter(slug=slug).first()
    context = {'blog':blog}
    return render(request, 'blogpost.html', context)
    #return HttpResponse(f"You are viewing {slug}")
def search(request):
    return render(request, "search.html")
def contact(request):
    #return HttpResponse('this is my contact page{/contact}')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        ins = Contact(name=name, email=email, phone=phone,desc=desc)
        ins.save()
        print('the data has been written to db')
    return render(request, 'contact.html')
def about(request):
    return render(request, "about.html")

def allblogs(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, "allblogs.html", context)

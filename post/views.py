from django.shortcuts import render,HttpResponse,get_object_or_404,HttpResponseRedirect,redirect,Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from  django.utils.text import slugify

def post_index(request):
    posts=Post.objects.all()
    return render(request,'post/index.html',{'posts':posts})


def post_detail(request,id):
    post=get_object_or_404(Futbol,id=id)
    context={
        'post':post
    }
    return render(request,'post/detail.html',context)

def post_create(request):
    if not request.user.is_authenticated:
       return Http404
    #if request.method=="POST":
        # print(request.POST)
    #title=request.POST.get('title')
    #content=request.POST.get('content')
    #Post.objects.create(title=title,content=content)
   # if request.method=="POST":
     #   form=PostForm(request.POST)
     #   print(form.is_valid())
     #   if form.is_valid():
     #       form.save()
    #else:
    #    form = PostForm()# formu kulalnıcıya geri döndür
    #context = {
    #    'form':form,
    #}
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post=form.save()
        messages.success(request,"Başarılı bir şekilde oluştur")
        return HttpResponseRedirect(post.get_absolute_url())
    context = {
        'form':form,
    }
    return render(request ,'post/form.html',context)

def post_update(request,id):
    if not request.user.is_authenticated:
        return Http404
    post=get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None,request.FILES or None,instance=post)# gelen değer varsa al yıksa bos
    if form.is_valid():
        form.save()
        messages.success(request,"Başarılı bir şekilde oluştur")

        return HttpResponseRedirect(post.get_absolute_url())

    context = {
        'form':form,
    }
    return render(request,'post/form.html',context)
def post_delete(request,id):
    if not request.user.is_authenticated:
        return Http404
    post=get_object_or_404(Post,id=id)
    post.delete()
    return redirect('post:index')


from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .models import Post,BlogComment

from django.contrib import messages

# Create your views here.
def bloghome(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request,'blog/home.html',context);

def blogpost(request,slug):
    post=Post.objects.filter(slug=slug).first();
    comments=BlogComment.objects.filter(post=post)
    context={"post":post,"comments":comments,'user':request.user};
    return render(request,'blog/blogpost.html',context);

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if(len(comment)<1):
            messages.success(request,"Please writes somethings")
        elif(parentSno==""):    
            comment=BlogComment(comment= comment, user=user, post=post)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent= BlogComment.objects.get(sno=parentSno)
            comment=BlogComment(comment= comment, user=user, post=post,parent=parent)
            comment.save()
            messages.success(request, "Your comment has been posted successfully")
    return redirect(f"/blog/{post.slug}")
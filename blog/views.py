from django.shortcuts import render,HttpResponse
from .models import Post

# Create your views here.
def blogHome(request):
    allPosts = Post.objects.all()
    context = {'allPosts': allPosts}
    return render(request,"blog/blogHome.html",context)
    # return HttpResponse('This is blogHome. We will keep all the the blog posts here')


def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html',context)
    # return HttpResponse(f'This is blogPost: {slug}')


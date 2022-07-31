from django.shortcuts import render, redirect

from contact.models import Subscribe
from mooses.models import *
from django.core.paginator import Paginator


def index(request):
    posts = Blog.objects.filter(is_published=True)
    # subscribe
    email = request.POST.get('email')
    if email:
        Subscribe.objects.create(email=email)
        return redirect('index')

    context = {'posts': posts}
    return render(request, 'mooses/index.html', context)


def blog(request):
    posts = Blog.objects.all().order_by('-id')
    category = Category.objects.all()
    tags = Tag.objects.all()
    # pagination
    p = Paginator(posts, 1)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    # subscribe
    email = request.POST.get('email')
    if email:
        Subscribe.objects.create(email=email)
        return redirect('blog')

    context = {'posts': posts_, 'category': category, 'tags': tags, 'p': p}
    return render(request, 'mooses/blog.html', context)


def about(request):
    about = About.objects.all()
    # subscribe
    email = request.POST.get('email')
    if email:
        Subscribe.objects.create(email=email)
        return redirect('about')

    context = {'about': about}
    return render(request, 'mooses/about.html', context)


# def blog_detail(request, id):
#     postobj = Blog.objects.get(pk=id)
#     comments = Comment.objects.filter(post=id)
#     form = CommentForm()
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.post = postobj
#             obj.save()
#             messages.success(request, 'Your comment sent successfully')
#             return redirect('blog-detail', id)
#     context = {'post': postobj, 'form': form, 'comments': comments}
#     return render(request, 'mooses/blog-single.html', context)

def blog_detail(request, id):
    post = Blog.objects.get(pk=id)
    # comment
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        name = request.POST.get('name')
        website = request.POST.get('website')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        Comment.objects.create(post=post, name=name, website=website, email=email, message=msg)
        return redirect('blog-detail', id)
    # subscribe
    email = request.POST.get('email')
    if email:
        Subscribe.objects.create(email=email)
        return redirect('blog-detail', id)

    context = {'post': post, 'comments': comments}
    return render(request, 'mooses/blog-single.html', context)


def get_tag(request, id):
    tags = Tag.objects.all()
    tag = Tag.objects.get(pk=id)
    posts = Blog.objects.filter(tag=tag)
    # pagination
    p = Paginator(posts, 1)
    page = request.GET.get('page')
    posts_ = p.get_page(page)
    # subscribe
    email = request.POST.get('email')
    if email:
        Subscribe.objects.create(email=email)

    context = {'tags': tags, 'posts': posts_, 'p': p}
    return render(request, 'mooses/tag.html', context)

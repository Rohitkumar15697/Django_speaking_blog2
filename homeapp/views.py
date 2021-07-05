from django.shortcuts import redirect, render,render,HttpResponse,get_object_or_404
from django.http import HttpResponseRedirect
from blog.models import blogpost,CommentModel
import random
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView
from django.urls import reverse_lazy,reverse
from blog.forms import Myblogform
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q

# Create your views here.

def index(request):
    count=len(blogpost.objects.all())
    postdata=list(blogpost.objects.all()[:30])
    
    #This is for showing topic names in index page
    topic_names=blogpost.objects.values_list('topic',flat=True).distinct() 
    
     

    blog_data=postdata[:3]
    
    return render(request,'index.html',{'data':postdata,'blog_data':blog_data,'topics':topic_names,'count':count})


def search_result(request):
    search_element=request.GET.get('search_me')
    if search_element=="":
        return HttpResponse('No data for search!')
    else:
        search_data=blogpost.objects.all().filter(Q(title__icontains=search_element) | Q(topic__icontains=search_element))
        count=len(search_data)
        print(search_result)
    
    return render(request,'search_result.html',{'searched':search_element,'result':search_data,'count':count})



#Listing the blogs when we click on all blogs from index page

class ListData(ListView):
    model=blogpost
    template_name='blogpost_list.html'
    def get_queryset(self):
        return blogpost.objects.all().order_by('topic')

        

#detail of every blog when we click on any blog title

class DetailData(DetailView):
    model=blogpost
    template_name='blogpost_detail.html'
    context_object_name='data'


'''
#This code is for update blog post
@method_decorator(login_required, name='dispatch')
class UpdateBlog(UpdateView):
    model=blogpost
    template_name='edit_blog.html'
    '''
   

@method_decorator(login_required, name='dispatch')
class EditBlog(UpdateView):
    model=blogpost
    template_name='edit_blog.html'
    fields=['topic','title','post']
    success_url=reverse_lazy('profile')



#Delete the blog post with this view class

class DeleteBlog(DeleteView):
    model=blogpost
    template_name='delete_blog.html'
    success_url=reverse_lazy('profile') #This shows- When delete is successfull then where to go!


class user_blogs(ListView):
    model=blogpost
    template_name='blogpost_list.html'
    def get_queryset(self):
        return blogpost.objects.all().filter(created_by=self.request.user)
    
'''
class category_list(ListView):
    model=blogpost
    template_name='blogpost_list.html'
    def get_queryset(self):
        return blogpost.objects.all().filter(topic=self.request.GET.get('cate'))'''

@login_required(login_url='index')
def like_post(request, pk):
    post=get_object_or_404(blogpost, id=request.POST.get('like'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('detaildata',args=[str(pk)]))
    


def comment_view(request, pk):
    if request.method=='POST' and 'comment_button' in request.POST:
        
        body=request.POST.get('comment_text')
        post=get_object_or_404(blogpost, id=pk)
        obj=CommentModel(body=body)
        obj.name=request.user
        obj.post=post
        obj.save()
        return HttpResponseRedirect(reverse('detaildata',args=[str(pk)]))

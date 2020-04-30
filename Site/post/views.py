from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,DeleteView,DetailView,UpdateView,ListView
from .models import *
from django.http import HttpResponseRedirect
from .forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy,reverse
# Create your views here.

class PostList(LoginRequiredMixin,ListView):
    model=Post
    template_name = 'post/post_list'


class CreatePost(LoginRequiredMixin,CreateView):
    form_class=PostForm
    template_name='post/post_create.html'
    success_url = reverse_lazy('post:post_list')


    def form_valid(self,form):
        self.object=form.save(commit=False)
        self.object.created_by=self.request.user
        #self.object.image=self.request.FILES['image']
        self.object.save()
        return super().form_valid(form)
'''
class CommentView(CreateView):
    form_class =CommentForm
    template_name='app/comment_form.html'
    success_url=reverse_lazy('app:detail' ,kwargs={'pk':self.pk} )

    def form_valid(self, form):
        self.object=form.save(commit=False)
        self.object.on_post=get_object_or_404(Post,pk=form.cleaned_data['list_pk'])
        self.object.user=self.request.user
        self.object.save()
        return super().form_valid(form)
        '''

class PostDetailView(LoginRequiredMixin,DetailView):
    model=Post
    template_name = 'post/post_detail.html'

@login_required
def commentCreate(request,pk):
    form=CommentForm()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            form=form.save(commit=False)
            form.on_post=get_object_or_404(Post,pk=pk)
            form.user=request.user
            form.save()
            return HttpResponseRedirect(reverse('post:detail',kwargs={'pk':pk}))
    return render(request,'post/comment_form.html',{'form':form})




class DeletePost(LoginRequiredMixin,DeleteView):
    model=Post
    success_url = reverse_lazy('post:post_list')
    template_name='post/post_delete_confirm.html'



class DeleteComment(LoginRequiredMixin,DeleteView):
    model=Comment
    success_url = reverse_lazy('post:detail', )
    template_name = 'post/post_delete_confirm.html'
@login_required
def deleteCommment(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post=comment.on_post
    comment.delete()
    return HttpResponseRedirect(reverse('post:detail',kwargs={'pk':post.pk}))


class EditPost(LoginRequiredMixin,UpdateView):
    form_class=PostForm
    model = Post
    template_name='post/post_create.html'
    success_url = reverse_lazy('post:post_list')


class EditComment(LoginRequiredMixin,UpdateView):
    model=Comment
    form_class = CommentForm
    template_name='post/comment_form.html'


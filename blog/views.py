from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404, HttpResponseServerError
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Adoption, Rehome
from .forms import CommentForm, AdoptionForm, RehomeForm, PostCreateForm
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView


class AdoptionView(TemplateView):
    template_name = "adoption.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adoption_form'] = AdoptionForm()
        return context
    
    def post(self, request, *args, **kwargs):
        adoption_form = AdoptionForm(request.POST)
        if adoption_form.is_valid():
            adoption = adoption_form.save(commit=False)
            adoption.author = request.user
            adoption.save()
            messages.success(self.request, 'Your adoption request has been posted successfully')
            return redirect(reverse('adoption_detail', args=[adoption.id]))
          
        context = self.get_context_data()
        context['adoption_form'] = adoption_form
        return self.render_to_response(context)

class AdoptionDetailView(DetailView):
    model = Adoption
    template_name = "adoption_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        adoption = get_object_or_404(Adoption, pk=pk)
        context['adoption'] = adoption
        return context
    
    def get(self, request, *args, **kwargs):
        
        try:
            pk = self.kwargs.get('pk') 
            return super().get(request, *args, **kwargs)

        except Http404:
            return render(request, 'no_adoption.html')
        

class AdoptionUpdateView(UpdateView):
    model = Adoption
    form_class = AdoptionForm
    template_name = "update_adoption.html"
    
    def get_success_url(self):
        messages.success(self.request, 'Your update has been successful')
        return reverse('adoption_detail', kwargs={'pk': self.object.pk})

class DeleteAdoptionView(DeleteView):
    model = Adoption
    template_name = "delete_adoption.html"
    success_url = reverse_lazy('adoption')
    
    def post(self, request, *args, **kwargs):
        adoption = self.get_object()
        adoption.delete()
        messages.success(self.request, 'Your deletion has been successful')
        return redirect(self.success_url)


class RehomeView(TemplateView):
    template_name = "rehome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rehome_form'] = RehomeForm()
        return context
    
    def post(self, request, *args, **kwargs):
        rehome_form = RehomeForm(request.POST)
        if rehome_form.is_valid():
            rehome = rehome_form.save(commit=False)
            rehome.author = request.user
            rehome.save()
            messages.success(self.request, 'Your rehoming request has been posted successfully')
            return redirect(reverse('rehome_detail', args=[rehome.id]))
            
        context = self.get_context_data()
        context['rehome_form'] = rehome_form
        return self.render_to_response(context)


class RehomeDetailView(TemplateView):
    model = Rehome
    template_name = "rehome_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        rehome = get_object_or_404(Rehome, pk=pk)
        context['rehome'] = rehome
        return context
    
    def get(self, request, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk') 
            return super().get(request, *args, **kwargs)

        except Http404:
            return render(request, 'no_rehome.html')

class RehomeUpdateView(UpdateView):
    model = Rehome
    form_class = RehomeForm
    template_name = "update_rehome.html"
    
    def get_success_url(self):
        messages.success(self.request, 'Your update has been successful')
        return reverse('rehome_detail', kwargs={'pk': self.object.pk})

class DeleteRehomeView(DeleteView):
    model = Rehome
    template_name = "delete_rehome.html"
    success_url = reverse_lazy('rehome')
    
    def post(self, request, *args, **kwargs):
        rehome = self.get_object()
        rehome.delete()
        messages.success(self.request, 'Your deletion has been successful')
        return redirect(self.success_url)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)   
        context['post_create_form'] = PostCreateForm()
        return context

    def post(self, request, *args, **kwargs):
        post_create_form = PostCreateForm(request.POST)
        if post_create_form.is_valid():
            post = post_create_form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(request, 'Your post is awaiting approval')

            return redirect('blog.html', slug=post.slug)
        else:
            context = self.get_context_data()
            context['post_create_form'] = post_create_form
            return self.render_to_response(context)


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1) 
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )
        def dispatch(self, request, *args, **kwargs):
            try:
                return super().dispatch(request, *args, **kwargs)
            except Post.DoesNotExist:
                return HttpResponseServerError("Post not found.")


class AboutView(TemplateView):
    template_name = "about.html"

    
class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

class HomeView(TemplateView):
    template_name = "index.html"

class PostComment(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)

        if post.comment.filter(id=request.user.id).exists():
            post.comment.remove(request.user)
        else:
            post.comment.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

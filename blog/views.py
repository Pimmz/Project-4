from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .models import Adoption, Rehome
from .forms import CommentForm, AdoptionForm, RehomeForm
from django.views.generic import TemplateView


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
            return redirect(reverse('adoption_detail', args=[adoption.id]))
          
        context = self.get_context_data()
        context['adoption_form'] = adoption_form
        return self.render_to_response(context)

class AdoptionDetailView(TemplateView):
    template_name = "adoption_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adoption'] = get_object_or_404(Adoption, pk=self.kwargs['pk'])
        return context

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
            return redirect(reverse('rehome_detail', args=[rehome.id]))
            
        context = self.get_context_data()
        context['rehome_form'] = rehome_form
        return self.render_to_response(context)

class RehomeDetailView(TemplateView):
    template_name = "rehome_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rehome'] = get_object_or_404(Rehome, pk=self.kwargs['pk'])
        return context

class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6


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

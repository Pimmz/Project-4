from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404, HttpResponseServerError
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Adoption, Rehome
from .forms import CommentForm, AdoptionForm, RehomeForm, PostCreateForm, PostUpdateForm
from django.views.generic import TemplateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class AdoptionView(TemplateView):
    template_name = "adoption.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adoption_form'] = AdoptionForm()
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        adoption_form = AdoptionForm(request.POST)
        if adoption_form.is_valid():
            adoption = adoption_form.save(commit=False)
            adoption.author = request.user
            adoption.save()

            messages.success(
                self.request, 'Your adoption request has been posted successfully. You will be contacted shortly.')
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
        context['user'] = self.request.user
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
        context = {}
        context['user'] = self.request.user
        messages.success(self.request, 'Your update has been successfull')
        return reverse('adoption_detail', kwargs={'pk': self.object.pk})


class DeleteAdoptionView(DeleteView):
    model = Adoption
    template_name = "delete_adoption.html"
    success_url = reverse_lazy('adoption')

    def post(self, request, *args, **kwargs):
        context = {}
        context['user'] = self.request.user
        adoption = self.get_object()
        adoption.delete()
        messages.success(self.request, 'Your deletion has been successfull')
        return redirect(self.success_url)


@method_decorator(login_required, name='dispatch')
class RehomeView(TemplateView):
    template_name = "rehome.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rehome_form'] = RehomeForm()
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        rehome_form = RehomeForm(request.POST)
        if rehome_form.is_valid():
            rehome = rehome_form.save(commit=False)
            rehome.author = request.user
            rehome.save()
            messages.success(
                self.request, 'Your rehoming request has been posted successfully. You will be contacted shortly.')
            return redirect(reverse('rehome_detail', args=[rehome.id]))

        context = self.get_context_data()
        context['rehome_form'] = rehome_form
        return self.render_to_response(context)


class RehomeDetailView(TemplateView):
    model = Rehome
    template_name = "rehome_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
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
        context = {}
        context['user'] = self.request.user
        messages.success(self.request, 'Your update has been successful')
        return reverse('rehome_detail', kwargs={'pk': self.object.pk})


class DeleteRehomeView(DeleteView):
    model = Rehome
    template_name = "delete_rehome.html"
    success_url = reverse_lazy('rehome')

    def post(self, request, *args, **kwargs):
        context = {}
        context['user'] = self.request.user
        rehome = self.get_object()
        rehome.delete()
        messages.success(self.request, 'Your deletion has been successful')
        return redirect(self.success_url)


@method_decorator(login_required, name='dispatch')
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(
        status=1, approved=True).order_by("-created_on")
    template_name = "blog.html"
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_create_form'] = PostCreateForm()
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        post_create_form = PostCreateForm(request.POST, request.FILES)
        if post_create_form.is_valid():
            post = post_create_form.save(commit=False)
            post.author = request.user
            post.save()

            messages.success(request, 'Your post is awaiting approval')

            return redirect('blog')
        else:
            context = self.get_context_data()
            context['post_create_form'] = post_create_form

            return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        context = {}
        context['user'] = self.request.user
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
        context['user'] = self.request.user
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


class DeletePostView(DeleteView):
    model = Post
    template_name = "delete_post.html"
    success_url = reverse_lazy('blog')

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        if post.author == request.user:
            post.delete()
            messages.success(self.request, 'Your deletion has been successful')
        else:
            messages.error(
                request, 'You do not have permission to delete this post')
        return redirect(self.success_url)

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except Post.DoesNotExist:
            return HttpResponseServerError("Post not found.")


class UpdatePostView(UpdateView):
    model = Post
    form_class = PostUpdateForm
    template_name = "update_post.html"

    def get_success_url(self):
        messages.success(self.request, 'Your update has been successful')
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        context = {}
        context['user'] = self.request.user
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class HomeView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


@method_decorator(login_required, name='dispatch')
class PostComment(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        context['user'] = self.request.user

        if post.comment.filter(id=request.user.id).exists():
            post.comment.remove(request.user)
        else:
            post.comment.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))

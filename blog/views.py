"""Views"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect, Http404, HttpResponseServerError
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Post, Adoption, Rehome
from .forms import CommentForm, AdoptionForm, RehomeForm, PostCreateForm
from .forms import PostUpdateForm
from django.views.generic import TemplateView, UpdateView, View
from django.views.generic import DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@method_decorator(login_required, name='dispatch')
class AdoptionView(TemplateView):
    """
    View for the Adoption page hwere you can submit a form
    """
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
                self.request,
                'Your request has been posted successfully.'
                'You will be contacted shortly.')
            return redirect(reverse('adoption_detail', args=[adoption.id]))

        context = self.get_context_data()
        context['adoption_form'] = adoption_form
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class AdoptionDView(View):
    """
    View for the Adoption detail page where you can view the form submitted. 
    The view name AdoptionDView is because it was originally called 
    Adoptiondetailview to match the template name but it caused an issue with 
    a single view so the name was changed to stop that and so that it didnt 
    match any other names.
    """
    model = Adoption
    template_name = "adoption_detail.html"

    def get(self, request, *args, **kwargs):
        adoption = Adoption.objects.filter(author=request.user).first()

        if adoption is not None:
            context = {'adoption': adoption, 'user': request.user}
            return render(request, self.template_name, context)
        else:
            return render(request, 'no_adoption.html')


@method_decorator(login_required, name='dispatch')
class AdoptionUpdateView(UpdateView):
    """
    View for the update Adoption page where you can update the form submitted
    """
    model = Adoption
    form_class = AdoptionForm
    template_name = "update_adoption.html"

    def get_success_url(self):
        context = {}
        context['user'] = self.request.user
        messages.success(self.request, 'Your update has been successfull')
        return reverse('adoption_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class DeleteAdoptionView(DeleteView):
    """
    View for the delete Adoption page where you can delete the form submitted
    """
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
    """
    View for the Rehome page where you can submit the form
    """
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
                self.request,
                'Your request has been posted successfully.'
                'You will be contacted shortly.')
            return redirect(reverse('rehome_detail', args=[rehome.id]))

        context = self.get_context_data()
        context['rehome_form'] = rehome_form
        return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class RehomeDetailView(TemplateView):
    """
    View for the Rehome detail page where you can view the form submitted
    """
    model = Rehome
    template_name = "rehome_detail.html"

    def get(self, request, *args, **kwargs):
        rehome = Rehome.objects.filter(author=request.user).first()

        if rehome is not None:
            context = {'rehome': rehome, 'user': request.user}
            return render(request, self.template_name, context)
        else:
            return render(request, 'no_rehome.html')


@method_decorator(login_required, name='dispatch')
class RehomeUpdateView(UpdateView):
    """
    View for the update Rehome page where you can update the form submitted
    """
    model = Rehome
    form_class = RehomeForm
    template_name = "update_rehome.html"

    def get_success_url(self):
        context = {}
        context['user'] = self.request.user
        messages.success(self.request, 'Your update has been successful')
        return reverse('rehome_detail', kwargs={'pk': self.object.pk})


@method_decorator(login_required, name='dispatch')
class DeleteRehomeView(DeleteView):
    """
    View for the delete Rehome page where you can delete the form submitted
    """
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
    """
    View for the Postroom page "blog.html" where you can post images and text
    """
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

            messages.success(
                request, 'Your post was successful and awaiting approval')

            return redirect('blog')
        else:
            context = self.get_context_data()
            context['post_create_form'] = post_create_form

            return self.render_to_response(context)


@method_decorator(login_required, name='dispatch')
class PostDetail(View):
    """
    View for the Postroom page "post_detail" displays information about a post
    and allows for commenting
    """

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


@method_decorator(login_required, name='dispatch')
class PostComment(View):
    """
    View for the post detail page for adding and removing comments
    """

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        context['user'] = self.request.user

        if post.comment.filter(id=request.user.id).exists():
            post.comment.remove(request.user)
        else:
            post.comment.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    """
    View for the delete Post page where you can delete the post submitted
    """
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


@method_decorator(login_required, name='dispatch')
class UpdatePostView(UpdateView):
    """
    View for the Update Post page where you can update the post submitted
    """
    model = Post
    form_class = PostUpdateForm
    template_name = "update_post.html"

    def get_success_url(self):
        messages.success(self.request, 'Your update has been successful')
        return reverse_lazy('post_detail', kwargs={'slug': self.object.slug})


@method_decorator(login_required, name='dispatch')
class PostLike(View):
    """
    View for the Post detail page where you can like or unlike a post
    """

    def post(self, request, slug, *args, **kwargs):
        context = {}
        context['user'] = self.request.user
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AboutView(TemplateView):
    """
    View for the About page
    """
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class HomeView(TemplateView):
    """
    View for the Home page
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class custom_400(View):
    """
    View for the 400 error page
    """
    def custom_400(request, exception):
        return render(request, '400.html', status=400)


class custom_403(View):
    """
    View for the 403 error page
    """
    def custom_403(request, exception):
        return render(request, '403.html', status=403)


class custom_404(View):
    """
    View for the 404 error page
    """
    def custom_404(request, exception):
        return render(request, '404.html', status=404)


class custom_500(View):
    """
    View for the 500 error page
    """
    def custom_500(request, exception):
        return render(request, '500.html', status=500)

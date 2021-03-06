from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from WVWebsite.app.models import Post, About, Ordinance


def render_page(request):
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return redirect("Home")


def home(request, username=None):
    first_name = ""
    last_name = ""
    if username:
        user = User.objects.get(username=username)
        first_name = user.first_name
        last_name = user.last_name
        post_list = Post.objects.filter(user=user)
    else:
        post_list = Post.objects.all()

    post_list = post_list.order_by("-pub_date")

    paginator = Paginator(post_list, 5)  # Show NUM_OF_PAGES posts per page
    page = request.GET.get("page")

    posts = paginator.get_page(page)
    abouts = About.objects.all()
    ordinances = Ordinance.objects.all()

    return render(
        request,
        "home.html",
        {
            "posts": posts,
            "first_name": first_name,
            "last_name": last_name,
            "abouts": abouts,
            "ordinances": ordinances,
        },
    )


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "body"]
    template_name = "create_post.html"
    login_url = reverse_lazy("login")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ["title", "body"]
    template_name = "create_post.html"
    login_url = reverse_lazy("login")

    def test_func(self):
        return Post.objects.get(id=self.kwargs["pk"])


class AboutUpdate(LoginRequiredMixin, UpdateView):
    model = About
    fields = ["content"]
    template_name = "update_about.html"
    login_url = "/accounts/google/login/"
    success_url = reverse_lazy("Home")

    def test_func(self):
        return About.objects.get(id=self.kwargs["pk"])


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("Home")
    login_url = reverse_lazy("login")
    template_name = "post_confirm_delete.html"

    def test_func(self):
        return Post.objects.get(id=self.kwargs["pk"])


class OrdinanceCreate(LoginRequiredMixin, CreateView):
    model = Ordinance
    fields = ["link", "title"]
    template_name = "create_ordinance.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("Home")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class OrdinanceUpdate(LoginRequiredMixin, UpdateView):
    model = Ordinance
    fields = ["link", "title"]
    template_name = "create_ordinance.html"
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("Home")

    def test_func(self):
        return Ordinance.objects.get(id=self.kwargs["pk"])


class OrdinanceDelete(LoginRequiredMixin, DeleteView):
    model = Ordinance
    success_url = reverse_lazy("Home")
    login_url = reverse_lazy("login")
    template_name = "ordinance_confirm_delete.html"

    def test_func(self):
        return Post.objects.get(id=self.kwargs["pk"])

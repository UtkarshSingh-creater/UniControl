from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Home
from .forms import HomeForm


@login_required
def home_list(request):

    homes = Home.objects.filter(owner=request.user)

    return render(
        request,
        "homes/home_list.html",
        {"homes": homes},
    )


@login_required
def home_create(request):

    if request.method == "POST":

        form = HomeForm(request.POST)

        if form.is_valid():

            home = form.save(commit=False)

            home.owner = request.user

            home.save()

            return redirect("home_list")

    else:

        form = HomeForm()

    return render(
        request,
        "homes/home_form.html",
        {"form": form},
    )


@login_required
def home_update(request, pk):

    home = get_object_or_404(
        Home,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":

        form = HomeForm(
            request.POST,
            instance=home,
        )

        if form.is_valid():

            form.save()

            return redirect("home_list")

    else:

        form = HomeForm(instance=home)

    return render(
        request,
        "homes/home_form.html",
        {
            "form": form
        },
    )


@login_required
def home_delete(request, pk):

    home = get_object_or_404(
        Home,
        pk=pk,
        owner=request.user,
    )

    if request.method == "POST":

        home.delete()

        return redirect("home_list")

    return render(
        request,
        "homes/home_delete.html",
        {
            "home": home
        },
    )
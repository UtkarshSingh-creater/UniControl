from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Room

from .forms import RoomForm


@login_required
def room_list(request):

    rooms = Room.objects.filter(
        home__owner=request.user
    )

    return render(
        request,
        "rooms/room_list.html",
        {
            "rooms": rooms
        },
    )


@login_required
def room_create(request):

    if request.method == "POST":

        form = RoomForm(request.POST)

        if form.is_valid():

            room = form.save(commit=False)

            if room.home.owner != request.user:

                return redirect("room_list")

            room.save()

            return redirect("room_list")

    else:

        form = RoomForm()

        form.fields["home"].queryset = request.user.homes.all()

    return render(
        request,
        "rooms/room_form.html",
        {
            "form": form
        },
    )


@login_required
def room_update(request, pk):

    room = get_object_or_404(
        Room,
        pk=pk,
        home__owner=request.user
    )

    if request.method == "POST":

        form = RoomForm(
            request.POST,
            instance=room
        )

        if form.is_valid():

            form.save()

            return redirect("room_list")

    else:

        form = RoomForm(instance=room)

        form.fields["home"].queryset = request.user.homes.all()

    return render(
        request,
        "rooms/room_form.html",
        {
            "form": form
        },
    )


@login_required
def room_delete(request, pk):

    room = get_object_or_404(
        Room,
        pk=pk,
        home__owner=request.user
    )

    if request.method == "POST":

        room.delete()

        return redirect("room_list")

    return render(
        request,
        "rooms/room_delete.html",
        {
            "room": room
        },
    )
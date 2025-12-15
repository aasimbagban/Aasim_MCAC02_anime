from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import *


def index(request):
    return render(request, "index.html")


def blog(request):
    return render(request, "blog.html")


def categories(request):
    return render(request, "categories.html")


def login(request):

    if request.method == "POST":
        un = request.POST["uname"]
        p1 = request.POST["pass1"]

        user = auth.authenticate(username=un, password=p1)
        if user is not None:
            auth.login(request, user)
            print("login sucessful!")
            return redirect("/")

        else:
            print("Invalid username or password!!")
            redirect("/login/")
    return render(request, "login.html")


def main(request):
    return render(request, "main.html")


def signup(request):
    if request.method == "POST":
        fn = request.POST["fname"]
        ln = request.POST["lname"]
        em = request.POST["email"]
        un = request.POST["uname"]
        p1 = request.POST["pass1"]
        p2 = request.POST["pass2"]
        if p1 != p2:
            print("password doesn't match !")
            return redirect("/signup/")

        if User.objects.filter(username=un).exists():
            print("USername already Exists! try another Username")
            return redirect("/signup/")

        if User.objects.filter(email=em).exists():
            print("Email already exists")
            return redirect("/signup/")

        User.objects.create_user(
            first_name=fn, last_name=ln, email=em, username=un, password=p1
        )

        print("UserID created Sucessfully")
        return redirect("/login/")

    return render(request, "signup.html")


def anime_details(request):
    return render(request, "anime-details.html")


def anime_watching(request):
    return render(request, "anime-watching.html")


def base(request):
    return render(request, "base.html")


def blog_details(request):
    return render(request, "blog-details.html")


def anime_dashboard(request):

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        genre_id = request.POST.get("genre")

        genre_obj = Genre.objects.get(gid=genre_id)

        Anime.objects.create(
            title=title, description=description, image=image, genre=genre_obj
        )

        return redirect("anime_dashboard")

    geners = Genre.objects.all()
    anime_list = Anime.objects.all()

    return render(
        request, "anime-dashboard.html", {"anime_list": anime_list, "geners": geners}
    )

    if request.method == "POST":

        title = request.POST.get("title")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        genre = request.POST.get("genre")

        Anime.objects.create(
            title=title, description=description, image=image, genre=genre
        )

        return redirect("anime-dashboard")

    geners = Genre.objects.all()
    anime_list = Anime.objects.all()
    return render(
        request, "anime-dashboard.html", {"anime_list": anime_list, "geners": geners}
    )


def contact(request):
    return render(request, "contact.html")


def logout(request):
    auth.logout(request)
    print("logged out suceesfuly")
    return redirect("/")


def add_anime(request):
    geners = Genre.objects.all()

    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        genre_id = request.POST.get("genre")
        image = request.FILES.get("image")

        genre_obj = Genre.objects.get(gid=genre_id)

        Anime.objects.create(
            title=title, description=description, image=image, genre=genre_obj
        )

        return redirect("anime_dashboard")

    return render(request, "add_anime.html", {"geners": geners})


def edit_anime(request, id):
    geners = Genre.objects.all()
    anime = get_object_or_404(Anime, aid=id)

    if request.method == "POST":
        anime.title = request.POST.get("title")
        anime.description = request.POST.get("description")

        genre_id = request.POST.get("genre1")
        anime.genre = Genre.objects.get(gid=genre_id)

        if request.FILES.get("image"):
            anime.image = request.FILES.get("image")

        anime.save()
        return redirect("anime_dashboard")

    return render(request, "edit_anime.html", {"anime": anime, "geners": geners})


def delete_anime(request, id):
    anime = get_object_or_404(Anime, aid=id)
    anime.delete()
    return redirect("anime_dashboard")

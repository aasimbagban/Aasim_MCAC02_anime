from django.urls import path
from .views import *

urlpatterns = [
    path("", index, name="index"),
    path("blog/", blog, name="blog"),
    path("categories/", categories, name="categories"),
    path("login/", login, name="login"),
    path("main/", main, name="main"),
    path("anime-details/", anime_details, name="anime_details"),
    path("anime-watching/", anime_watching, name="anime_watching"),
    path("base/", base, name="base"),
    path("blog-details/", blog_details, name="blog_details"),
    path("signup/", signup, name="signup"),
    path("contact/", contact, name="contact"),
    path("logout/", logout, name="logout"),
    path("anime-dashboard/", anime_dashboard, name="anime_dashboard"),
    path("add/", add_anime, name="add_anime"),
    path("edit/<int:id>/", edit_anime, name="edit_anime"),
    path("delete/<int:id>/", delete_anime, name="delete_anime"),
]

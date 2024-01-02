from django.urls import path

from portfolio import views

urlpatterns = [
    path("", views.index, name="index"),
    path("resumee/", views.ResumeeList.as_view(), name="resumee-list"),
    # path("resumee/<int:pk>/", views.MatchDetail.as_view(), name="match-detail"),
]

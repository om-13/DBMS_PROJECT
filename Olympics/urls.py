"""LeaderboardZoneApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sortLeaderboard',views.sortLeaderboard,name="sortLeaderboard"),
    path('showLeaderboard',views.showLeaderboard,name="showLeaderboard"),
    path('insertLeaderboard',views.insertLeaderboard,name="insertLeaderboard"),
    path('editLeaderboard/<int:id>',views.editLeaderboard,name="editLeaderboard"),
    path('',views.HomePage,name="HomePage"),
    path('updateLeaderboard/<int:id>',views.updateLeaderboard,name="updateLeaderboard"),
    path('delLeaderboard/<int:id>',views.delLeaderboard,name="delLeaderboard"),
    path('deletedLeaderboard/<int:id>',views.deletedLeaderboard,name="deletedLeaderboard"),
    path('runQueryLeaderboard',views.runQueryLeaderboard,name="runQueryLeaderboard"),

    path('showAthlete',views.showAthlete,name="showAthlete"),
    path('insertAthlete',views.insertAthlete,name="insertAthlete"),
    path('sortAthlete',views.sortAthlete,name="sortAthlete"),
    path('editAthlete/<int:id>',views.editAthlete,name="editAthlete"),
    path('updateAthlete/<int:id>',views.updateAthlete,name="updateAthlete"),
    path('delAthlete/<int:id>',views.delAthlete,name="delAthlete"),
    path('deletedAthlete/<int:id>',views.deletedAthlete,name="deletedAthlete"),
    path('runQueryAthlete',views.runQueryAthlete,name="runQueryAthlete"),
]

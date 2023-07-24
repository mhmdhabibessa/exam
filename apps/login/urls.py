from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.wall),
    path('craete-pie', views.craetePie),
    path('edit/<int:uid>', views.edit),
    path('update/<int:uid>', views.update),
    path('delete/<int:uid>', views.delete),
    path('pie-derby', views.pieDerby),
    path('vote-pie/<int:uid>', views.votePie),
    path('user/vote/<int:uid>', views.addVote),
    path('user/un-vote/<int:uid>', views.unvote),
    path('logout', views.logout),
    
    
    # _______________________
    path('travels', views.traavels),
    path('index-travel', views.IndexTravel),
    path('add_travel', views.add_travel),
    path('travels/destination/<int:id>', views.travelsDetails),
    path('craete-travel', views.craeteTravel),
    path('join/<int:TripId>', views.addTrip),
    path('unjoin/<int:TripId>', views.removeTrip),
    path('travels/destination/<int:id>', views.detailsTravel),
    
    #___________________________________________________
    
    
]
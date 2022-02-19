from django.urls import path
from . import views
urlpatterns = [
   path("",views.ReviewView.as_view()) ,
   path("thank-you/<str:username>",views.ThankyouView.as_view(),name="thankyou"),
   path("reviews", views.ReviewsListView.as_view()),
   path("review/<int:id>", views.ReviewView.as_view(),name='reviewdetail'),

   ]
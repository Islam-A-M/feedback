from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .forms import ReviewForm
from .models import Review
from django.views import View
# Create your views here.
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
    
        return render(request, "reviews/review.html",{
        "form":form
        })
        
    def post(self, request):
        # existing_model = Review.objects.get(pk=1)
        # form = ReviewForm(request.POST,instance=existing_model) if update
        form = ReviewForm(request.POST,)
          
        if form.is_valid():
            # review = Review(user_name=form.cleaned_data['user_name'], 
            #                 review_text = form.cleaned_data['review_text'], 
            #                 rating = form.cleaned_data['rating'])
            # review.save()
            
            form.save()
            return HttpResponseRedirect(reverse("thankyou", args=[form.cleaned_data['user_name']]))
        return render(request, "reviews/review.html",{
        "form":form
        })
        
        
        
# def  review(request):
#     if request.method =="POST":
#         # existing_model = Review.objects.get(pk=1)
#         # form = ReviewForm(request.POST,instance=existing_model) if update
#         form = ReviewForm(request.POST,)
          
#         if form.is_valid():
#             # review = Review(user_name=form.cleaned_data['user_name'], 
#             #                 review_text = form.cleaned_data['review_text'], 
#             #                 rating = form.cleaned_data['rating'])
#             # review.save()
            
#             form.save()
#             return HttpResponseRedirect(reverse("thankyou", args=[form.cleaned_data['user_name']]))
#     else:   
#        form = ReviewForm()
    
#     return render(request, "reviews/review.html",{
#         "form":form
#     })

class ThankyouView(View):
   def get(self, request, username):
     return render(request, "reviews/thank_you.html", 
                  {"username":username})

# def thank_you(request,username):
#     return render(request, "reviews/thank_you.html", 
#                   {"username":username})
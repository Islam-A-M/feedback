import imp
import django
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .forms import ReviewForm,ReviewFormViewOnly
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView,DetailView
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm # if we want to customize the fields the create view cant do that like there
    template_name ="reviews/review.html"
    success_url =''
    
    def form_valid(self, form) :
        #this is optional in this case i want to pass username from form
        self.success_url=  reverse('thankyou', kwargs={'username': form.cleaned_data['user_name']})
        # self.success_url=self.success_url+form.cleaned_data['user_name']
        return super().form_valid(form)
    
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name ="reviews/review.html"
#     success_url =''
    
#     def form_valid(self, form) :
#         form.save()
#         self.success_url=  reverse('thankyou', kwargs={'username': form.cleaned_data['user_name']})
#         # self.success_url=self.success_url+form.cleaned_data['user_name']
#         return super().form_valid(form)
        
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
    
#         return render(request, "reviews/review.html",{
#         "form":form
#         })
        
#     def post(self, request):
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
#         return render(request, "reviews/review.html",{
#         "form":form
#         })
        
        
        
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

class ThankyouView(TemplateView):
    template_name = "reviews/thank_you.html"
    def get_context_data(self, **kwargs) :
        return super().get_context_data(**kwargs)

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review
    context_object_name = "reviews"
    
    def get_queryset(self):
        
        base_query= super().get_queryset()
       # base_query= base_query.filter(rating__gt = 3)
        return base_query
# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context['reviews']= reviews
        
#         return context
    
class ReviewViewDetail(DetailView):
     template_name = "reviews/review_detail.html"
     model = Review   
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        
        return context
# class ReviewViewDetail(TemplateView):
#      template_name = "reviews/review_detail.html"

#      def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review = Review.objects.get(pk=context['id'])

#         form = ReviewFormViewOnly(initial={'user_name':review.user_name ,
#                                            'review_text':review.review_text,
#                                            'rating':review.rating })

#         context['form']= form
        
#         return context
# class ThankyouView(View):
#    def get(self, request, username):
#      return render(request, "reviews/thank_you.html", 
#                   {"username":username})

# def thank_you(request,username):
#     return render(request, "reviews/thank_you.html", 
#                   {"username":username})

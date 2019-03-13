from django.shortcuts import render, get_object_or_404
from .models import Company, Review

# Create your views here.

def review_list(request):
    latest_review_list = Review.objects.order_by('-date_published')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'reviews/review_list.html', context)

def review_detail(request):
    review = get_object_or_404(Review, pk=review_id)
    return render(request, 'reviews/review_detail.html', {'review': review})

def company_list(request):
    company_list = Company.objects.order_by('-name')
    context = {'company_list':company_list}
    return render(request, 'reviews/company_list.html', context)

def company_detail(request):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'reviews/company_detail.html', {'company': company})

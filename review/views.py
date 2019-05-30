from django.shortcuts import render, get_object_or_404, redirect
from .forms import ReviewForm
from .models import Review
from django.utils import timezone

# Create your views here.
# 글쓰기
def rpost(request):
    if request.method == "POST":
        form = ReviewForm(request.POST) 

        if form.is_valid(): 
            review = form.save(commit=False) 
            review.update_date=timezone.now() 
            review.save()
            return redirect('rshow') 
    else:
        form = ReviewForm() 
        return render(request, 'rpost.html',{'form' : form})

def rshow(request):
        reviews = Review.objects.order_by('-id')
        return render(request, 'rshow.html', {'reviews':reviews})

def redit(request, pk):
        review = get_object_or_404(Review, pk=pk)

        if request.method == "POST":
                form = ReviewForm(request.POST, instance=review) 

                if form.is_valid(): 
                        review = form.save(commit=False) 
                        review.update_date=timezone.now() 
                        review.save()
                        return redirect('rshow') 

        else:
                form = ReviewForm(instance=review) 
                return render(request, 'rpost.html',{'form' : form})

def delete(request, pk):
        review = Review.objects.get(id=pk)
        review.delete()
        return redirect('rshow')
from django.shortcuts import render, get_object_or_404
from .models import Portfolio

# Create your views here.


def home(request):
    portfolios = Portfolio.objects
    return render(request, 'portfolio.html', {'portfolios': portfolios})


def detail(request, portfolio_id):
    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    return render(request, 'pfdetail.html', {'portfolio': portfolio})

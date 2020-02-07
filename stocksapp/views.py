from django.shortcuts import render, redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm
import time
import requests
import json


def index(request):
    

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_token = "pk_4207608c73a8464fbd181abcd5259a73"
        api_request = requests.get(
            f"https://cloud.iexapis.com/stable/stock/{ticker}/quote?token={api_token}&format=json")

        # get info about company /stock/{ticker}/company --> {symbol}

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        return render(request, 'index.html', {"api": api})

    else:
        return render(request, 'index.html', {"ticker": "Fill out the ticker in the form above."})

    


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added successfully.")
            return redirect('add_stock')

    else:
        ticker = Stock.objects.all()
        output = []
        api_token = "pk_4207608c73a8464fbd181abcd5259a73"


        for ticker_item in ticker:
            # time.sleep(0.001)
            api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{str(ticker_item)}/quote?token={api_token}&format=json")

            try:
                api = json.loads(api_request.content)
                output.append(api)
            except Exception as e:
                api = "Error"

        return render(request, 'add_stock.html', {"ticker": ticker, "output": output})


def delete(request, stock_id):
    try:
        item = Stock.objects.get(pk=stock_id)
        item.delete()
        messages.success(request, "Item has been deleted.")
        return redirect('delete_stock')
    except Exception:
        messages.error(request, "There is no such stock to delete.")
        return redirect('delete_stock')


def delete_stock(request):
    ticker = Stock.objects.all()
    return render(request, "delete_stock.html", {"ticker": ticker})

# using messages in django: https://docs.djangoproject.com/en/3.0/ref/contrib/messages/

from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
          "my_list": [

              {"restaurant_name" : "nino",
              "food_type" : "italian" },

              {"restaurant_name" : "macd",
              "food_type" : "fast_food"},

              {"restaurant_name" : "kfc",
              "food_type" : "chicken"}

          ]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = { "my_object":{"restaurant_name" : "nino",
              "food_type" : "italian" }

    }
    return render(request, 'detail.html', context)

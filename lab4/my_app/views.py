from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class OrdersView(View):
    def get(self,request):
        data={
            'orders': [
                {'title': 'Первый заказ', 'id': 1},
                {'title': 'Второй заказ', 'id': 2},
                {'title': 'Третий заказ', 'id': 3},
            ]
        }
        return render(request,'orders.html',data)

def func(request):
    return render(request, 'variable.html', {'my_variable': 'HIIIIIII!'})
class OrderView(View):
    def get(self,request,id):
        data={
            'order': {
                'id': id
            }
        }
        return render(request,'order.html',data)

def function_view(request):
    return render(request, 'variable.html',{'my_variable': 'HIIIIIII!'})



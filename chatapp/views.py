from django.shortcuts import render

# Create your views here.


def index_view(request):
    return render(request,'chat/index.html')



def room_view(request,room_name):
    context={"room_name":room_name}
    return render(request,'chat/room.html',context)
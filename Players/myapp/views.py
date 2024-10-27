from django.shortcuts import render,redirect
from .models import Player
from django.contrib.auth.models import User
# def playersea(request):
#     player=None
#     notplayer=None
#     if(request.method=="POST"):
#         sear=request.POST.get('name')
#         if sear:
#             players=Player.objects.filter(name=sear)
#             if players:
#                 player=players[0]
#             else:
#                 notplayer="Not in Records!"
#         return render(request, 'player.html',{'player':player,'notplayer': notplayer})
#     else:
#         sear=request.GET.get('name')
#         if sear:
#             players=Player.objects.filter(name=sear)
#             if players:
#                 player=players[0]
#             else:
#                 notplayer="Not in Records!"
#         return render(request, 'player.html',{'player':player,'notplayer': notplayer})
    
# def func(request,no,name):
#     obj=Player.objects.get(id=no)
#     obj.name=name
#     obj.save()
#     return render(request,'player.html',{'player':obj})

# def playersear(request):
#     if request.method == "POST":
#         pid=request.POST.get('pid')
#         name = request.POST.get('name')
#         team = request.POST.get('team')
#         position = request.POST.get('position')
#         age = request.POST.get('age')
#         nationality = request.POST.get('nationality')
#         if Player.objects.filter(id=pid):
#             obj=Player.objects.get(id=pid)
#             obj.name=name
#             obj.team=team
#             obj.position=position
#             obj.age=age
#             obj.nationality=nationality
#             obj.save()
            
#             players = Player.objects.all()
#             return render(request, 'player.html', {'players': players})

        # """if pid:
        #    Player.objects.filter(id=pid).update(
        #         name=name,
        #         team=team,
        #         position=position,
        #         age=age,
        #         nationality=nationality
        #     ) 
        # else:
        #     player = Player(name=name, team=team, position=position, age=age, nationality=nationality)
        #     player.save()"""
        
    # players = Player.objects.all()
    # return render(request, 'player.html', {'players': players})
# def Usersview(request):
#     result=User.objects.all()
#     return render(request,'users.html',{'res':result})

def loginview(request):
    c=False
    res=True
    if request.method=="POST":
        usern=request.POST.get('powerstar')
        passw=request.POST.get('superstar')
        c=User.objects.filter(username=usern).exists()
        print(c)
    return render(request,'exist.html',{'res':c})
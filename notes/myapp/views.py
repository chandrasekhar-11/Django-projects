from django.shortcuts import render
from django.shortcuts import redirect
from .models import Note



def note(request):
    notes = Note.objects.all()
    return render(request, 'index.html', {'notes': notes})


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(title=title, content=content)
        return redirect('note_list')
    return render(request, 'noteform.html')

def update(request, id):
    note = Note.objects.filter(id=id).first()
    if not note:
        return HttpResponseNotFound("id ille")
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.save()
        return redirect('note_list')
    return render(request, 'noteform.html', {'note': note})
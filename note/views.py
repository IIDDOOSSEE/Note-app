from django.shortcuts import render
from django.http import HttpResponse
from .models import note
from django.shortcuts import render, get_object_or_404 ,redirect
from datetime import datetime
def index(request):
    latest_note_list = note.objects.order_by("-pub_date")[:5]
    context = {"latest_note_list": latest_note_list}
    return render(request, "note/index.html", context)

def detail(request, note_id):
    latest_note_data = get_object_or_404(note, id=note_id)
    context = {"latest_note_data": latest_note_data}
    return render(request, "note/detail.html", context)

def add_note(request):
    if request.method == 'POST':
        
        title = request.POST.get('title_text')
        content = request.POST.get('content_text')
        pub_date = request.POST.get('pub_date')

        if title and content and pub_date:
            note.objects.create(
                title_text=title,
                content_text=content,
                pub_date=datetime.strptime(pub_date, '%Y-%m-%dT%H:%M')
            )
            return redirect('index')  

    return render(request, 'note/add_note.html')
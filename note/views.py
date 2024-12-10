from django.shortcuts import render
from django.http import HttpResponse
from .models import note
from django.shortcuts import render, get_object_or_404

def index(request):
    latest_note_list = note.objects.order_by("-pub_date")[:5]
    context = {"latest_note_list": latest_note_list}
    return render(request, "note/index.html", context)

def detail(request, note_id):
    latest_note_data = get_object_or_404(note, id=note_id)
    context = {"latest_note_data": latest_note_data}
    return render(request, "note/detail.html", context)
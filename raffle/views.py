from django.views import generic
from django.shortcuts import render
from raffle.models import Entry
from raffle.forms import TextFileForm


class IndexView(generic.CreateView):
    model = Entry
    fields = ["name", "image"]
    template_name = "raffle.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entries"] = Entry.objects.all()
        return context


def upload_file(request):
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            with open(request.FILES['text_file'], "r", encoding="utf-8") as lines:
                for line in lines:
                    new = Entry(name=line)
                    new.save()
            return HttpResponseRedirect('/')
    else:
        form = TextFileForm()
    return render(request, 'upload.html', {'form': form})


def participants(request):
    return render(request, "participants.html")


def privacy(request):
    return render(request, "privacypolicy.htm")

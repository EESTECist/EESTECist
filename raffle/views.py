from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from raffle.models import Entry
from raffle.forms import TextFileForm
from django.contrib.auth.decorators import user_passes_test


class IndexView(generic.CreateView):
    model = Entry
    fields = ["name", "image"]
    template_name = "raffle.html"
    success_url = "/"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["entries"] = Entry.objects.all()
        return context


@user_passes_test(lambda u: u.is_superuser)
def upload_file(request):
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)
        if form.is_valid():
            for line in request.FILES["text_file"]:
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

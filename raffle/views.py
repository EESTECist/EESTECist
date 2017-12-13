from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from raffle.models import Entry
from raffle.forms import TextFileForm, EntryForm
from django.contrib.auth.decorators import user_passes_test
from instagram_scraper import InstagramScraper
from EESTECist.settings import MEDIA_ROOT
import json


class IndexView(generic.CreateView):
    model = Entry
    fields = ["name", "img_url"]
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
            scraper = InstagramScraper(usernames=[line.rstrip().decode("utf-8") for line in request.FILES["text_file"]], media_metadata=True, media_types=[], maximum=5, destination=MEDIA_ROOT, retain_username=False)
            scraper.scrape()
            for line in request.FILES["text_file"]:
                username = line.rstrip().decode("utf-8")
                try:
                    f = open(MEDIA_ROOT + username + ".json")
                    data = json.load(f)
                    new = Entry(name=username, img_url=get_hashtag_img_url(data, request.POST["hashtag"]))
                    new.save()
                except:
                    new = Entry(name=username)
                    new.save()
                finally:
                    f.close()
            return HttpResponseRedirect('/')
    else:
        form = TextFileForm()
        entry_form = EntryForm()
    return render(request, 'upload.html', {'form': form, 'entry_form': entry_form})


def get_hashtag_img_url(data, hashtag):
    for img in data:
        try:
            tags = img["tags"]
            if hashtag in tags:
                return img["display_url"]
        except:
            continue


@user_passes_test(lambda u: u.is_superuser)
def flush(request):
    Entry.objects.all().delete()
    return HttpResponseRedirect('/')


def participants(request):
    return render(request, "participants.html")


def privacy(request):
    return render(request, "privacypolicy.htm")

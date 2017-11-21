from raffle.models import Entry


def global_context_processor(request):
    usernames = [entry.name for entry in Entry.objects.all()]
    return {"usernames": usernames}

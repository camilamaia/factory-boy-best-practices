from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from polls.models import Choice, Poll, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_poll_list"

    def get_queryset(self):
        """
        Return the published polls (not including those set to be
        published in the future) order by DESC pub_date
        """
        return Poll.objects.filter(pub_date__lte=timezone.now()).order_by(
            "-pub_date"
        )


class DetailView(generic.DetailView):
    model = Poll
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Poll
    template_name = "polls/results.html"


def vote(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)

    try:
        selected_choice = poll.question.choices.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "poll": poll,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(poll.id,)))

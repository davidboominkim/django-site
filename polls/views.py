
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question, Choice, Thought
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from .forms import ThoughtForm

class IndexView(generic.ListView):
    template_name = 'polls/question_index.html'
    context_object_name = 'latest_question_list'
    # latest_question_list = Question.objects.filter()
    # context_object_name2 = 'latest_thought_list'
    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

    # def get_queryset2(self):
    #     return Thought.objects


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# Create your views here.

def detail(request, thought_id):
    thought = get_object_or_404(Thought, pk=thought_id)
    return render(request, 'polls/thought_detail.html', {'thought': thought})


def think(request):
    return HttpResponse("You're thinking a thought.")

def post_thought(request):
    template_name = 'polls/thought_creation.html'
    thoughts = Thought.objects.filter()
    new_thought = None
    if request.method == 'POST':
        thought_form = ThoughtForm(data=request.POST)
        if thought_form.is_valid():
            new_thought = thought_form.save(commit=False)
            new_thought.save()
    else:
        thought_form = ThoughtForm()

    return render(request, template_name, {'thoughts':thoughts,'new_thought':new_thought,'thought_form':thought_form})

def index(request):
    latest_thought_list = Thought.objects.filter()
    context = {
        'latest_thought_list': latest_thought_list,
    }
    return render(request, 'polls/thought_index.html', context)

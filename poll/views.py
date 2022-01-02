from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Poll
from .forms import PollForm


def home(request):
    polls =Poll.objects.all()

    context = {'polls':polls}
    return render(request, 'poll/home.html', context)


def create(request):
    if request.method=='POST':
        form= PollForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect('home')
    else:
        form= PollForm()
    form= PollForm()
    context= {
        'form': form
    }
    return render(request, 'poll/create.html', context)


def vote(request, poll_id):
    poll = Poll.objects.get(pk= poll_id)
    if request.method == 'POST':
        poll_ans= request.POST['poll']
        if poll_ans == 'option1':
            poll.option_one_count +=1
        elif poll_ans == 'option2':
            poll.option_two_count +=1
        elif poll_ans == 'option3':
            poll.option_three_count +=1
        else: return HttpResponse(400,'invalid form')
        poll.save()
        return redirect('results', poll.id)
    context = {
        'poll':poll
    }
    return render(request, 'poll/vote.html', context)


def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'poll/results.html', context)


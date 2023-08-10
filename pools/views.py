from django.http import HttpResponse
from pools.models import Question, Choice
from datetime import datetime
from django.shortcuts import get_object_or_404, render, redirect


def index(request):
    context = {}
    vote_counts = {}  # question_id: number of votes
    context["title"] = "List of all questions"
    questions = Question.objects.all()
    context["questions"] = questions
    for q in questions:
        vote_counts[q.id] = sum([c.votes for c in q.choices.all()])
    context["vote_counts"] = vote_counts
    return render(request, "pools/index.html", context)


def delete(request):
    count = Question.objects.count()
    Question.objects.all().delete()
    return HttpResponse(f"We deleted {count} questions")


def create_question(request):
    q = Question()
    q.question_text = "A question created at " + str(datetime.now())
    q.pub_date = datetime.now()
    q.save()
    return HttpResponse("Create a dummy question")


def update(request):
    questions = Question.objects.filter(id__gte=10).filter(id__lte=12)
    questions.update(question_text="This questions got updated")
    return HttpResponse("updated the questions")


def update_one(request, qid):
    context = {}
    context["qid"] = qid
    question = get_object_or_404(Question, pk=qid)
    if request.method == 'POST':
        text  = request.POST.get("question_text")
        question.question_text = text
        question.save()
    return render(request, "pools/question_update_one.html", context)
    # questions = Question.objects.get(id = qid)
    # questions.question_text = "Question " + qid + " has been updated"
    # questions.save()
    # return HttpResponse("Updated question " + qid)


def question_detail(request, qid):
    question = get_object_or_404(Question, pk=qid)
    choices = question.choices.all()
    context = {
        "question": question,
        "choices": choices,
    }
    if request.method == "POST":
        selected_choice_id = request.POST.get("selected_choice")
        selected_choice = Choice.objects.get(pk=selected_choice_id)
        selected_choice.votes += 1
        selected_choice.save()
        context["message"] = "You voted successfully..."
    return render(request, "pools/question_detail.html", context)

# def hello(request, first_name):
#     return HttpResponse("Hello " + first_name + ". You are on the Hello page.")


# def hello_shivam(request):
#     return HttpResponse("Hello Shivam. You are on your page.")


def create_choice(request, q_id):
    c = Choice()
    question = get_object_or_404(Question, pk=q_id)
    # The first approach to pass a value to foreignkey
    # c.question_id = q_id

    # the second appoach to pass a value to foreignkey using an object
    c.question = question
    c.choice_text = "A question created at " + str(datetime.now())
    c.save()
    return HttpResponse("Create a dummy question")


def choice_detail_view(request, id):
    choice = get_object_or_404(Choice, pk=id)
    context = {"choice": choice}
    return render(request, "pools/choice_detail.html", context)


def choice_update_view(request, id):
    # TODO: Fix this after learning forms
    choice = get_object_or_404(Choice, pk=id)
    if request.method == "POST":
        # Process form data
        pass
    else:
        # Initial request, send form
        form = ChoiceForm(instance=choice)
        context = {"form": form}
        return render(request, "pools/choice_update.html", context)


def choice_delete_view(request, id):
    choice = get_object_or_404(Choice, pk=id)
    if request.method == "POST":
        # Delete choice
        choice.delete()
        return render(request, "pools/choice_delete_success.html", {})
    context = {"choice": choice}
    return render(request, "pools/choice_delete.html", context)


def choice_list_view(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question)
    context = {"choices": choices}
    print(choices)
    return render(request, "pools/choice_list.html", context)

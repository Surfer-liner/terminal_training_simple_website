from django.shortcuts import render, redirect
from .models import Topic, Comments
from .forms import TopicForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


def home_page(request):
    return render(request, 'simple_site/home_page.html')


def topics(request):
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'simple_site/topics.html', context)


@login_required
def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    comments = topic.comments_set.order_by('-date')
    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.topic = topic
            new_comment.owner = request.user
            new_comment.save()
            return redirect('simple_site:topic', topic_id=topic.id)
    context = {'form': form, 'topic': topic, 'comments': comments}
    return render(request, 'simple_site/topic.html', context)


@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic_new = form.save(commit=False)
            topic_new.owner = request.user
            topic_new.save()
            return redirect('simple_site:topics')
    context = {'form': form}
    return render(request, 'simple_site/new_topic.html', context)


@login_required
def delete_comment(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    topic_id = comment.topic.id
    comment.delete()
    return redirect('simple_site:topic', topic_id)


@login_required
def comment_owner_checker(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    if comment.owner != request.user:
        raise Http404
    else:
        return (request, comment_id)


@login_required
def topic_owner_checker(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    else:
        return (request, topic_id)


@login_required
def edit_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    topic_owner_checker(request, topic_id)
    if request.method != 'POST':
        form = TopicForm(instance=topic)
    else:
        form = TopicForm(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('simple_site:topics')
    context = {'form': form, 'topic': topic}
    return render(request, 'simple_site/edit_topic.html', context)


@login_required
def edit_comment(request, comment_id):
    comment = Comments.objects.get(id=comment_id)
    topic = comment.topic
    comment_owner_checker(request, comment_id)
    if request.method == "POST":
        form = CommentForm(instance=comment, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('simple_site:topic', topic_id=topic.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form, 'comment': comment}
    return render(request, 'simple_site/edit_comment.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404, HttpResponse

from .models import Topic, Comments, UploadFile
from .forms import TopicForm, CommentForm, UploaFileForm

from reportlab.pdfgen import canvas
from io import BytesIO


def home_page(request):
    '''Directs to the home page'''
    return render(request, 'simple_site/home_page.html')


def topics(request):
    '''Directs to the topics page'''
    topics = Topic.objects.all()
    context = {'topics': topics}
    return render(request, 'simple_site/topics.html', context)


@login_required
def topic(request, topic_id):
    '''Directs to the topic page and shows a list of comments on the topic'''
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
    '''Page for creating a new theme'''
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
    '''Comment deletion function'''
    comment = Comments.objects.get(id=comment_id)
    topic_id = comment.topic.id
    comment.delete()
    return redirect('simple_site:topic', topic_id)


@login_required
def comment_owner_checker(request, comment_id):
    '''Checks whether the user from the request matches the comment creator'''
    comment = Comments.objects.get(id=comment_id)
    if comment.owner != request.user:
        raise Http404
    else:
        return (request, comment_id)


@login_required
def topic_owner_checker(request, topic_id):
    '''Checks whether the user from the request matches the topic creator'''
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    else:
        return (request, topic_id)


@login_required
def edit_topic(request, topic_id):
    '''Directs to the topic changes page'''
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
    '''Directs to the comment changes page'''
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


def converter(request):
    '''Converting .txt to .pdf'''
    if request.method == 'POST':
        form = UploaFileForm(request.POST, request.FILES)
        if form.is_valid():
            txt_file = request.FILES['upload_file']
            txt_file_content = txt_file.read().decode('utf-8').split('\n')

            buffer = BytesIO()
            pdf = canvas.Canvas(buffer)
            x = 60
            y = 780
            length = 90
            pdf.setFont("Helvetica", 10)

            # with open(txt_file.name, 'r') as f:
            #     txt_file_content = f.readlines()

            for string_inside in txt_file_content:
                index = 0
                if len(string_inside) >= length:
                    strings_in_string_inside = round(len(string_inside) /
                                                         length)
                    for string in range(int(strings_in_string_inside)):
                        string_to_print = string_inside[index:index + length]
                        pdf.drawString(x, y, string_to_print.rstrip('\n'))
                        index += length
                        y -= 13
                elif len(string_inside) < length:
                    pdf.drawString(x, y, string_inside[:-1])
                    y -= 13
            pdf.save()

            buffer.seek(0)

            response = HttpResponse(buffer, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; ' \
                                              'filename="output.pdf"'
            return response
    else:
        form = UploaFileForm()
    context = {'form': form}
    return render(request, 'simple_site/home_page.html', context)
from .forms import StoryForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Edition, Story, Author
from .forms import EditionForm, AuthorForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .context_processors import is_author


# USER VERIFICATION
def is_author(user):
    return user.is_authenticated and user.groups.filter(name="Authors").exists()

# HOMEPAGE VIEW


def home_page(request):
    return render(request, 'my_app/home.html')


# EDITONS: CRUD, LISTING

def edition_list(request):
    editions = Edition.objects.all().order_by('-date')
    return render(request, 'my_app/edition_list.html', {'editions': editions})


def edition_detail(request, pk):
    edition = get_object_or_404(Edition, pk=pk)
    stories = edition.stories.all()
    return render(request, 'my_app/edition_detail.html', {'edition': edition, 'stories': stories, 'is_author': request.user.is_authenticated})


@user_passes_test(is_author)
def edition_create(request):
    if request.method == "POST":
        form = EditionForm(request.POST)
        if form.is_valid():
            edition = form.save()
            messages.success(request, "Edition created successfully!")
            return redirect('edition_detail', pk=edition.pk)
    else:
        form = EditionForm()
    return render(request, 'my_app/edition_form.html', {'form': form})


@user_passes_test(is_author)
def edition_edit(request, pk):
    edition = get_object_or_404(Edition, pk=pk)
    if request.method == "POST":
        form = EditionForm(request.POST, request.FILES, instance=edition)
        if form.is_valid():
            form.save()
            return redirect('edition_detail', pk=edition.pk)
    else:
        form = EditionForm(instance=edition)
    return render(request, 'my_app/edition_form.html', {'form': form})


@user_passes_test(is_author)
def edition_delete(request, pk):
    edition = get_object_or_404(Edition, pk=pk)
    edition.delete()
    messages.warning(request, "Edition deleted.")
    return redirect('edition_list')


# STORY: CRUD


@user_passes_test(is_author)
def story_create(request, edition_pk):
    edition = get_object_or_404(Edition, pk=edition_pk)
    if request.method == "POST":
        form = StoryForm(request.POST)
        if form.is_valid():
            story = form.save(commit=False)
            story.edition = edition
            story.save()
            messages.success(request, "Story created successfully!")
            return redirect('edition_detail', pk=edition.pk)
    else:
        form = StoryForm()
    return render(request, 'my_app/story_form.html', {'form': form, 'edition': edition})


@user_passes_test(is_author)
def story_edit(request, pk):
    story = get_object_or_404(Story, pk=pk)
    if request.method == "POST":
        form = StoryForm(request.POST, request.FILES, instance=story)
        if form.is_valid():
            form.save()
            return redirect('edition_detail', pk=story.edition.pk)
    else:
        form = StoryForm(instance=story)
    return render(request, 'my_app/story_form.html', {'form': form, 'edition': story.edition})


@user_passes_test(is_author)
def story_delete(request, pk):
    story = get_object_or_404(Story, pk=pk)
    edition_pk = story.edition.pk
    story.delete()
    return redirect('edition_detail', pk=edition_pk)

# AUTHORS VIEWS


def author_list(request):
    authors = Author.objects.exclude(name__isnull=True).exclude(name__exact="")
    return render(request, 'my_app/author_list.html', {'authors': authors})


@user_passes_test(is_author)
def author_create(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Author added with success!")
            return redirect('author_list')
    else:
        form = AuthorForm()
    return render(request, 'my_app/author_form.html', {'form': form})

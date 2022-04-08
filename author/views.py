from django.shortcuts import render
from .models import Author
from .forms import AuthorForm

# Create your views here.


def show_authors(request):
    all_auth = Author.objects.all()
    title = "all authors"
    context = {"all_auth": all_auth,
               "title": title,
               }
    return render(request, 'author/authors.html', context)


def edit_author(request, pk):
    author = Author.get_by_id(pk)
    context = {"author": author,
               "title": f"id:{pk}"
               }
    if request.method == "POST":
        if "delete" in request.POST:
            author.delete()
            context["delete"] = "Author was deleted"
        if "save" in request.POST:
            form_author = AuthorForm(request.POST, instance=author)
            if form_author.is_valid():
                if form_author.has_changed():
                    form_author.save()
                    context["saved"] = "changes was saved"
                else:
                    context["form_not_changed"] = "form not changed"
    else:
        context["form"] = AuthorForm(instance=author)
    return render(request, 'author/author.html', context)


def add_author(request):
    context = {"title": "create author"
               }
    if request.method == "POST":
        form_author = AuthorForm(request.POST)
        if form_author.is_valid():
            if form_author.has_changed():
                form_author.save()
                context["create"] = "author was created"
            else:
                context["form_not_changed"] = "author wasn't created"
    else:
        context["form"] = AuthorForm()
    return render(request, 'author/add_author.html', context)

from django.shortcuts import render
from .models import CustomUser
from .forms import UserForm

# Create your views here.


def show_all_users(request):
    all_users = CustomUser.objects.all()
    title = "all users"
    context = {"all_users": all_users,
               "title": title,
               }
    return render(request, 'authentication/all_users.html', context)


def edit_user(request, pk):
    user = CustomUser.get_by_id(pk)
    context = {"user": user,
               "title": f"id:{pk}"
               }
    if request.method == "POST":
        if "delete" in request.POST:
            user.delete()
            context["delete"] = "User was deleted"
        if "save" in request.POST:
            form_user = UserForm(request.POST, instance=user)
            if form_user.is_valid():
                if form_user.has_changed():
                    form_user.save()
                    context["saved"] = "changes was saved"
                else:
                    context["form_not_changed"] = "form not changed"
    else:
        context["form"] = UserForm(instance=user)
    return render(request, 'authentication/edit_user.html', context)


def add_user(request):
    context = {"title": "create user"
               }
    if request.method == "POST":
        form_user = UserForm(request.POST)
        if form_user.is_valid():
            if form_user.has_changed():
                form_user.save()
                context["create"] = "user was created"
            else:
                context["form_not_changed"] = "user wasn't created"
    else:
        context["form"] = UserForm()
    return render(request, 'authentication/add_user.html', context)

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import LoginForm, RegisterForm


def auth_view(request):
    login_form = LoginForm(request, data=request.POST or None)
    register_form = RegisterForm(request.POST or None)

    if request.method == "POST":
        form_type = request.POST.get("form_type")

        if form_type == "login":
            login_form = LoginForm(request, data=request.POST)
            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect("home")

        elif form_type == "register":
            register_form = RegisterForm(request.POST)
            if register_form.is_valid():
                user = register_form.save(commit=False)
                user.set_password(register_form.cleaned_data["password"])
                user.save()

                login(request, user)
                return redirect("home")

    return render(request, "accounts/auth.html", {
        "login_form": login_form,
        "register_form": register_form,
    })


def logout_view(request):
    logout(request)
    return redirect("auth")
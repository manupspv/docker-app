from django.shortcuts import render, redirect
from .forms import UserSignUpForm
from django.contrib import messages
from django.contrib.auth import views as auth_views


def signup(request):

    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account created for {username}! Log In here.")
            form.save()
            return redirect('account-login')
    else:
        form = UserSignUpForm()

    context = {
    "title":"Sign Up",
    'form':form
    }
    return render(request, "account/signup.html", context)

class MyLoginView(auth_views.LoginView):
    template_name = 'account/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title":"Login"
        })
        return context

class MyLogoutView(auth_views.LogoutView):
    template_name = 'account/logout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title":"Logout"
        })
        return context
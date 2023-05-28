from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Registry a new user"""
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('guideline_list')

    context = {'form': form}
    return render(request, 'registration/register.html', context)


# def custom_logout(request):
#     logout(request)
#     # messages.info(request, "Logged out successfully!")
#     return render(request, 'registration/logged_out.html')
#     # return redirect("homepage")

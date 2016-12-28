from django.shortcuts import render, render_to_response, redirect

from .forms import ModelContactForm


def contact(request):
    if request.method == 'POST':
        form = ModelContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.save()
            return redirect('/')
    else:
        form = ModelContactForm()

    context = {
        'form': form,
    }

    return render(request, "contact.html", context)

from django.views import generic
from django.contrib.auth.decorators import login_required

from safari.models import TinderImage

class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

class TinderImages(LoginRequiredMixin, generic.ListView):
    queryset = TinderImage.objects.all()
    template_name = 'safari/safari.html'
    paginate_by = 50


from django import forms

class UploadForm(forms.ModelForm):
    class Meta:
        model = TinderImage
        fields = ['image']

from django.shortcuts import render
from django.http import HttpResponseRedirect

@login_required
def upload(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = UploadForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            form.save()   
            return HttpResponseRedirect('/tinder-safari/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = UploadForm()

    return render(request, 'safari/upload.html', {'form': form})

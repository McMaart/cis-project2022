from django.views.generic.edit import FormView
from .forms import FileFieldForm
from django.urls import reverse
from django.shortcuts import render


class FileFieldFormView(FormView):
    form_class = FileFieldForm
    template_name = 'upload/index.html'
    success_url = 'success/'  # Replace with your URL or reverse().
    print("yeah")

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                ...
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


def success(request):
    return render(request, 'success.html')

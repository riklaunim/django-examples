from django.views.generic import TemplateView


class EmberView(TemplateView):
    template_name = 'eblog/blog.html'

ember_view = EmberView.as_view()

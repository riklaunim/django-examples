from django.views import generic


class CanvasViews(generic.TemplateView):
    template_name = 'canvas.html'

canvas = CanvasViews.as_view()

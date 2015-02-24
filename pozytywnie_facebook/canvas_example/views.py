from django.views import generic


class CanvasViews(generic.TemplateView):
    template_name = 'canvas.html'

    def get_context_data(self, **kwargs):
        context = super(CanvasViews, self).get_context_data()
        context['facebook'] = self.request.facebook
        return context

canvas = CanvasViews.as_view()

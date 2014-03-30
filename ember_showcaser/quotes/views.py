from django.views import generic


class MainPageView(generic.TemplateView):
    template_name = 'index.html'

main_page = MainPageView.as_view()

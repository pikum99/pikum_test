from django.views.generic import TemplateView


class Index(TemplateView):
    template_name = "main_page.html"


index = Index.as_view()

from django.db.models.fields.reverse_related import ManyToOneRel
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView

from business_hours.forms import BusinessHourForm
from business_hours.models import BusinessHour
from timetables.models import Timetable


# Create your views here.
class BusinessHourListView(ListView):
    model = BusinessHour
    paginate_by = 10

    def get_verbose_names(self):
        verbose_names = {}
        fields = self.model._meta.get_fields()
        for field in fields:
            if type(field) != ManyToOneRel:
                verbose_names[field.name] = field.verbose_name

        return verbose_names

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "영업 시간 목록"
        context["verbose_names"] = self.get_verbose_names()

        return context


class BusinessHourCreateView(CreateView):
    model = BusinessHour
    form_class = BusinessHourForm
    success_url = reverse_lazy("business_hours:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "시간표 추가"

        return context


class BusinessHourDeleteView(DeleteView):
    model = BusinessHour
    form_class = BusinessHourForm
    success_url = reverse_lazy("business_hours:list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "시간표 추가"

        return context


class BusinessHourUpdateView(UpdateView):
    model = BusinessHour
    form_class = BusinessHourForm
    success_url = reverse_lazy("business_hours:list")

    def get_object(self, queryset=None):
        object = BusinessHour.objects.get(
            branch=self.kwargs["branch"], srl=self.kwargs["srl"]
        )
        return object

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = "시간표 추가"

        return context


class BusinessHourDetailView(DetailView):
    model = Timetable

    def get_queryset(self):
        if "branch" in self.kwargs.keys():
            return self.model.objects.filter(branch=self.kwargs["branch"])
        else:
            return self.model.objects.all()

    def get_object(self):
        return self.get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["detail"] = self.get_queryset()

        context["page_title"] = f"{context['detail'][0].branch} 영업 시간"

        return context

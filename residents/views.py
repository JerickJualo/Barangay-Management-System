from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Resident
from django.urls import reverse_lazy
from .serializers import ResidentSerializer
from rest_framework import viewsets
from .forms import ResidentForm
from django.contrib.auth.mixins import LoginRequiredMixin

class ResidentListView(LoginRequiredMixin, ListView):
    model = Resident
    template_name = 'residents/resident_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        purok = self.request.GET.get('purok')
        street = self.request.GET.get('street')
        household = self.request.GET.get('household')
        if household:
            queryset = queryset.filter(household_id=household)
        elif street:
            queryset = queryset.filter(household__street__id=street)
        elif purok:
            queryset = queryset.filter(household__street__purok__id=purok)
        return queryset

class ResidentCreateView(LoginRequiredMixin, CreateView):
    model = Resident
    form_class = ResidentForm
    template_name = 'residents/resident_form.html'
    success_url = reverse_lazy('resident-list-web')


class ResidentUpdateView(LoginRequiredMixin, UpdateView):
    model = Resident
    template_name = 'residents/resident_form.html'
    success_url = reverse_lazy('resident-list-web')
    form_class = ResidentForm

class ResidentDeleteView(LoginRequiredMixin, DeleteView):
    model = Resident
    template_name = 'residents/resident_confirm_delete.html'
    success_url = reverse_lazy('resident-list-web')

    # VIEWSCLASS FOR API

class ResidentViewSet(viewsets.ModelViewSet):
    queryset = Resident.objects.all()
    serializer_class = ResidentSerializer
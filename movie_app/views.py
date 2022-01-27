from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
class Index(TemplateView):
  template_name = "index.html"

@api_view(["GET"])
def search(request):

  return Response({
    "title":request.GET.get("title",""),
    "date":request.GET.get("date",""),
    "overview":request.GET.get("overview","")
  },status=status.HTTP_200_OK)
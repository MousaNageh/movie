
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.conf import settings
import os
import pandas as pd
import json
from .serializers import SearchSerializer
class Index(TemplateView):
  template_name = "index.html"

@api_view(["GET"])
def search(request):
  title = request.GET.get("title","")
  overview = request.GET.get("overview","")
  date = request.GET.get("date",None)
  if not date :
    date = None
  serializer = SearchSerializer(data={
    "title":title,
    "overview":overview,
    "date":date,
  })
  if serializer.is_valid() : 
      results =[]
      dataSet = pd.read_csv(os.path.join(settings.BASE_DIR, "dataset.csv")) 
      queryData = None
      
      if title and not overview and not date : 
        queryData = dataSet[dataSet["title"].str.contains(title,case=False,na=False)]
        results = json.loads(pd.DataFrame(queryData).to_json(orient="records"))

      elif overview and not title and not date: 
          queryData = dataSet[
            dataSet['overview'].str.contains(overview,case=False,na=False) 
            ]
          results = json.loads(pd.DataFrame(queryData).to_json(orient="records"))
      
      elif not title and not overview and date : 
        queryData = dataSet[
            pd.to_datetime(dataSet['release_date']) == pd.to_datetime(date) 
            ]
        results = json.loads(pd.DataFrame(queryData).to_json(orient="records"))
      
      elif title and overview and not date :  
        queryData = dataSet[
              dataSet["title"].str.contains(title,case=False,na=False)&
              dataSet['overview'].str.contains(overview,case=False,na=False) 
          ]
        results = json.loads(pd.DataFrame(queryData).to_json(orient="records"))
      
      elif title and not overview and date :  
        queryData = dataSet[
              (pd.to_datetime(dataSet['release_date']) == pd.to_datetime(date))& 
              dataSet["title"].str.contains(title,case=False,na=False)
          ]
        results = json.loads(pd.DataFrame(queryData).to_json(orient="records"))
      
      elif not title and overview and date :  
        queryData = dataSet[
              (pd.to_datetime(dataSet['release_date']) == pd.to_datetime(date))& 
              dataSet['overview'].str.contains(overview,case=False,na=False) 
          ]
        results = json.loads(pd.DataFrame(queryData).to_json(orient="records"))
      
      
      elif title and overview and date :  
        queryData = dataSet[
              (pd.to_datetime(dataSet['release_date']) == pd.to_datetime(date))& 
              dataSet["title"].str.contains(title,case=False,na=False)&
              dataSet['overview'].str.contains(overview,case=False,na=False)
        ]
        results = json.loads(pd.DataFrame(queryData).to_json(orient="records"))
      
      return Response({"results":results},status=status.HTTP_200_OK)
  else : 
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

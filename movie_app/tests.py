
from rest_framework.test import APITestCase
from django.urls import reverse
# Create your tests here.
class TestSetUp(APITestCase):
  def setUp(self) :
      self.query ={
        "title":"the godfather",
        "overview":"Raj is a rich",
        "date":"2020-09-03"
      }
      self.searchUrl = reverse("searchmovie")
      return super().setUp()
  def tearDown(self) :
      return super().tearDown()

class TestView(TestSetUp):
  def test_query_by_title(self):
    title = self.query["title"]
    response =  self.client.get(F"{self.searchUrl}?title={title}")
    self.assertEqual(response.status_code , 200) 
  
  def test_query_by_overview(self):
    overview = self.query["overview"]
    response =  self.client.get(F"{self.searchUrl}?overview={overview}")
    self.assertEqual(response.status_code , 200) 
  
  def test_query_by_date(self):
    date = self.query["date"]
    response =  self.client.get(F"{self.searchUrl}?date={date}")
    self.assertEqual(response.status_code , 200) 
  
  def test_query_by_title_and_date(self):
    date = self.query["date"]
    title = self.query["title"]
    response =  self.client.get(F"{self.searchUrl}?date={date}&title={title}")
    self.assertEqual(response.status_code , 200) 
  
  def test_query_by_title_and_overview(self):
    overview = self.query["overview"]
    title = self.query["title"]
    response =  self.client.get(F"{self.searchUrl}?overview={overview}&title={title}")
    self.assertEqual(response.status_code , 200) 
  
  def test_query_by_overview_and_date(self):
    overview = self.query["overview"]
    date = self.query["date"]
    response =  self.client.get(F"{self.searchUrl}?overview={overview}&date={date}")
    self.assertEqual(response.status_code , 200) 
  
  def test_query_by_overview_and_overview_title(self):
    overview = self.query["overview"]
    date = self.query["date"]
    title = self.query["title"]
    response =  self.client.get(F"{self.searchUrl}?overview={overview}&date={date}&title={title}")
    self.assertEqual(response.status_code , 200) 

from django.db import models
import requests
# Create your models here.
class Book(models.Model):
    isbn = models.CharField(max_length=10)
    author = models.TextField()
    title = models.TextField()
    link = models.URLField()
    mileage = models.IntegerField()
    price = models.IntegerField()
    fixed_price = models.BooleanField()
    pub_date = models.DateField()
    @classmethod
    def insert_data(cls):
        API_URL = 'https://www.aladin.co.kr/ttb/api/ItemList.aspx'
        API_KEY = 'ttbddoriboy1501001'
        params = {
            'ttbkey': API_KEY,
            'Querytype': "ItemNewAll",
            "SearchTarget": "Book",
            "Version": "20131101",
            "output": "js",
            "start" : '1',
            "MaxResults": '50'

        }
        response = requests.get(API_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            for item in data['item']:
                my_model = cls(isbn = item['isbn'], author = item['author'], title = item['title'],
                                link = item['link'], mileage = item['mileage'],
                                price = item['priceSales'], fixed_price = item['fixedPrice'],  
                                pub_date = item['pubDate'])
                my_model.save()
        


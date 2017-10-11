# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import psycopg2
from tutorial.items import *

class TutorialPipeline(object):
  def __init__(self):
    self.connection = psycopg2.connect(host='/scrapehost', database='scrapedb', user='postgres', password='password')
    self.cursor = self.connection.cursor()
 
  def process_item(self, item, spider):
    # check item type to decide which table to insert
        self.cursor.execute("""INSERT INTO odi_ranking (Position, Player, Country, Rating, Best_Rank) VALUES(%s, %s, %s, %s, %s)""", (item.get('Position'), item.get('Player'), item.get('Country'), item.get('Rating'),  item.get('Best_Rank') ))

        self.connection.commit()
        self.cursor.fetchall()
        return item
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Ssr1Pipeline:
    def __init__(self):
        self.connection = pymysql.connect(
            user='root',  # 换上你自己的账密和数据库
            password='123456',
            db='scrapy_demo',
        )
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        table_sql = """CREATE TABLE IF NOT EXISTS ssr1 (
            id INT PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(255),
            category VARCHAR(255),
            area VARCHAR(255),
            time VARCHAR(255),
            publish_time VARCHAR(255))CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
        """
        self.cursor.execute(table_sql)
        self.connection.commit()


    def process_item(self, item, spider):
        # 将item数据插入到ssr1表中
        try:
            insert_sql = """INSERT INTO ssr1(title, category, area, time, publish_time) VALUES (%s, %s,%s, %s, %s)"""
            self.cursor.execute(insert_sql, (item['title'], item['category'], item['area'], item['time'], item['publish_time']))

            self.connection.commit()
        except pymysql.MySQLError as e:
            spider.logger.error(f"Error saving item: {e}")
            print(e)
        return item


    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

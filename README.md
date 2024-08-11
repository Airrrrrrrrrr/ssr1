这是一个简单的scrapy爬虫

step1：scrapy startproject projectname	//创建scrapy项目

step2：cd projectname；scrapy genspider example example.com；	//初始化

step3：通过pycharm打开已经建好的scrapy项目

step4：在setting.py中设置相应的属性；eg：ROBOTSTXT_OBEY = False ；User-Agent；Item-Pipeline；

step5：在item.py中编写对应需要获取的属性；eg：name = scrapy.Field()

step6：在example.py下导入item.py	//from ssr1.items import Ssr1Item

step7：在parse函数中编写获取信息的代码（xpath定位），以及翻页操作，获取完成后记得yield item，才会传输到pipeline去；	//item记得实例化

step8：编写pipeline.py，数据库的连接，插入语句；或文件读写保存；

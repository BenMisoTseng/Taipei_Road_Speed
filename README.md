#Taipei_Road_Speed DataMining
目前抓資料是用scrapy框架做web crawler
先抓取兩個資料，道路速率與每段時間的氣象
###道路速率
道路速率是直接執行下載連結 
```
urlopen('http://data.taipei/opendata/datalist/datasetMeta/download?id=38f2d8e0-07ce-4201-87cb-3462be39d8aa&rid=5aacba65-afda-4ad5-88f5-6026934140e6')
```

由於道路速率是每五分鐘更新一次 所以在AWS ubuntu伺服器上 在crontab加上
```
#run script every 5 minutes
*/5 * * * * ubuntu python /autodownload.py
```
讓他每五分鐘抓一次資料

###每日天氣
天氣部分從中央氣象局網站抓取臺北市的天氣資料
包含時間、溫度、天氣、風力大小、能見度、濕度、雨量等等作為日後分析的因素
這部分利用scrapy 
```
weathertime = response.xpath("//table/tr[2]/th/text()").extract()
```
抓取資料並儲存
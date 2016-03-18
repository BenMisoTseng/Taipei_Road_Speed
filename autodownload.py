import urllib2
import pytz
from datetime import datetime, timedelta

tz = pytz.timezone(pytz.country_timezones('tw')[0])
filename = datetime.strftime(datetime.now(tz) - timedelta(minutes =11), '%Y-%m-%d_%H-%M')

response = urllib2.urlopen('http://data.taipei/opendata/datalist/datasetMeta/download?id=38f2d8e0-07ce-4201-87cb-3462be39d8aa&rid=5aacba65-afda-4ad5-88f5-6026934140e6')
taipeiroadspeed = response.read()

taipeiroadspeed_f = open('./taipeiroadspeed/' + filename + '.xml', 'w+')
taipeiroadspeed_f.write(taipeiroadspeed)
taipeiroadspeed_f.closed

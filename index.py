from gmap import google_map_search

keyword = 'Game+Stores+near+Regional+Municipality+of+Peel,+ON,+Canada'
location = '@43.6521638,-79.8970969'
file_name = 'game store'
# 


# 
keyword = "{} {}".format(keyword, location)
keyword = "https://www.google.com/maps/search/{}".format(
    '+'.join(keyword.split(' ')))
print(keyword)
file_name = file_name+'.csv'
google_map_search(keyword,0,file_name)
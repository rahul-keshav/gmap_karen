from gmap import google_map_search
f = open('url.txt','rt')
url = f.read()
f.close()
# 
file_name = 'hardware store'
# 
file_name = 'data_2/'+file_name+'.csv'
google_map_search(url,0,file_name)
import pandas as pd






dict2 = {
        "title":[],
        "address":[],
        "opening_hrs":[],
        "website":[],
        "phone":[],
        "plus_code":[],
        }

clmn = clmn = list(dict2.keys())

def save_data(data):
    try:
        df2 = pd.read_csv('gmap_details.csv')
    except:
        df2 = pd.DataFrame(dict2)
    
    df0 = pd.DataFrame([data], columns=clmn)
    df = df2.append(df0,ignore_index=True)    
    df.to_csv('gmap_details.csv',index=False)
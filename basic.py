import pandas as pd



dict2 = {"google_category":[],
        "title":[],
        "address":[],
        "opening_hrs":[],
        "website":[],
        "phone":[],
        "plus_code":[],
        "review":[],
        "total number of reviews":[]
        }

clmn = list(dict2.keys())

def save_data(data,file_name):
    try:
        df2 = pd.read_csv(file_name)
    except:
        df2 = pd.DataFrame(dict2)
    
    df0 = pd.DataFrame([data], columns=clmn)
    df = df2.append(df0,ignore_index=True)    
    df.to_csv(file_name,index=False)



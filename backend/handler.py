import json
import pandas as pd

def dominancia(event, context):
    try:
        df = read_table(event)
        check_dominance=[]
        for column in df:
            check_dominance.append(df[column].idxmax())  
        if all(x == check_dominance[0] for x in check_dominance):
            result = check_dominance[0]
        else:
            result = None

        return response(200, { "result": result })
    except Exception as e:
        return response(500, { "error": str(e) })

def maximax(event, context):
    try:
        df = read_table(event)
        df_max = max(df.max())
        maximax=df.loc[df.isin([df_max]).any(axis=1)].index.tolist()
        return response(200, { "result": maximax[0] })
    except Exception as e:
        return response(500, { "error": str(e) })

def read_table(event):
    df = pd.DataFrame(json.loads(event['body'])['table'])
    df = df.set_index(df.columns[0])
    return df

def response(status_code, data):
    return {
        "statusCode": status_code,
        "body": json.dumps(data),
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Credentials": True,
        },
    }
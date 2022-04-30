import json
import pandas as pd

def dominancia(event, context):
    df = read_matrix(event)
    check_dominance=[]
    for column in df:
        check_dominance.append(df[column].idxmax())  
    if all(x == check_dominance[0] for x in check_dominance):
        result = check_dominance[0]
    else:
        result = None

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }

def maximax(event, context):
    df = read_matrix(event)
    df_max = max(df.max())
    maximax=df.loc[df.isin([df_max]).any(axis=1)].index.tolist()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": maximax[0]
        })
    }

def read_matrix(event):
    print(1, event['body'], type(event['body']))
    df = pd.DataFrame(json.loads(event['body']), header=0)
    df = df.set_index(df.columns[0])
    return df
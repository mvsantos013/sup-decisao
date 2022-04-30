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

def maximin(event, context):
    try:
        df = read_table(event)
        values = []
        indexes = []
        for column in df:
            values.append(df[column].min())
            indexes.append(df[column].idxmin())
        maximin = indexes[values.index(max(values))]
        return response(200, { "result": maximin })
    except Exception as e:
        return response(500, { "error": str(e) })

def minimax_regret(event, context):
    try:
        df = read_table(event)
        greatest = df.max().tolist()
        elements = df.values.tolist()
        minmaxregret=[]
        for i in range(0,len(greatest)):
            regrets=[]  
            for j in range(0, len(elements)):
                regrets.append(greatest[j] - elements[i][j])
            minmaxregret.append(max(regrets))
        minmaxregret = minmaxregret.index(min(minmaxregret))
        return response(200, { "result": df.index[minmaxregret] })
    except Exception as e:
        return response(500, { "error": str(e) })

def media(event, context):
    try:
        df = read_table(event)
        averages = (df.mean(axis=1).tolist())
        media = averages.index(max(averages))
        return response(200, { "result": df.index[media] })
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
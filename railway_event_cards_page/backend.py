import pandas as pd
import json
from datetime import datetime

def read_railway_events(file_name, sheet='Лист11'):
    df = pd.read_excel(file_name, sheet_name=sheet)
    df = df.drop(df.columns[0], axis=1)
    df = df.drop([0, 1, 3])
    df.columns = df.iloc[0]
    df = df.drop(df.index[0])
    df = df.set_index(df.columns[0])
    df.index.name = '№'
    df.columns.name = None
    df = df.loc[:, ~pd.isnull(df.columns)]
    return df

def datetime_converter(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

def excel_to_json(excel_path, json_path):
    xls = pd.ExcelFile(excel_path)
    
    result = {}
    
    try:
        df = read_railway_events(excel_path)
    
        # Преобразуем datetime в строки
        for col in df.columns:
            if pd.api.types.is_datetime64_any_dtype(df[col]):
                df[col] = df[col].apply(lambda x: x.isoformat() if pd.notnull(x) else None)
            
        # Преобразуем в список словарей
        result = df.where(pd.notnull(df), None).to_dict('records')
    except Exception as e:
        print(f"Ошибка при обработке листа {sheet_name}: {str(e)}")
        result = []
    
    # Сохраняем в JSON с обработкой datetime
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2, default=datetime_converter)
    
    print(f"Данные сохранены в {json_path}")

if __name__ == "__main__":
    excel_to_json("data.xlsx", "data.json")

def checkNullValues(df):
    flag = False
    # Verificar se alguma coluna possui dados faltantes
    for column in df.columns.values:
        x = df[column].isnull().sum()
        if x > 0:
            print(f'{column} = {x}')
            flag = True
            
    if not flag:
        print("Nenhum dado faltante!")
        
        
def fillNullWithMode(df, columns):
    newDf = df.copy()
    print()
    for column in columns:
        mode_value = newDf[column].mode()[0]
        newDf[column] = newDf[column].fillna(mode_value)
        
    return newDf


def fillNullWithMedian(df, columns):
    newDf = df.copy()
    for column in columns:
        median_value = newDf[column].median()
        newDf[column] = newDf[column].fillna(median_value)
        
    return newDf
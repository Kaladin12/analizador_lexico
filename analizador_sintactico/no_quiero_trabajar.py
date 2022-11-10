import pandas as pd
import json

df = pd.read_csv('ll1.csv')
df = df.fillna('-')
df.to_csv('ll1_2.csv')
print(df.head())


# primera columna son las variables
variables = df.iloc[:, 0]
final = {}
for var in variables:
    final[var] = {}

# por cada variable crear un diccionario donde "key" = column name y : "value" valor de celda
i = 0

# final['S']['$'] = cont de celda
for key in final:
    # quiero la fila que tiene en la primera columna = key 
    row_data = df.iloc[i,:]
    # cada columna
    for data in row_data.iteritems():
        col, cell = data
        splitted = cell.split()
        if len(splitted) == 1:
            final[key][col] = [splitted]
        else:
            splitted = [[i] for i in splitted[2:]]
            final[key][col] = splitted
    i += 1


print(final)

json_obj = json.dumps(final)
with open('final.json', 'w') as f:
    f.write(json_obj)
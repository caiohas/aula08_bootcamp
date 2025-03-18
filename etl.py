import pandas as pd
import os
import glob

# uma funcao de extract que le e consolida jsons
pasta = "data"
arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
df_total = pd.concat(df_list,ignore_index=True)

print(df_total)
# uma funcao que transforma

# uma funcao que da load em um csv ou parquet
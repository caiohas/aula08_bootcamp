import pandas as pd
import os
import glob

# uma funcao de extract que le e consolida jsons
def extrair_dados_json(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, "*.json"))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list,ignore_index=True)
    return df_total

# uma funcao que transforma
def calcular_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total Vendas"] = df["Quantidade"] * df["Venda"]
    return df

# uma funcao que da load em um csv ou parquet
def carregar_dados(df: pd.DataFrame, formato_saida: list) -> None:
    for formato in formato_saida:
        if formato == 'csv':
            df.to_csv("dados.csv")
        if formato == 'parquet':
            df.to_parquet("dados.parquet")
    
    return None


if __name__ == "__main__":
    pasta_argumento: str = 'data'
    df = extrair_dados_json(pasta=pasta_argumento)
    df = calcular_total_vendas(df)
    formato_saida: list = ["csv", "parquet"] 
    carregar_dados(df, formato_saida)

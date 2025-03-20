from etl import pipeline_calcular_total_vendas_consolidado

pasta_argumento = 'data'
formato_saida = ["csv", "parquet"]

pipeline_calcular_total_vendas_consolidado(pasta_argumento, formato_saida)
import pandas as pd


class MiDataFrame(pd.DataFrame):
    def __init__(self, args):
        super().__init__(args)
        print(args)

    def prom_columnas(self):
        return self.mean()

    def obtener_maximo(self):
        return self.max()

    def obtener_minimo(self):
        return self.min()


datos = {
    'A': [24.0, 33.2, 30.2, 29.4, 29.3],
    'B': [34.0, 30.2, 31.2, 29.4, 29.3]
}

df = MiDataFrame(datos)
print(df.prom_columnas())
print(df.obtener_maximo())
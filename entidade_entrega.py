# Classe Entidade da Entrega
class Entrega:
    def __init__(self, origem, destino, tipo, valor, data_contratacao, data_entrega, tempo, formaPagamento, status, custo_adicional, observacao):
        self.origem = origem
        self.destino = destino
        self.tipo = tipo
        self.valor = valor
        self.data_contratacao = data_contratacao
        self.data_entrega = data_entrega
        self.tempo = tempo
        self.forma_pagamento = formaPagamento
        self.status = status
        self.custo_adicional = custo_adicional
        self.obs = observacao

    def __str__(self):
        return f"""
        Origem: {self.origem}
        Destino: {self.destino}
        Tipo de carga: {self.tipo}
        Valor do frete: {self.valor}
        Data de Contratação: {self.data_contratacao}
        Data de Entrega: {self.data_entrega}
        Tempo de entrega (dias): {self.tempo}
        Status: {self.status}
        Custo Adicional: {self.custo_adicional}
        Observação: {self.obs}"""
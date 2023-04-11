# TODO: Enviar classes para erpbrasil.base


class CampoPosicional:
    def __init__(self, nome, valor, obrigatorio, tipo, tamanho, posicao_inicial, posicao_final):
        self.nome = nome
        self.valor = valor
        self.obrigatorio = obrigatorio
        self.tipo = tipo
        self.tamanho = tamanho
        self.posicao_inicial = posicao_inicial
        self.posicao_final = posicao_final

    def exportar(self):
        if self.tipo == "ALFA":
            formatado = str(self.valor).ljust(self.tamanho)
        elif self.tipo == "NUM":
            formatado = str(self.valor).rjust(self.tamanho, "0")
        else:
            raise ValueError(f"Tipo desconhecido: {self.tipo}")

        return formatado[: self.tamanho]


class Registro:
    campos = []

    def exportar(self):
        return ''.join([campo.exportar() for campo in self.campos])

    def __setattr__(self, name, value):
        if name != "campos" and name in {campo.nome for campo in self.campos}:
            for campo in self.campos:
                if campo.nome == name:
                    campo.valor = value
                    return
            raise AttributeError(f"Campo desconhecido: {name}")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in {campo.nome for campo in self.campos}:
            for campo in self.campos:
                if campo.nome == name:
                    return campo.valor
            raise AttributeError(f"Campo desconhecido: {name}")
        return super().__getattribute__(name)


class Arquivo:
    def __init__(self, registros=None):
        if registros is None:
            registros = []
        self.registros = registros

    def adicionar_registro(self, registro):
        self.registros.append(registro)

    def exportar_txt(self, caminho_arquivo):
        with open(caminho_arquivo, "w") as arquivo:
            for registro in self.registros:
                arquivo.write(registro.exportar())

    def exportar(self):
        texto = ''
        for registro in self.registros:
            texto += registro.exportar()
        return texto

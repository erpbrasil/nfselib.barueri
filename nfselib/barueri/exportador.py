

class CampoPosicional:
    def __init__(self, nome, valor, obrigatorio, tipo, tamanho, posicao_inicial, posicao_final):
        """A class representing a positional field in a file.

        Args:
            nome (str): The name of the field.
            valor (Any): The value of the field.
            obrigatorio (bool): Whether the field is required or not.
            tipo (str): The type of the data ("ALFA" or "NUM").
            tamanho (int): The size of the field.
            posicao_inicial (int): The starting position of the field.
            posicao_final (int): The ending position of the field.
        """
        self.nome = nome
        self.valor = valor
        self.obrigatorio = obrigatorio
        self.tipo = tipo
        self.tamanho = tamanho
        self.posicao_inicial = posicao_inicial
        self.posicao_final = posicao_final

    def exportar(self):
        """Formats and exports the field value based on its type.

        Returns:
            str: The formatted field value.
        """
        if self.tipo == "ALFA":
            formatado = str(self.valor).ljust(self.tamanho)  # Format the string as left-justified
        elif self.tipo == "NUM":
            formatado = str(self.valor).rjust(self.tamanho, "0")  # Format the string as right-justified with zeroes added to the left
        else:
            raise ValueError(f"Tipo desconhecido: {self.tipo}")  # Raise an error if the data type is unknown

        return formatado[: self.tamanho]  # Return only the first n characters of the formatted string based on the field size


class Registro:
    campos = []  # A list to store the fields in the record

    def exportar(self):
        """Exports the record by concatenating its fields.

        Returns:
            str: The concatenated fields.
        """
        return ''.join([campo.exportar() for campo in self.campos])

    def __setattr__(self, name, value):
        """Sets the value of a field in the record.

        Args:
            name (str): The name of the field.
            value (Any): The new value of the field.

        Raises:
            AttributeError: If the field name is not recognized.
        """
        if name != "campos" and name in {campo.nome for campo in self.campos}:
            for campo in self.campos:
                if campo.nome == name:
                    campo.valor = value  # Set the value of the field
                    return
        super().__setattr__(name, value)

    def __getattr__(self, name):
        """Gets the value of a field in the record.

        Args:
            name (str): The name of the field.

        Raises:
            AttributeError: If the field name is not recognized.

        Returns:
            Any: The value of the field.
        """
        if name in {campo.nome for campo in self.campos}:
            for campo in self.campos:
                if campo.nome == name:
                    return campo.valor  # Return the value of the field
            raise AttributeError(f"Campo desconhecido: {name}")  # Raise an error if the field name is not recognized
        return super().__getattribute__(name)


class Arquivo:
    def __init__(self, registros=None):
        """Initializes a new file object.

        Args:
            registros (list[Registro], optional): A list of records in the file. Defaults to None.
        """
        if registros is None:
            registros = []
        self.registros = registros  # Initializes the list of records

    def adicionar_registro(self, registro):
        """Adds a record to the file.

        Args:
            registro (Registro): The record to be added.
        """
        self.registros.append(registro)

    def exportar_txt(self, caminho_arquivo):
        """Exports the file as a text file.

        Args:
            caminho_arquivo (str): The file path to save the exported file.
        """
        with open(caminho_arquivo, "w") as arquivo:  # Opens the file for writing
            for registro in self.registros:
                arquivo.write(registro.exportar())  # Writes each record to the file

    def exportar(self):
        """Exports the file as a string.

        Returns:
            str: The concatenated records in the file.
        """
        texto = ''
        for registro in self.registros:
            texto += registro.exportar()  # Concatenates the export of each record
        return texto  # Returns the concatenated result

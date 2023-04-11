from nfselib.barueri.rps import RPS
from nfselib.barueri.rps import RegistroTipo1
from nfselib.barueri.rps import RegistroTipo2
from nfselib.barueri.rps import RegistroTipo3
from nfselib.barueri.rps import RegistroTipo9


def test_gerar_registro_tipo_1():
    # Instanciar objeto RPSBarueri

    registro_tipo1 = RegistroTipo1()
    registro_tipo1.InscricaoContribuinte = "12345"
    registro_tipo1.IdentificacaoRemessaContribuinte = "3333333"
    registro_tipo2 = RegistroTipo2()
    registro_tipo3 = RegistroTipo3()
    registro_tipo9 = RegistroTipo9()

    # Criando um objeto RPS com os registros
    rps = RPS([registro_tipo1, registro_tipo2, registro_tipo3, registro_tipo9])

    # Exportando RPS para um arquivo TXT
    rps.exportar_txt("rps_teste.txt")

    # Lendo e imprimindo o conteúdo do arquivo TXT gerado
    # with open("rps_teste.txt", "r") as arquivo:
    #     conteudo = arquivo.read()
    #     print(conteudo)

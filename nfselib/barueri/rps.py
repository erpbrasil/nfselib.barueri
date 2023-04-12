from .exportador import Arquivo
from .exportador import CampoPosicional
from .exportador import Registro


class RPS(Arquivo):
    pass


class RegistroTipo1(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "1", True, "NUM", 1, 1, 1),
        CampoPosicional("InscricaoContribuinte", None, True, "ALFA", 7, 2, 8),
        CampoPosicional("VersaoLayout", "PMB002", True, "NUM", 6, 9, 14),
        CampoPosicional("IdentificacaoRemessaContribuinte", None, True, "NUM", 11, 15, 25),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 26, 26),
    ]


class RegistroTipo2(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "2", True, "NUM", 1, 1, 1),
        CampoPosicional("TipoRPS", None, True, "ALFA", 5, 2, 6),
        CampoPosicional("SerieRPS", None, False, "ALFA", 4, 7, 10),
        CampoPosicional("SerieNFe", None, False, "ALFA", 5, 11, 15),
        CampoPosicional("NumeroRPS", None, True, "NUM", 10, 16, 25),
        CampoPosicional("DataRPS", None, True, "NUM", 8, 26, 33),
        CampoPosicional("HoraRPS", None, True, "NUM", 6, 34, 39),
        CampoPosicional("SituacaoRPS", None, True, "ALFA", 1, 40, 40),
        CampoPosicional("CodigoMotivoCancelamento", None, False, "ALFA", 2, 41, 42),
        CampoPosicional("NumeroNFeCancelada", None, False, "NUM", 7, 43, 49),
        CampoPosicional("SerieNFeCancelada", None, False, "ALFA", 5, 50, 54),
        CampoPosicional("DataEmissaoNFeCancelada", None, False, "NUM", 8, 55, 62),
        CampoPosicional("DescricaoCancelamento", None, False, "ALFA", 180, 63, 242),
        CampoPosicional("CodigoServicoPrestado", None, True, "NUM", 9, 243, 251),
        CampoPosicional("LocalPrestacaoServico", None, False, "ALFA", 1, 252, 252),
        CampoPosicional("ServicoPrestadoViasPublicas", None, False, "ALFA", 1, 253, 253),
        CampoPosicional("EnderecoLogradouroLocalServico", None, False, "ALFA", 75, 254, 328),
        CampoPosicional("NumeroLogradouroLocalServico", None, False, "ALFA", 9, 329, 337),
        CampoPosicional("ComplementoLogradouroLocalServico", None, False, "ALFA", 30, 338, 367),
        CampoPosicional("BairroLogradouroLocalServico", None, False, "ALFA", 40, 368, 407),
        CampoPosicional("CidadeLogradouroLocalServico", None, False, "ALFA", 40, 408, 447),
        CampoPosicional("UFLogradouroLocalServico", None, False, "ALFA", 2, 448, 449),
        CampoPosicional("CEPLogradouroLocalServico", None, False, "ALFA", 8, 450, 457),
        CampoPosicional("QuantidadeServico", None, True, "NUM", 6, 458, 463),
        CampoPosicional("ValorServico", None, True, "NUM", 15, 464, 478),
        CampoPosicional("Reservado", None, False, "ALFA", 5, 479, 483),
        CampoPosicional("ValorTotalRetencoes", None, True, "NUM", 15, 484, 498),
        CampoPosicional("TomadorEstrangeiro", None, True, "NUM", 1, 499, 499),
        CampoPosicional("PaisNacionalidadeTomadorEstrangeiro", None, False, "NUM", 3, 500, 502),
        CampoPosicional("ServicoExportacao", None, False, "NUM", 1, 503, 503),
        CampoPosicional("IndicadorCPFCNPJTomador", None, False, "NUM", 1, 504, 504),
        CampoPosicional("CPFCNPJTomador", None, False, "NUM", 14, 505, 518),
        CampoPosicional("RazaoSocialNomeTomador", None, True, "ALFA", 60, 519, 578),
        CampoPosicional("EnderecoLogradouroTomador", None, False, "ALFA", 75, 579, 653),
        CampoPosicional("NumeroLogradouroTomador", None, False, "ALFA", 9, 654, 662),
        CampoPosicional("ComplementoLogradouroTomador", None, False, "ALFA", 30, 663, 692),
        CampoPosicional("BairroLogradouroTomador", None, False, "ALFA", 40, 693, 732),
        CampoPosicional("CidadeLogradouroTomador", None, False, "ALFA", 40, 733, 772),
        CampoPosicional("UFLogradouroTomador", None, False, "ALFA", 2, 773, 774),
        CampoPosicional("CEPLogradouroTomador", None, False, "ALFA", 8, 775, 782),
        CampoPosicional("EmailTomador", None, False, "ALFA", 152, 783, 934),
        CampoPosicional("Fatura", None, False, "NUM", 6, 935, 940),
        CampoPosicional("ValorFatura", None, False, "NUM", 15, 941, 955),
        CampoPosicional("FormaPagamento", None, False, "ALFA", 15, 956, 970),
        CampoPosicional("DiscriminacaoServico", None, True, "ALFA", 1000, 971, 1970),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 1971, 1971),
    ]


class RegistroTipo3(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "3", True, "NUM", 1, 1, 1),
        CampoPosicional("CodigoOutrosValores", None, True, "ALFA", 2, 2, 3),
        CampoPosicional("Valor", None, True, "NUM", 15, 4, 18),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 19, 19),
    ]


class RegistroTipo9(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "9", True, "NUM", 1, 1, 1),
        CampoPosicional("NumeroTotalLinhas", None, True, "NUM", 7, 2, 8),
        CampoPosicional("ValorTotalServicos", None, True, "NUM", 15, 9, 23),
        CampoPosicional("ValorTotalValores", None, True, "NUM", 15, 24, 38),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 39, 39),
    ]

from .exportador import Arquivo
from .exportador import CampoPosicional
from .exportador import Registro


class RPS(Arquivo):
    pass


class RegistroTipo1(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "1", True, "NUM", 1, 1, 1),
        CampoPosicional("InscricaoContribuinte", "", True, "ALFA", 7, 2, 8),
        CampoPosicional("VersaoLayout", "PMB003", True, "ALFA", 6, 9, 14),
        CampoPosicional("IdentificacaoRemessaContribuinte", "", True, "NUM", 11, 15, 25),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 26, 26),
    ]


class RegistroTipo2(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "2", True, "NUM", 1, 1, 1),
        CampoPosicional("TipoRPS", "", True, "ALFA", 5, 2, 6),
        CampoPosicional("SerieRPS", "", False, "ALFA", 4, 7, 10),
        CampoPosicional("SerieNFe", "", False, "ALFA", 5, 11, 15),
        CampoPosicional("NumeroRPS", "", True, "NUM", 10, 16, 25),
        CampoPosicional("DataRPS", "", True, "NUM", 8, 26, 33),
        CampoPosicional("HoraRPS", "", True, "NUM", 6, 34, 39),
        CampoPosicional("SituacaoRPS", "", True, "ALFA", 1, 40, 40),
        CampoPosicional("CodigoMotivoCancelamento", "", False, "ALFA", 2, 41, 42),
        CampoPosicional("NumeroNFeCancelada", "", False, "NUM", 7, 43, 49),
        CampoPosicional("SerieNFeCancelada", "", False, "ALFA", 5, 50, 54),
        CampoPosicional("DataEmissaoNFeCancelada", "", False, "NUM", 8, 55, 62),
        CampoPosicional("DescricaoCancelamento", "", False, "ALFA", 180, 63, 242),
        CampoPosicional("CodigoServicoPrestado", "", True, "NUM", 9, 243, 251),
        CampoPosicional("LocalPrestacaoServico", "", False, "ALFA", 1, 252, 252),
        CampoPosicional("ServicoPrestadoViasPublicas", "", False, "ALFA", 1, 253, 253),
        CampoPosicional("EnderecoLogradouroLocalServico", "", False, "ALFA", 75, 254, 328),
        CampoPosicional("NumeroLogradouroLocalServico", "", False, "ALFA", 9, 329, 337),
        CampoPosicional("ComplementoLogradouroLocalServico", "", False, "ALFA", 30, 338, 367),
        CampoPosicional("BairroLogradouroLocalServico", "", False, "ALFA", 40, 368, 407),
        CampoPosicional("CidadeLogradouroLocalServico", "", False, "ALFA", 40, 408, 447),
        CampoPosicional("UFLogradouroLocalServico", "", False, "ALFA", 2, 448, 449),
        CampoPosicional("CEPLogradouroLocalServico", "", False, "ALFA", 8, 450, 457),
        CampoPosicional("QuantidadeServico", "", True, "NUM", 6, 458, 463),
        CampoPosicional("ValorServico", "", True, "NUM", 15, 464, 478),
        CampoPosicional("Reservado", "", False, "ALFA", 5, 479, 483),
        CampoPosicional("ValorTotalRetencoes", "", True, "NUM", 15, 484, 498),
        CampoPosicional("TomadorEstrangeiro", "", True, "NUM", 1, 499, 499),
        CampoPosicional("PaisNacionalidadeTomadorEstrangeiro", "", False, "NUM", 3, 500, 502),
        CampoPosicional("ServicoExportacao", "", True, "NUM", 1, 503, 503),
        CampoPosicional("IndicadorCPFCNPJTomador", "", False, "NUM", 1, 504, 504),
        CampoPosicional("CPFCNPJTomador", "", False, "NUM", 14, 505, 518),
        CampoPosicional("RazaoSocialNomeTomador", "", True, "ALFA", 60, 519, 578),
        CampoPosicional("EnderecoLogradouroTomador", "", False, "ALFA", 75, 579, 653),
        CampoPosicional("NumeroLogradouroTomador", "", False, "ALFA", 9, 654, 662),
        CampoPosicional("ComplementoLogradouroTomador", "", False, "ALFA", 30, 663, 692),
        CampoPosicional("BairroLogradouroTomador", "", False, "ALFA", 40, 693, 732),
        CampoPosicional("CidadeLogradouroTomador", "", False, "ALFA", 40, 733, 772),
        CampoPosicional("UFLogradouroTomador", "", False, "ALFA", 2, 773, 774),
        CampoPosicional("CEPLogradouroTomador", "", False, "ALFA", 8, 775, 782),
        CampoPosicional("EmailTomador", "", False, "ALFA", 152, 783, 934),
        CampoPosicional("Fatura", "", False, "NUM", 6, 935, 940),
        CampoPosicional("ValorFatura", "", False, "NUM", 15, 941, 955),
        CampoPosicional("FormaPagamento", "", False, "ALFA", 15, 956, 970),
        CampoPosicional("DiscriminacaoServico", "", True, "ALFA", 1000, 971, 1970),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 1971, 1971),
    ]


class RegistroTipo3(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "3", True, "NUM", 1, 1, 1),
        CampoPosicional("CodigoOutrosValores", "", True, "ALFA", 2, 2, 3),
        CampoPosicional("Valor", "", True, "NUM", 15, 4, 18),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 19, 19),
    ]

class RegistroTipo4(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "4", True, "NUM", 1, 1, 1),
        CampoPosicional("OptanteSimplesNacional", "", True, "NUM", 1, 2, 2),
        CampoPosicional("RegimeApuracaoSN", "", False, "NUM", 1, 3, 3),
        CampoPosicional("CodigoPaisLocalServico", "", False, "NUM", 3, 4, 6),
        CampoPosicional("CodigoCidadeLocalPrestacao", "", False, "NUM", 7, 7, 13),
        CampoPosicional("CodigoCidadeTomador", "", False, "NUM", 7, 14, 20),
        CampoPosicional("NIF", "", False, "ALFA", 40, 21, 60),
        CampoPosicional("CodigoNBS", "", False, "NUM", 9, 61, 69),
        CampoPosicional("CEPExteriorTomador", "", False, "ALFA", 11, 70, 80),
        CampoPosicional("EstadoProvinciaTomadorExt", "", False, "ALFA", 60, 81, 140),
        CampoPosicional("VinculoPartes", "", False, "NUM", 1, 141, 141),
        CampoPosicional("Reservado", "", False, "ALFA", 30, 142, 171),
        CampoPosicional("CEPExteriorLocalServico", "", False, "ALFA", 11, 172, 182),
        CampoPosicional("EstadoProvinciaLocalExt", "", False, "ALFA", 60, 183, 242),
        CampoPosicional("NomeEvento", "", False, "ALFA", 255, 243, 497),
        CampoPosicional("DataInicioEvento", "", False, "NUM", 8, 498, 505),
        CampoPosicional("DataFimEvento", "", False, "NUM", 8, 506, 513),
        CampoPosicional("CodJustifCancelSubst", "", False, "NUM", 1, 514, 514),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 515, 515),
    ]

class RegistroTipo9(Registro):
    campos = [
        CampoPosicional("TipoRegistro", "9", True, "NUM", 1, 1, 1),
        CampoPosicional("NumeroTotalLinhas", "", True, "NUM", 7, 2, 8),
        CampoPosicional("ValorTotalServicos", "", True, "NUM", 15, 9, 23),
        CampoPosicional("ValorTotalValores", "", True, "NUM", 15, 24, 38),
        CampoPosicional("CaracterFimLinha", "\r\n", True, "ALFA", 1, 39, 39),
    ]

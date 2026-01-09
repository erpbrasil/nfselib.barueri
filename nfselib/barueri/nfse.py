from .exportador import Arquivo
from .exportador import CampoPosicional
from .exportador import Registro

class NFSe(Arquivo):
    pass


class NFSeRegistroTipo1(Registro):
    def __init__(self):
        super().__init__()
        self.campos = [
            CampoPosicional("TipoRegistro", "1", True, "NUM", 1, 1, 1),
            CampoPosicional("InscricaoContribuinte", "", True, "ALFA", 7, 2, 8),
            CampoPosicional("InicioPeriodoTransferencia", "", False, "NUM", 8, 9, 16),
            CampoPosicional("FimPeriodoTransferencia", "", False, "NUM", 8, 17, 24),
            CampoPosicional("VersaoLayout", "PMB003", True, "ALFA", 6, 25, 30),
            CampoPosicional("IdentificacaoRemessaContribuinte", "", False, "NUM", 11, 31, 41),
            # Fim de linha é ASC13 segundo o layout; pro parser normalmente você lê a linha sem o \r
            # então isso aqui é mais útil pro gerador do que pro leitor.
            CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 42, 42),
        ]

class NFSeRegistroTipo2(Registro):
    def __init__(self):
        super().__init__()
        self.campos = [
            CampoPosicional("TipoRegistro", "2", True, "NUM", 1, 1, 1),
            CampoPosicional("SerieNFe", "", True, "ALFA", 4, 2, 5),
            CampoPosicional("NumeroNFe", "", True, "NUM", 7, 6, 12),
            CampoPosicional("DataNFe", "", True, "NUM", 8, 13, 20),      # AAAAMMDD
            CampoPosicional("HoraNFe", "", True, "NUM", 6, 21, 26),      # HHMMSS
            CampoPosicional("CodigoAutenticidade", "", True, "ALFA", 24, 27, 50),
            CampoPosicional("SerieRPS", "", False, "ALFA", 4, 51, 54),
            CampoPosicional("NumeroRPS", "", False, "NUM", 10, 55, 64),
            CampoPosicional("Tributacao", "", True, "NUM", 1, 65, 65),
            CampoPosicional("ISSRetido", "", True, "ALFA", 1, 66, 66),
            CampoPosicional("SituacaoNFe", "", True, "ALFA", 1, 67, 67),
            CampoPosicional("DataCancelamentoNFe", "", False, "NUM", 8, 68, 75),
            CampoPosicional("NumeroGuia", "", False, "NUM", 10, 76, 85),
            CampoPosicional("DataPagamentoGuia", "", False, "NUM", 8, 86, 93),
            CampoPosicional("CPFCNPJTomador", "", False, "NUM", 14, 94, 107),
            CampoPosicional("RazaoSocialNomeTomador", "", True, "ALFA", 100, 108, 207),
            CampoPosicional("EnderecoLogradouroTomador", "", False, "ALFA", 100, 208, 307),
            CampoPosicional("NumeroLogradouroTomador", "", False, "ALFA", 9, 308, 316),
            CampoPosicional("ComplementoLogradouroTomador", "", False, "ALFA", 20, 317, 336),
            CampoPosicional("BairroLogradouroTomador", "", False, "ALFA", 40, 337, 376),
            CampoPosicional("CidadeLogradouroTomador", "", False, "ALFA", 40, 377, 416),
            CampoPosicional("UFLogradouroTomador", "", False, "ALFA", 2, 417, 418),
            CampoPosicional("CEPLogradouroTomador", "", False, "ALFA", 8, 419, 426),
            CampoPosicional("PaisLogradouroTomador", "", False, "ALFA", 50, 427, 476),
            CampoPosicional("EmailTomador", "", False, "ALFA", 152, 477, 628),
            CampoPosicional("DiscriminacaoServico", "", False, "ALFA", 1000, 629, 1628),
            CampoPosicional("ChaveAcessoNFSe", "", False, "ALFA", 50, 1629, 1678),
            CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 1679, 1679),
        ]

class NFSeRegistroTipo3(Registro):
    def __init__(self):
        super().__init__()
        self.campos = [
            CampoPosicional("TipoRegistro", "3", True, "NUM", 1, 1, 1),
            CampoPosicional("QuantidadeServico", "", True, "NUM", 6, 2, 7),
            CampoPosicional("DescricaoServico", "", True, "ALFA", 60, 8, 67),
            CampoPosicional("CodigoServico", "", True, "NUM", 9, 68, 76),
            CampoPosicional("ValorUnitarioServico", "", True, "NUM", 15, 77, 91),
            CampoPosicional("AliquotaServico", "", True, "NUM", 4, 92, 95),
            CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 96, 96),
        ]

class NFSeRegistroTipo4(Registro):
    def __init__(self):
        super().__init__()
        self.campos = [
            CampoPosicional("TipoRegistro", "4", True, "NUM", 1, 1, 1),
            CampoPosicional("CodigoOutrosValores", "", True, "ALFA", 2, 2, 3),
            CampoPosicional("Valor", "", True, "NUM", 15, 4, 18),
            CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 19, 19),
        ]

class NFSeRegistroTipo9(Registro):
    def __init__(self):
        super().__init__()
        self.campos = [
            CampoPosicional("TipoRegistro", "9", True, "NUM", 1, 1, 1),
            CampoPosicional("NumeroTotalLinhas", "", True, "NUM", 7, 2, 8),
            CampoPosicional("ValorTotalServicos", "", True, "NUM", 15, 9, 23),
            CampoPosicional("ValorTotalValores", "", True, "NUM", 15, 24, 38),
            CampoPosicional("CaracterFimLinha", "\r", True, "ALFA", 1, 39, 39),
        ]

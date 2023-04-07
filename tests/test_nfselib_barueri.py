
from nfselib.barueri import main


def test_main():
    if not main():
        AssertionError

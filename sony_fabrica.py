from abstract_factory import Fabrica
from sony_televisor import SonyTelevisor
from sony_celular import SonyCelular

class SonyFabrica(Fabrica):
    def create_product_a(self):
        return SonyTelevisor()
    
    def create_product_b(self):
        return SonyCelular()
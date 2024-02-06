class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro = self.session.get("carro")
        if not carro:
            carro = self.session["carro"] = {}
        # else:
        self.carro = carro

    def agregar(self, tienda):
        if (str(tienda.id) not in self.carro.keys()):
            self.carro[tienda.id] = {
                "tienda_id": tienda.id,
                "producto": tienda.producto,
                "precio": str(tienda.precio),
                "cantidad": 1,
                "imagen": tienda.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key == str(tienda.id):
                    value["cantidad"] = value["cantidad"]+1
                    value["precio"] = float(value["precio"])+tienda.precio
                    break
        self.guardar_carro()

    def guardar_carro(self):
        self.session["carro"] = self.carro
        self.session.modified = True

    def eliminar(self, tienda):
        tienda.id = str(tienda.id)
        if tienda.id in self.carro:
            del self.carro[tienda.id]
            self.guardar_carro()

    def restar_producto(self, tienda):
        for key, value in self.carro.items():
            if key == str(tienda.id):
                value["cantidad"] = value["cantidad"]-1
                value["precio"] = float(value["precio"])-tienda.precio
                if value["cantidad"] < 1:
                    self.eliminar(tienda)
                break
        self.guardar_carro()

    def limpiar_carro(self):
        self.session["carro"] = {}
        self.session.modified = True

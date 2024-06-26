class Cart:
    from item_manager import show_items
    from ownable import set_owner

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance >= self.total_amount():
            self.owner.wallet.withdraw(self.total_amount())
        else:
            for item in self.items:
                owner = item.owner
                owner.wallet.deposit(item.price)

        for item in self.items:
            item.set_owner(self.owner)
            
        self.items.clear
            # Eliminar pase al codificar el método check_out.
        # Requisitos
        #: el monto de la compra de todos los artículos en el carrito (Cart#items) se transfiere de la billetera del propietario del carrito a la billetera del propietario del artículo.
        #: la propiedad de todos los artículos del carrito (Cart#items) se transfiere al propietario del carrito.
        # - El contenido del carrito (Cart#items) está vacío.
        # Consejo
        # - Cartera del propietario del carrito ==> self.owner.wallet
        # - Cartera del propietario del artículo ==> item.owner.wallet
        # - El dinero se transferirá ==> Esa cantidad se retirará de la billetera de (?) y se depositará en la billetera de (?).
        # - La propiedad del artículo se transfiere al propietario del carrito ==> Reescribir propietario (item.owner 

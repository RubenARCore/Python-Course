from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        pn = next((x for x in self.products if x.name == product_name), None)
        if pn:
            return pn
        return None

    def remove(self, product_name: str):
        pn = next((x for x in self.products if x.name == product_name), None)
        if pn:
            self.products.remove(pn)

    def __repr__(self):
        result = []
        for pr in self.products:
            result.append(f"{pr.name}: {pr.quantity}")

        return "\n".join(result)





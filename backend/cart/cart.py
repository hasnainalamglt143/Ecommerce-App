from store.models import Product


class Cart():
    def __init__(self,request):
        self.session=request.session
        cart=self.session.get('cart')
        if not cart:
            cart=self.session['cart']={}
        self.cart=cart

    def add(self, product, quantity):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price)  # price stored as string (JSON serializable)
            }
        self.cart[product_id]['quantity'] = int(quantity)

        self.session.modified = True  # ✅ tells Django to save        
    
    def delete(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True  # ✅ tells Django to save


    def __len__(self):
        return len(self.cart)
    
    def get_prods(self):
       product_ids = self.cart.keys()
       products = Product.objects.filter(id__in=product_ids)

       cart_items = []
       for product in products:
           cart_items.append({
            "product": product,
            "quantity": self.cart[str(product.id)]["quantity"],  # session stores quantities as strings
        })

       return cart_items
    
    def get_totals(self):
        total_price = 0
        for item in self.get_prods():
            total_price += item["product"].sale_price * int(item["quantity"]) if item["product"].sale_price else item["product"].price * int(item["quantity"])
        return total_price
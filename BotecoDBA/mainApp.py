from pedido import pedido

if __name__ == "__main__":
    p = pedido()
    
    p.nPedido = 1
    p.produto = ["Cerveja", "Vodka", "Cachaça"]
    p.comidas = ["Batata Frita", "Frango a Passarinho", "Picanha"]
    
    print(p.nPedido)
    print(p.comidas)
    print(p.produto)


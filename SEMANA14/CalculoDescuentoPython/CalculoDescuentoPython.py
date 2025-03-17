# Función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el descuento aplicado a un monto total de compra.
    
    :param monto_total: Monto total de la compra (float o int).
    :param porcentaje_descuento: Porcentaje de descuento (float o int). Por defecto es 10%.
    :return: Monto del descuento calculado (float).
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


# Programa principal
if __name__ == "__main__":
    # Llamada 1: Usando el porcentaje de descuento predeterminado (10%)
    monto_compra_1 = 5000  # Monto total de la compra
    descuento_1 = calcular_descuento(monto_compra_1)
    monto_final_1 = monto_compra_1 - descuento_1

    print(f"Compra 1: Monto total = ${monto_compra_1}")
    print(f"Descuento aplicado = ${descuento_1}")
    print(f"Monto final a pagar = ${monto_final_1}\n")

    # Llamada 2: Especificando un porcentaje de descuento personalizado (20%)
    monto_compra_2 = 7500  # Monto total de la compra
    porcentaje_descuento_2 = 20  # Porcentaje de descuento personalizado
    descuento_2 = calcular_descuento(monto_compra_2, porcentaje_descuento_2)
    monto_final_2 = monto_compra_2 - descuento_2

    print(f"Compra 2: Monto total = ${monto_compra_2}")
    print(f"Descuento aplicado = ${descuento_2}")
    print(f"Monto final a pagar = ${monto_final_2}")
    
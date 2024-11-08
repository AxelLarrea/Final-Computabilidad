def porcentaje_error(diferencia, suma_total):
    
    suma_ideal = (suma_total) / 2
    
    # Calcular el porcentaje de error
    porcentaje = (diferencia / suma_ideal) * 100
    
    print(f"El porcentaje de error es: {porcentaje:.2f}%")
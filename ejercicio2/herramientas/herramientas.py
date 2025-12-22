def interseccion_intervalos(inicio1, fin1, inicio2, fin2):
    if inicio2 <= inicio1 <= fin2:
        return True
    if inicio2 <= fin1 <= fin2:
        return True
    if inicio1 <= inicio2 and fin2 <= fin1:
        return True
    return False
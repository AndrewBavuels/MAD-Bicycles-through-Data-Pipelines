import argparse

def parsing():

    """Arguments that will be read within main.py, which give the user options of accessing 
    information about the closest Bicimad and Bicipark stations when searching for an specific
     place of interest.

    Returns:
        args.Namespace: An object containing the parsed arguments. 
        The attributes of this object represent options entered by the user.
    """
    # (analizador), que es donde se van a agregar los argumentos que se vayan definiendo.
    parser = argparse.ArgumentParser(description='Elige Bicimad o Bicipark y encuentra la estación más cercana a tu destino')
    # (admite varios parámetros) que definen las características del argumento que crea
    parser.add_argument('--bicimad', action='store_true', help='Elegir Bicimad')
    parser.add_argument('--bicipark', action='store_true', help='Elegir Bicipark')
    parser.add_argument('--todas', action='store_true', help='Obtener información de todos los sitios de interés')
    parser.add_argument('--lugar', type=str, help='Obtener información de la estación más cercana al sitio de interés')
        
    # analiza y procesa todos los argumentos creados
    args = parser.parse_args()
    return args

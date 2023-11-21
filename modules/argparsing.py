import argparse

def parsing():
    parser = argparse.ArgumentParser(description='Elige Bicimad o Bicipark y encuentra la estación más cercana a tu destino')
    parser.add_argument('--bicimad', action='store_true', help='Elegir Bicimad')
    parser.add_argument('--bicipark', action='store_true', help='Elegir Bicipark')
    parser.add_argument('--todas', action='store_true', help='Obtener información de todos los sitios de interés')
    parser.add_argument('--lugar', type=str, help='Obtener información de la estación más cercana al sitio de interés')

    
    
    args = parser.parse_args()
    return args

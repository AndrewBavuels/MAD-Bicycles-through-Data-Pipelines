from argparsing import parsing
from fuzzywuzzy import process
import pandas as pd

"""The main script that reads a specific dataframe if a specific args exists. 
If the parsing exists an all field, it returns bicistation_df. 
Or else, it returns place_specificic and exports it in the corresponding path. 
Else, it returns none.

Returns:
    Dataframe: Information on places of interest related to the nearest station:
     
      1. Bicimad with the number of bikes available
      2. Bicipark with the free parking spots available
    
"""

def the_fuzzer(user_input,sitios_interes,path_,bicistation_df):

    aprox = process.extract(user_input, sitios_interes, limit=5)
    place_specific = bicistation_df.loc[bicistation_df['Place of interest'].isin([i[0]for i in aprox]), :]
    print(place_specific)
    place_specific.to_csv(f'../modules/{path_}_to_place.csv', index=False, encoding='utf-8')

def main():

    args = parsing()    

    if args.bicimad:

        path_ = "bicimad"
        bicistation_df = pd.read_csv(f'../modules/{path_}_project_df_v4.csv')

        if args.todas:
            print(bicistation_df)
            return bicistation_df
        
        elif args.lugar:
            # FuzzyWuzzy
            user_input = args.lugar
            sitios_interes = bicistation_df['Place of interest'].tolist()
            the_fuzzer(user_input,sitios_interes,path_,bicistation_df)

        else:
            print("No se encontró la información pedida")
            return None
        
    elif args.bicipark:

        path_ = "biciparks"
        bicistation_df = pd.read_csv(f'../modules/{path_}_project_df_v4.csv')

        if args.todas:
            print(bicistation_df)
            return bicistation_df
        
        elif args.lugar:
            # FuzzyWuzzy
            user_input = args.lugar
            sitios_interes = bicistation_df['Place of interest'].tolist()
            the_fuzzer(user_input,sitios_interes,path_,bicistation_df)

        else:
            print("No se encontró la información pedida")
            return None


if __name__ == '__main__':
    main()
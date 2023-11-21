from argparsing import parsing
from fuzzywuzzy import process
import pandas as pd

def the_fuzzer(user_input,sitios_interes,path_,bicistation_df):

    aprox = process.extractOne(user_input, sitios_interes)
    place_specific = bicistation_df.loc[bicistation_df['Place of interest'] == aprox[0], :]
    print(place_specific)
    place_specific.to_csv(f'../modules/{path_}_to_place.csv', index=False, encoding='utf-8')

def main():

    args = parsing()    

    if args.bicimad:

        path_ = "bicimad"
        bicistation_df = pd.read_csv(f'../modules/{path_}_project_df_v3.csv')

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
        bicistation_df = pd.read_csv(f'../modules/{path_}_project_df_v3.csv')

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
# **Project Module 1 - MAD Bicycles through Data Pipelines🚵🟰🚴**

The main reason why you should review this project is to get an approach about Data Pipelines. **Furthermore,** to show the potential of big data processing prior to AI and Machine Learning development.

**What is Data Pipelines about?** In a nutshell, is getting data from one or more sources, followed by organizing and transforming them. **The purpose is** to drive the analysis and report the findings that are relevant for decision-making in business.


## 1. Project description 👇
> Project Module 1 - Part time Sept 2023 - [Ironhack Madrid - Data Analytics Bootcamp](https://www.ironhack.com/es-en/data-analytics)

To put into practice what we have learned during Module 1, I was given **two datasources** related to geolocation coordinates as follows: 

- `CSV Files:`  All the BiciMAD and Bicipark stations with their location (latitude / longitude) 🌐
- Using an `API REST` from [Madrid City Council open data portal ](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/) 💻

With the previous,  **the main challenge** was creating a Python App that allows  potential users to find the nearest BiciMAD station to a set of places of interest based on the coordinates 🧭 within the data sets.


> **Bicimad Station near Reina Sofia Museum**

![Image](<https://www.bicimad.com/sites/default/files/styles/news_teaser/public/2023-07/Estaci%C3%B3n%20bicimad%20Museo%20Reina%20Sof%C3%ADa.jpg.webp?itok=AhKkKtGe alt="Image" width="200" height="100">)

## **2. Minimal Functional App ⚙️**

The Data Pipeline implemented allows the user from the Terminal with command-lines, to search for and **find an specific place** of interest to visit. Or, to **find a set of places** by entering a keyword related to. Both are exported into a csv file that, besides the placse of interest, they contain as well:

- Bicimad or Bicipark stations near to the place of interest (including their addresses)
- The distance in mts from Bicimad or Bicipark station per place of interest
- The availability of bikes in each Bicimad station
- Free spots in each Bicipark Station

> This beta version tested via command-line, could gather from potential user feedback on finding the nearest BiciMAD station to **improve the code and enhance the user experience.**

#### How does it work?
For example: the main script is executed in the terminal to get information about Museums in Madrid. If you want to try it , just enter via command-line:
```
python main.py --bicimad --lugar "mueso"
```
As you can see, the word museo was misspelled (museo). Despite the typo error, you will get related places from the keyword:

| Place of interest  | BiciMAD address | Bikes available  |
| ------------ | ------------ | ------------ |
| Museo ABC  | Calle Conde Duque nº 22  | 1  |
|  Museo Arqueológico Nacional | Calle Claudio Coello nº 109  |  2 |
|  Museo Casa de la Moneda | Calle Jorge Juan nº 131  | 0  |
|  Museo Lázaro Galdiano | Paseo de la Castellana nº 43  | 4  |
> The previous output is exported in a csv file.

## **3. Technology stack 💻**

#### Programming language:
- [Python](https://docs.python.org/3/)

#### Libraries:

- [Pandas](https://pandas.pydata.org/docs/reference/frame.html): data manipulation and analysis.
- [Requests](https://requests.readthedocs.io/en/latest/): making HTTP requests.
- [Geopandas](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries): geospatial data analysis.
- [Shapely](https://geopandas.org/en/stable/docs/reference/api/geopandas.GeoSeries.html#geopandas.GeoSeries): geometric operations (Geopandas dependance)
- [Argparse](https://docs.python.org/3/library/argparse.html):   command-line parsing.
- [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/):  string comparison and matching

#### Development tools: 
- [VSC](https://code.visualstudio.com/)
- Terminal

#### Distribution platform
- [Anaconda](https://www.anaconda.com/)

#### Computing environment
- [Jupyter Notebooks](https://jupyter.org/)

## **4. Folder structure 📁**
```
└── project
    ├── _wip_
    ├── .gitignore
    ├── notebooks
    │   ├── 1_Primer_dataset_v2.ipynb
    │   ├── 2_Segundo_dataset_v2.ipynb
    │   ├── 3_API_dataset_v2.ipynb
    │   ├── 4_Funciones.ipynb
    │   └── 5_Bicis_por_estacion.ipynb 
    ├── modules
    │   ├── main.py
    │   └── argparsing.py
    ├── data
    │   ├── raw
    │   │   ├── bicimad_stations.csv
    │   │   └── biciparks_stations.csv
    │   ├── processed
    │   │   ├── bicimad_stations.csv
    │   │   ├── biciparks_df.csv
    │   │   ├── inst_no_munic_df.csv
    │   │   ├── 0_bicimad_dispo.csv
    │   │   └── 0_bicipark_dispo.csv
    │   └── results
    │       ├── bicimad_vfinal_df.csv
    │       └── biciparks_vfinal_df.csv
    └── README.md
```
###  **Contact info📧**
For further information, reach me at andrew.bavuels@gmail.com

---

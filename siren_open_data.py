from sqlalchemy import create_engine
from sqlalchemy import create_engine
import pandas as pd
import time

engine = create_engine("mysql+pymysql://misterheinz:simplon@localhost/siren_open_data")

def importcsv(link, table, date):
    print("Lecture des données")
    start_time = time.time()
    csize = 2000
    df = pd.read_csv(link, compression = 'zip', chunksize = csize, parse_dates = date)
    print("Données lu")
    i = csize
    for chunk in df:
        chunk.to_sql(table, con = engine, if_exists='append', index = False)
        i += csize
        print(i)
    return print("Temps d execution : %s secondes ---" % (time.time() - start_time))


importcsv('http://files.data.gouv.fr/insee-sirene/StockEtablissement_utf8.zip','etab', ['anneeEffectifsEtablissement','dateCreationEtablissement', 'dateDernierTraitementEtablissement', 'dateDebut'])
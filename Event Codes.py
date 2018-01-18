import pandas as pd
from os import walk
from os.path import join

def fileList(directory):
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)
        break
    return f

directory = r'E:\Users\John\Documents\SportVu\Play By Play Data'

pbplist = fileList(directory)

pbp_df = pd.DataFrame()
for f in pbplist:
    df = pd.read_csv(join(directory, f))
    pbp_df = pbp_df.append(df, ignore_index=True)
    
events = pbp_df[['EVENTMSGTYPE', 'EVENTMSGACTIONTYPE', 'HOMEDESCRIPTION', 'VISITORDESCRIPTION']]
events.drop_duplicates(['EVENTMSGTYPE', 'EVENTMSGACTIONTYPE'], inplace = True)

outpath = r'E:\Users\John\Documents\SportVu'
events.to_csv(join(outpath, 'Event_Codes2.csv'), index=False)
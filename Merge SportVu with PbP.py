import pandas as pd
from os import walk
from os.path import join

pbp_dir = r'E:\Users\John\Documents\SportVu\Play By Play Data'
sv_dir = r'E:\Users\John\Documents\SportVu\SportVu CSVs'

# Get a list of all the files in the top level of a directory
def fileList(directory):
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)
        break
    
    return f

def mergeSVtoPBP(filename):
    sv = pd.read_csv(join(sv_dir, filename))
    pbp = pd.read_csv(join(pbp_dir, filename))
    pbp = pbp[['EVENTNUM', 'GAME_ID', 'EVENTMSGTYPE_DESCRIPTION', 'EVENTMSGACTIONTYPE_DESCRIPTION']]
    df = pd.merge(sv, pbp, how='left', left_on = 'event.id', right_on = 'EVENTNUM')
    
    return df
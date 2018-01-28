import pandas as pd
from os import walk
from os.path import join

directory = r'E:\Users\John\Documents\SportVu\Play By Play Data'

# Get a list of all the files in the top level of a directory
def fileList(directory):
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)
        break
    
    return f

# Add EVENTMSGTYPE_DESCRIPTION and EVENTMSGACTIONTYPE_DESCRIPTION columns to all CSV files in directory
def addEventDescriptions(directory):
    pbplist = fileList(directory)
    
    for f in pbplist:
        if f[-3:].upper() == 'CSV':
            df = pd.read_csv(join(directory, f))
            eventdf = pd.read_csv(r'E:\Users\John\Documents\SportVu\Event_Codes.csv')
            newdf = pd.merge(df, eventdf, how='left', on = ['EVENTMSGTYPE', 'EVENTMSGACTIONTYPE'])
            newdf.to_csv(join(directory, f), index = False)

# Compile all CSV files from a directory into a single dataframe
def dfFromDirectory(directory):
    pbplist = fileList(directory)
    pbp_df = pd.DataFrame()
    for f in pbplist:
        if f[-3:].upper() == 'CSV':
            df = pd.read_csv(join(directory, f))
            pbp_df = pbp_df.append(df, ignore_index=True)
        
    return pbp_df

# Filter the Play By Play dataframe by event. Context = True will include the 2 plays before and after the event
def filterByEvent(pbp_df, e1, e2 = -1, context = False):
    if e2 > -1:
        idx_list = pbp_df.index[(pbp_df['EVENTMSGTYPE'] == e1) & (pbp_df['EVENTMSGACTIONTYPE'] == e2)].tolist()
    else:
        idx_list = pbp_df.index[pbp_df['EVENTMSGTYPE'] == e1].tolist()
    if context:
        filter_idx = []
        for idx in idx_list:
            filter_idx.extend([idx-2, idx-1, idx])
    else:
        filter_idx = idx_list
    play_df = pbp_df.iloc[filter_idx]
    
    return play_df
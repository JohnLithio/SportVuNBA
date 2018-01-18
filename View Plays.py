import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from os import walk
from os.path import join

sns.set_color_codes()
sns.set_style("white")

directory = r'E:\Users\John\Documents\SportVu'
pbp_dir = r'E:\Users\John\Documents\SportVu\Play By Play Data'
sv_dir = r'E:\Users\John\Documents\SportVu\SportVu CSVs'

# Get a list of all the files in the top level of a directory
def fileList(directory):
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)
        break
    
    return f

# Filter game log by event type, player name, and event number
# Results in the path of 1 player for 1 play
def filterPlayer(df, eventmsgtype='', lastname='', eventnum=''):
    if eventmsgtype != '':
        df = df[df['EVENTMSGTYPE_DESCRIPTION'] == eventmsgtype]
    if lastname != '':
        df = df[df['lastname'] == lastname]
    if eventnum != '':
        df = df[df['event.id'] == eventnum]
        
    return df

# Merge the SportVu data with the Play by Play data
def mergeSVtoPBP(filename):
    sv = pd.read_csv(join(sv_dir, filename))
    pbp = pd.read_csv(join(pbp_dir, filename))
    pbp = pbp[['EVENTNUM', 'GAME_ID', 'EVENTMSGTYPE_DESCRIPTION', 'EVENTMSGACTIONTYPE_DESCRIPTION']]
    df = pd.merge(sv, pbp, how='left', left_on = 'event.id', right_on = 'EVENTNUM')
    
    return df
    
# Plot a single player's path over the course of a possession
def plotPlayer(df):
    court = plt.imread(join(directory, 'fullcourt.png'))

    plt.figure(figsize=(15, 11.5))
    plt.scatter(df.x_loc, df.y_loc, c=df.game_clock,
                cmap=plt.cm.Blues, s=100, zorder=1)
    
    cbar = plt.colorbar(orientation="horizontal")
    cbar.ax.invert_xaxis()
    
    plt.imshow(court, zorder=0, extent=[0,94,50,0])
    
    plt.xlim(0,101)
    
    plt.show()

pbplist = fileList(pbp_dir)
df = mergeSVtoPBP(pbplist[0])
ball = filterPlayer(df, eventmsgtype = 'Made Field Goal',
                     lastname = 'ball',
                     eventnum = 46)

plotPlayer(ball)
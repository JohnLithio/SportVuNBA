import pyunpack
import requests
import pandas as pd
from json import loads
from os import walk
from os.path import join

headers = requests.utils.default_headers()
headers.update({'User-Agent':'New User Agent',})

def unzipSportVu(inpath):
    pyunpack.Archive(inpath).extractall(r'E:\Users\John\Documents\SportVu\SportVu JSONs\\')
    
def fileList(directory):
    f = []
    for (dirpath, dirnames, filenames) in walk(directory):
        f.extend(filenames)
        break
    return f

def get_pbp(gameid):
    url = "http://stats.nba.com/stats/playbyplayv2?EndPeriod=10&EndRange=55800&GameID=" +\
    gameid +\
    "&RangeType=2&Season=2015-16&SeasonType=Regular+Season&StartPeriod=1&StartRange=0"
    page = requests.get(url, headers = headers)
    
    dic = loads(page.text)
    pbp_headers = dic['resultSets'][0]['headers']
    pbp_data = dic['resultSets'][0]['rowSet']
    
    pbp_df = pd.DataFrame(pbp_data, columns=pbp_headers)
    
    filepath = r'E:\Users\John\Documents\SportVu\Play By Play Data\\' + gameid + '.csv'
    
    pbp_df.to_csv(filepath, index = False)
    
#directory = r'E:\Users\John\Documents\SportVu\SportVu JSONs\7Zip Files'
#
#filelist = fileList(directory)
#
#for f in filelist:
#    inpath = join(directory, f)
#    unzipSportVu(inpath)

sv_dir = r'E:\Users\John\Documents\SportVu\SportVu JSONs'
    
#sv_list = fileList(sv_dir)
#sv_list = [f[:-5] for f in sv_list]
#
#for f in sv_list:
#    get_pbp(f)

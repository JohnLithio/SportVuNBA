source("E:/Users/John/Documents/SportVu/Rajiv Shah/_functions.R")

setwd("E:/Users/John/Documents/SportVu")

file.names <- dir(paste(getwd(), "/SportVu JSONs", sep=""), pattern = ".json")

file.names <- c('0021500660.json', '0021500661.json', '0021500662.json', '0021500663.json')

for (i in 1:length(file.names)){
  inpath <- paste("SportVu JSONs/", file.names[i], sep="")
  all.movements <- sportvu_convert_json(inpath)
  
  outpath <- paste("SportVu CSVs/", gsub("json", "csv", file.names[i]), sep="")
  write.csv(all.movements, outpath)
}
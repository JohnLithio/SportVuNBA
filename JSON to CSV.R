source("C:/Users/John/Downloads/NBA_SportVu-master/NBA_SportVu-master/_functions.R")

setwd("E:/Users/John/Documents/SportVu")

file.names <- dir(paste(getwd(), "/SportVu JSONs", sep=""), pattern = ".json")
for (i in 1:length(file.names)){
  inpath <- paste("SportVu JSONs/", file.names[i], sep="")
  all.movements <- sportvu_convert_json(inpath)
  
  outpath <- paste("SportVu CSVs/", gsub("json", "csv", file.names[i]), sep="")
  write.csv(all.movements, outpath)
}
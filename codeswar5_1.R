# https://www.codewars.com/kata/56baeae7022c16dd7400086e/train/r
# Phone Directory
#Could you help John with a program that, given the lines of his phone book and a phone number num returns a string for this number : "Phone => num, Name => name, Address => adress"

# Clean environment ------------------------------------

rm(list = ls())
gc()

# Packages ---------------------------------------------

library(dplyr) # dataframes
library(tidyverse)  #split
library(stringr)  #split

# Examples ---------------------------------------------

a = "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n"
b = " 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010!\n"
c = "<Anastasia> +48-421-674-8974 Via Quirinal Roma\n"

dr <- "/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010
 +1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n :+1-321-512-2222 <Paul Dive> Sequoia Alley PQ-67209
 +1-741-984-3090 <Peter Reedgrave> _Chicago\n :+1-921-333-2222 <Anna Stevens> Haramburu_Street AA-67209
 +1-111-544-8973 <Peter Pan> LA\n +1-921-512-2222 <Wilfrid Stevens> Wild Street AA-67209
 <Peter Gone> LA ?+1-121-544-8974 \n <R Steell> Quora Street AB-47209 +1-481-512-2222
 <Arthur Clarke> San Antonio $+1-121-504-8974 TT-45120\n <Ray Chandler> Teliman Pk. !+1-681-512-2222! AB-47209,
 <Sophia Loren> +1-421-674-8974 Bern TP-46017\n <Peter O'Brien> High Street +1-908-512-2222; CC-47209
 <Anastasia> +48-421-674-8974 Via Quirinal Roma\n <P Salinger> Main Street, +1-098-512-2222, Denver
 <C Powel> *+19-421-674-8974 Chateau des Fosses Strasbourg F-68000\n <Bernard Deltheil> +1-498-512-2222; Mount Av.  Eldorado
 +1-099-500-8000 <Peter Crush> Labrador Bd.\n +1-931-512-4855 <William Saurin> Bison Street CQ-23071
 <P Salinge> Main Street, +1-098-512-2222, Denve
 /+5-541-754-3010 156 Alphandria_Street. <Jr Part>\n 1333, Green, Road <F Fulgur> NW-46423 ;+6-541-914-3010!
 +5-541-984-3012 <Peter Reeves> /PO Box 5300; Albertville, SC-28573\n :+5-321-512-2222 <Paulo Divino> Boulder Alley ZQ-87209
 +3-741-984-3090 <F Flanaghan> _Chicago Av.\n :+3-921-333-2222 <Roland Scorsini> Bellevue_Street DA-67209
 +8-111-544-8973 <Laurence Pantow> SA\n +8-921-512-2222 <Raymond Stevenson> Joly Street EE-67209
 <John Freeland> Mantow ?+2-121-544-8974 \n <Robert Mitch> Eleonore Street QB-87209 +2-481-512-2222?
 <Arthur Paternos> San Antonio $+7-121-504-8974 TT-45121\n <Ray Charles> Stevenson Pk. !+7-681-512-2222! CB-47209,
 <JP Gorce> +9-421-674-8974 New-Bern TP-16017\n <P McDon> Revolution Street +2-908-512-2222; PP-47209
 <Elizabeth Corber> +58-421-674-8974 Via Papa Roma\n <C Saborn> Main Street, +15-098-512-2222, Boulder
 <Colin Marshall> *+9-421-674-8974 Edinburgh UK\n <Bernard Povit> +3-498-512-2222; Hill Av.  Cameron
 +12-099-500-8000 <Pete Highman> Ontario Bd.\n +8-931-512-4855 <W Mount> Oxford Street CQ-23071
 <Donald Drinkaw> Moon Street, +3-098-512-2222, Peterville"


# Functions  ---------------------------------------------

left = function(x, sep) {
  substring(x, 1, regexpr(sep, x) - 1)
}
right = function(x, sep) {
  substring(x, regexpr(sep, x) + 1, nchar(x))
}


phone <- function(strng, num) {

  dr1 <- strsplit(strng, '\n')
  result <- grep(num, dr1[[1]])
  
  if(length(result) <1){
    return(paste0("Error => Not found: ",num))}
  if(length(result) >1){
    return(paste0("Error => Too many people: ",num))}
  if(length(result) ==1){
    contact <- dr1[[1]][result]
    name <- left(right(contact,"<"),">")
    locate_plus <-
      lapply(strsplit(contact, '+'), function(x)
        which(x == '+'))[[1]]
    number <- str_sub(contact, locate_plus, locate_plus + 15)
    adress <- gsub(name, "",gsub(number, "", contact))
    # problem with apostrophe and + sign
    # adress <- gsub("[^[:alnum:]-\'.]", " ", adress)
    adress <- gsub("[<>*/$?;:,/]", "", adress)
    adress <- gsub("\\+", "", adress)
    adress <- gsub("_", " ", adress)
    adress <- gsub("  ", " ", adress)
    
    adress <- trimws(adress)
    
    string_out = paste0(
      "Phone => ",
      num,
      ", Name => ",
      name,
      ", Address => ",
      adress
    )  
    return(string_out)
  }
}

testing <- function(s, num, expected) {
  actual <- phone(s, num)
  cat("actual ", actual, "\n")
  cat("expected ", expected, "\n")
}

# Main ---------------------------------------------

phone(dr,"48-421-674-8974")

phone(dr,"1-921-333-2222")
num="48-421-674-8974"


testing(dr, "48-421-674-8974", "Phone => 48-421-674-8974, Name => Anastasia, Address => Via Quirinal Roma")
testing(dr, "19-421-674-8974", "Phone => 19-421-674-8974, Name => C Powel, Address => Chateau des Fosses Strasbourg F-68000")
testing(dr, "1-481-512-2222", "Phone => 1-481-512-2222, Name => R Steell, Address => Quora Street AB-47209")
testing(dr, "1-098-512-2222", "Error => Too many people: 1-098-512-2222")
testing(dr, "5-555-555-5555", "Error => Not found: 5-555-555-5555")




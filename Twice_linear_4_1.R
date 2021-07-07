# https://www.codewars.com/kata/5672682212c8ecf83e000050
# Twice linear

# Clean environment ------------------------------------

rm(list = ls())
gc()

# Packages ---------------------------------------------
library(dplyr) # dataframes
library(tidyverse)  #map

# Main ---------------------------------------------

dblLinear = function(number) {
  u <- c(1)
  while(length(u)<number){
    u <-  sort(unique(c(u, unlist(u %>% map(function(x) c(2 * x + 1, 3 * x + 1))))), decreasing=F)
  }
  return(u[number+1])
}

dblLinear = function(number) {
  u <- c(1)
  while(length(u)<number){
    a <- unlist(u %>% map(function(x) c(2 * x + 1, 3 * x + 1)))
    u <-  sort(unique(c(u,a)), decreasing=F)
  }
  return(u[number+1])
}

  
# Testing  ---------------------------------------------


testing <- function(n, expected) {
  actual <- dblLinear(n)
  cat(actual, expected)
}

testing(10, 22)
testing(20, 57)

# 1/1 mismatches
# [1] 189 - 175 == 14 # 175  183  187  189
# u[51] = 175,  u[54] = 189

dblLinear(1740)
dblLinear(189)
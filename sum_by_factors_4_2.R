# https://www.codewars.com/kata/54d496788776e49e6b00052f/train/r
# Sum by Factors

# Clean environment ------------------------------------

rm(list = ls())
gc()

# Packages ---------------------------------------------

library(dplyr) # dataframes
library(tidyverse)  #map
# library(hash)

# Functions ---------------------------------------------

is_prime <- function(num) {num ==2 | !any(num %% 2:(num - 1) == 0)} 

get_primes <- function(num) {
  divs <- which(num %% 2:num  == 0) + 1
  return(divs[unlist(map(divs,is_prime))])} 


sumOfDivided <- function (lst) {
  if(length(lst)==0){ return(list()) } else {
    lst <- unlist(lst)
    vx = vector(mode = "list", length(lst))
    all_primes <- c()
    
    for (elem in 1:length(lst) ){
      primes <-  get_primes(lst[elem])
      vx[elem] <- list(primes)
      all_primes <- sort(unique(c(all_primes,primes)))}
    
    p <- list()
    for (elem in all_primes) {
      idx_list <- c()
      sublist <- grep(elem,vx) # elements containing 7, even 107...
      for (idx in sublist) {
        if ( any(vx[[idx]] == elem)){ # if truly equal
          idx_list <- c(idx_list, idx )}}
      p[[length(p)+1]] <-   c( elem, sum( lst[idx_list] ) ) }
    cat(lst)
    cat ("\n")
    cat(unlist(p))
    return(p)
  } 
}

testing <- function(ls, expected) {
  actual <- sumOfDivided(ls)
  if(identical(actual, expected)==TRUE){return(TRUE)
  } else {
    return(actual)
  }
}

test_that("tests", {
  testing(c(12, 15), list(c(2, 12), c(3, 27), c(5, 15)))
  testing(c(), list()) # not working
  testing(c(17, 34, 51, 68, 102), list(c(2, 204), c(3, 153), c(17, 272))) # 17 255
  })


ls = c(100,100,107,110,116,118,123,126,158,204)
ls= c(107, 158, 204, 100, 118, 123, 126, 110, 116, 100 )
ls = c(15, 30, -45)


# different ways to find primes
divisors_of <- function(num) {
  divs <- which(num %% 2:num  == 0) + 1
  # or which((pn)/2:(pn-1)==(pn)%/%2:(pn-1)) +1
  if (length(divs) == 0) {
    return(num)
  } else {
    return(divs)
  }
}

get_primes <- function(num) {
  divs <- divisors_of (num)
  return(divs[unlist(map(divs,is_prime))])
}

# mutate and summarize


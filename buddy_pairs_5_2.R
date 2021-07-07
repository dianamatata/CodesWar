# https://www.codewars.com/kata/59ccf051dcc4050f7800008f
# Buddy Pairs
# Level 5

# Clean environment ------------------------------------

rm(list = ls())
gc()

# Packages ---------------------------------------------
library(dplyr) # dataframes
library(tidyverse)  # split
library(stringr)  # split

# Functions ---------------------------------------------


divisors = function(number, lim=NULL) {
  list_d <- which(!n %% (1:(n/2)))
    return(sum(list_d))}


# solution
buddy <- function(start, limit) {
  for (n in start:limit) {
    m <- divisors(n) - 1
    if (n == s(m) - 1 && m > n) return(sprintf('(%d %d)', n, m))}
  'Nothing'}


# Test ---------------------------------------------
# Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) 
# of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive)
# m can be greater than limit and has to be greater than n


testing <- function(st, lim, expect) {
  actual <- buddy(st, lim)
  cat("start ", st, "limit ", lim, "\n")
  cat("actual" , actual, "\n")
  cat("expect" , expect, "\n\n")
  expect_equal(actual, expect)
}

test_that("decomp", {
  testing(654, 3567, "(1050 1925)")
  testing(23, 4669, "(48 75)")
  testing(6379, 8275, "Nothing")
  
})

# Debugging ---------------------------------------------


buddy1_number = 48
buddy2_number = 75
divisors(48)

buddy(48, 75)
buddy(654, 3567)
buddy(23, 4669)
buddy(6379, 8275)




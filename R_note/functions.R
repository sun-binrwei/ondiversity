#  calculate richness 
richness <- function(A){
    return(length(unique(A[!is.na(A)])))
}

# calculate Simpson's evenness (IER: Inter-kind Encounter Rate)
simpsonIER <- function(A){
    TA <- table(A[!is.na(A)])
    N <- sum(TA)          
    IER <-(1 - sum((TA / N) ^ 2)) * N / (N - 1)
    return(IER)
}  

# Mean distance between groupmates
meanDistWithin <- function(A){}
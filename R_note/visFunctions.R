tabDiversity <- function(data, groupID, nick = names(data)){
    # number of groups
    ng <- unique(groupID) %>% length
    # number of variables (columns)
    nv <- dim(data)[2]
    ## data sheet
    df <- data.frame(Group = rep(NA, (ng+1) * nv), 
                     Scale = rep(NA, (ng+1) * nv),
                     Type = rep(NA, (ng+1) * nv),
                     Richness = rep(NA, (ng+1) * nv),
                     IER = rep(NA, (ng+1) * nv)) 
    ## row counter
    r <-1
    for (g in 1:ng){
        subdata <- data[groupID == g,]
        for (v in 1: nv){
            df$Group[r] <- g
            df$Scale[r] <- 'Group'
            df$Type[r] <- nick[v]
            df$Richness[r] <- richness(subdata[,v])
            df$IER[r] <- simpsonIER(subdata[,v])
            r <- r + 1
        }
    }

    for (v in 1: nv){
        df$Group[r] <- 'ALL'
        df$Scale[r] <- 'Section'
        df$Type[r] <- nick[v]
        df$Richness[r] <- richness(data[,v])
        df$IER[r] <- simpsonIER(data[,v])
        r <- r + 1
    }
    
    df2 <- melt(df, measure.vars = c('Richness', 'IER'))
    
    return(df2)
} # end of function tabDiversity



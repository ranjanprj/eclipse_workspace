import logging
import math
logging.basicConfig(filename='.//stats.log',level=logging.DEBUG)

def inter_quartile(l):
    logging.info("INTER QUARTILE LIST " + str(l))
    sorted_l = sorted(l)
    len_l = len(sorted_l)
    logging.info("SORTED LIST " + str(sorted_l))
    if len_l % 2 is 0:
        split_l = [ sorted_l[:len_l//2], sorted_l[len_l//2:] ]
        logging.info("INTER QUARTILE SPLIT LIST " + str(split_l))
        Q1 = get_median(split_l[0])
        Q3 = get_median(split_l[1])
        IQR = Q3 - Q1
        return IQR
    else:
        split_l = [ sorted_l[len_l//2-1:], sorted_l[:len(sorted_l)//2] ]
        Q1 = get_median(split_l[0])
        Q3 = get_median(split_l[1])
        IQR = Q3 - Q1
        return IQR
    
def get_median(l): 
    if l is None:
        return 0
    sorted_l = sorted(l)
    
    if len(sorted_l) % 2 is not 0:
        return sorted_l[len(sorted_l)//2]
    else:
        first_middle = sorted_l[len(sorted_l)//2-1] 
        second_middle = sorted_l[len(sorted_l)//2] 
        return get_mean( [first_middle, second_middle] )
        
def get_mean(l):
    return sum(l)/len(l);
    
def get_std_dev(l):
    # std_dev = sqrt( sum ( x -m )^2 / n -1 )
    mean = get_mean(l)
    logging.info("MEAN " + str(mean))
    variance = sum ( [math.pow( (x - mean),2 ) for x in l] ) / len(l)
    logging.info("VARIANCE " + str(variance))
    std_dev = math.sqrt(variance)
    return std_dev

def get_outlier_using_IQR(l):
    pass
    
    
    
    
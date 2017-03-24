import test
from stats import inter_quartile, get_median, get_std_dev

if __name__ == "__main__":
    l = [5, 7, 2, 1, 3, 4, 8, 8, 6, 6]
    print(inter_quartile(l))
    print(get_std_dev([1, 10, 6, 9, 2, 5, 6, 6, 5, 10]))

    
    
  
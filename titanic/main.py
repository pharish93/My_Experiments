import pandas as pd

def main():
    print "Hello"

    k = pd.read_csv("train.csv")
    print k.shape
    print k.columns.values
    print k.dtypes
    print k.head()

    print k.isnull()

if __name__ == '__main__':
    main()

import argparse

def exchange(array,position1,position2):
    temp=array[position1]
    array[position1]=array[position2]
    array[position2]=temp
    return array


def sort(sortdata1):
    for i in range(0, len(sortdata1)):
        for j in range(1, len(sortdata1) - i):
            if sortdata1[j - 1] > sortdata1[j]:
                sortdata1=exchange(sortdata1, j - 1, j)
    print sortdata1


def sortfile(filename):
    fo=open(filename,"r+")
    fdata=fo.read()
    sortdata=fdata.split()
    sort(sortdata)

if __name__ == '__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--ifile", help="Specify the name of input file ")
    parser.add_argument("-o","--ofile", help="specify the name of output file ")

    args=parser.parse_args()
    print args.ifile
    print args.ofile


import os 
import argparse
import string
def main():
    parser = argparse.ArgumentParser(description="Please input a text file")
    parser.add_argument("text-file",help="Please input a text file..")
    args = vars(parser.parse_args())
    if(args['text-file']==None or args['text-file'] not in os.listdir() or not(args['text-file'].endswith(".txt"))):
        print("""Please input an appropriate textfile 
                (with .txt ending) in the current working directory""")
        return
    else:
        fname = args['text-file']
        with open(fname,"r") as ffname:
            wordList = ffname.read().lower().split()
            wordList = ["".join([ch for ch in word if ch not in string.punctuation]) for word in wordList]
        cumWordList = []
        if(len(wordList)<3): cumWordList.append(wordList)
        else:
            for i in range(0,len(wordList)-2):
                cumWordList.append([wordList[i],wordList[i+1],wordList[i+2]])
        nfname = fname[:fname.index(".txt")]+"-trips.txt"
        with open(nfname,"w") as fnfname:
            for wordTrip in cumWordList:
                fnfname.write("{} {} {}\n".format(wordTrip[0],wordTrip[1],wordTrip[2]))
            

main()


import getnum
import argparse


arg=argparse.ArgumentParser()
arg.add_argument("-i", "--input",type=str,default="test1.png",help="Enter the input image file")
args=vars(arg.parse_args())

inp_imagefile=args["input"]

if __name__=="__main__":

    getnum.get_num(inp_imagefile)
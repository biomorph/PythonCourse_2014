#!/usr/bin/env python
input1 = raw_input("Enter input1?\n")
input2 = raw_input("Enter input2?\n")

print "input1:%s, input2:%s" %(input1, input2)

(input1,input2) = (input2,input1)
print "input1:%s, input2:%s" %(input1, input2)




__author__ = 'ravi'
'''
#pet gene finder
sequence_six = raw_input("Enter a 6 base DNA and hit enter")
while len(sequence_six) != 6 : sequence_six = raw_input("Enter a 6 base DNA and hit enter")

j = -1
for i,base in enumerate(sequence_six):
    if sequence_six[i:i+3] == 'ATG':
        j = i
        print "First ATG is at %s" %j
        break
if j == -1: print j

# first fasta parser
fasta_genes = []
fasta_sequences = []

for i in range(6):
    user_input = raw_input("Enter gene or sequence ").strip()
    if user_input[0] == '>': fasta_genes.append(user_input[1:])
    else: fasta_sequences.append(user_input)

fasta_dict = dict(zip(fasta_genes,fasta_sequences))

print fasta_dict


# 911 operator
s = raw_input("Enter a number: ")
s = int(s)
t = 1 if s == 0 else 0
print t


#FizzBuzz
for i in range (1,101,1):
    if i%15 == 0: print "FizzBuzz"
    elif i%3 == 0: print "Fizz"
    elif i%5 == 0: print "Buzz"
    else: print i


#ASCII

string = "Rock and Roll"

for letter in string:
    print ord(letter)
ASCII_sum = 0

for letter in string:
    ASCII_sum += ord(letter)
print "ASCII_Sum:", ASCII_sum

ASCII_list = []
for letter in string:
    ASCII_list.append(ord(letter))
print ASCII_list

'''
# All roads lead to Rome

L = [2**i for i in range(7)]

#L = []
#for i in range(7): L.append(2**i)
#L = [1,2,4,8,16,32,64]
x = 5

for i,number in enumerate(L):
    if 2**x == number:
        print "at index ",i
        break

if 2**x in L:print "at index ", L.index(2**x)
else: print x, "not found"

myset = {(1,3,5),(1,3,5)}

print myset

listOfDictionaries = [{},{}]
listOfDictionaries[1]['ventricle'] = []
listOfDictionaries[1]['ventricle'].append('One of two lower chambers of the heart')
listOfDictionaries[1]['ventricle'].append('One of four cavities in the brain')

print listOfDictionaries
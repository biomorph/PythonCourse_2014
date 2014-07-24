__author__ = 'ravi'
import pandas
operon_table = pandas.read_table('E_coli_operons.gff',header=None)

for index in operon_table.index:
    start = str(operon_table.ix[index][3])
    stop = str(operon_table.ix[index][4])
    strand = operon_table.ix[index][6]
    if strand == '-': start,stop = stop,start
    column_9 = operon_table.ix[index][8]
    if index == len(operon_table.index)-1:
        print '\t'.join(['Chromosome',	'MicrobesOnline','operon',start,stop,'.',strand,'.',column_9])
        break
    next_start = str(operon_table.ix[index+1][3])
    if strand == '-': next_start = str(operon_table.ix[index-1][4])
    utr_start, utr_stop = stop, next_start
    length = abs(int(utr_stop) - int(utr_start)) + 1
    if length > 300: length = 300
    print '\t'.join(['Chromosome',	'MicrobesOnline','operon',start,stop,'.',strand,'.',column_9])
    column_9 += ' utr_length '+str(abs(length))+";"
    if abs(length) > 50:
        print '\t'.join(['Chromosome',	'MicrobesOnline','downstream_utr',utr_start,utr_stop,'.',strand,'.',column_9])




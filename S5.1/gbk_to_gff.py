__author__ = 'ravi'
import commands
import re

def get_feature_dict(start, end, file_handle):
    feature_dict= {}
    for line_num, line in enumerate(file_handle):
        if line_num > start and line_num < end:
            line = line.strip().split()
            if '/gene' not in line[0]:
                saved_line = line
            else:
                gene_name = line[0].split('=')[1].split('"')[1]
                if gene_name not in feature_dict and saved_line[0] not in ['tRNA','intron','rep_origin']: feature_dict[gene_name] = [saved_line]
                elif saved_line[0] not in ['tRNA','intron','rep_origin']: feature_dict[gene_name] = feature_dict[gene_name] + [saved_line]
    return feature_dict


def get_chunk_lines(file_name):
    cmd = 'grep -n FEATURES ' + file_name
    start_line = commands.getstatusoutput(cmd)[1].split(':')[0]
    cmd = 'grep -n ORIGIN ' + file_name
    end_line = commands.getstatusoutput(cmd)[1].split(':')[0]
    print start_line, end_line
    return (int(start_line),int(end_line))

gbk_fh = open('sequence.gb','r')

start, end = get_chunk_lines('sequence.gb')

feature_dict = get_feature_dict(start, end, gbk_fh)
print feature_dict
print len(feature_dict)
for entry in feature_dict:
    for feature_info in feature_dict[entry]:
        print feature_info
        feature = feature_info[0]
        #feature_start = re.findall(r'(\d+)..(\d+)',feature_info[1])[0][0]
        #feature_stop = re.findall(r'(\d+)..(\d+)',feature_info[1])[0][1]
        feature_strand = ''
        if feature_info[1].startswith('complement'): feature_strand = '-'
        else: feature_strand = '+'
        #print 'Chloroplast\t' + 'Genbank\t' + feature + '\t' + feature_start + '\t' + feature_stop + '\t.\t' + feature_strand + '\t.\t' + 'gene_id\"' + entry + '\";' + 'transcript_id\"' + entry + '\";'



__author__ = 'ravi'
import random
def parse_vcf(vcf_file, remove_ambiguous=False):
    vcf_fh = open(vcf_file,'r')
    ind_dict = {}
    individual_list = []
    S = 0
    if not remove_ambiguous:
        for entry in vcf_fh:
            entry = entry.strip().split("\t")
            if entry[0]=='#CHROM':
                for sample in entry[9:]:
                    sample = sample.split('-')[0]
                    ind_dict[sample] = []
                    individual_list.append(sample)
            elif entry[0]=='chr21' and entry[6]=='PASS':
                S += 1
                for i, individual in enumerate(individual_list):
                    genotype = entry[i+9]
                    random_genotype = get_random_genotype(genotype)
                    ind_dict[individual].append(random_genotype)
    else:
        for entry in vcf_fh:
            entry = entry.strip().split("\t")
            if entry[0]=='#CHROM':
                for sample in entry[9:]:
                    sample = sample.split('-')[0]
                    ind_dict[sample] = []
                    individual_list.append(sample)
            elif entry[0]=='chr21' and entry[6]=='PASS':
                #S += 1
                genotypes = '/'.join(entry[9:]).split("/")
                #print genotypes
                if "." in genotypes: continue
                S += 1
                for i, individual in enumerate(individual_list):
                    genotype = entry[i+9]
                    random_genotype = get_random_genotype(genotype)
                    ind_dict[individual].append(random_genotype)
    return ind_dict,S

def get_random_genotype(genotype_pair):
    genotypes = genotype_pair.split("/")
    int = random.randint(0,1)
    return genotypes[int]

def parse_individuals_table(table_file):
    individuals_fh = open(table_file,'r')
    pop_dict = {}
    for line in individuals_fh:
        line = line.strip().split("\t")
        if line[0] in pop_dict: pop_dict[line[0]].append(line[1])
        else: pop_dict[line[0]] = [line[1]]
    return pop_dict


vcf_dict, S = parse_vcf('test.vcf')
print vcf_dict
print len(vcf_dict.values()[0]), S

pop_dict = parse_individuals_table('CGS_Diversity+Ped_all54_indvs.txt')

#for population in pop_dict:




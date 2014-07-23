__author__ = 'ravi'
import glob
import subprocess as sp

fastq_file_list = glob.glob('*.fastq')

print fastq_file_list


program = 'tophat'
input_files = ','.join(fastq_file_list)
index = 'E_coli'
gtf = 'E_coli_mg1655.gtf'
output_dir = 'TophatOut'
num_procs = '6'

tophat_out = open('tophat_out','w')

proc = sp.Popen([program,'-G',gtf,'--no-novel-juncs','-o',output_dir,'-p',num_procs,index,input_files],stdout=tophat_out)


#!/usr/bin/python3
import os, subprocess, shutil
subprocess.call("esearch -db nucleotide -query \"AJ223353[accession]\" | efetch -format fasta | grep -v \">\" > AJ223353_noheader.fasta3",shell=True)

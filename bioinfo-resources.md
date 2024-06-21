## Bioinformatics Resources on GitHub
 The list was initially compiled for [RSG-Sweden](rsg-sweden.iscbsc.org)

1. [Getting started with genomics tools and resources](https://github.com/crazyhottommy/getting-started-with-genomics-tools-and-resources)
2. [Introduction to Bioinformatics](https://github.com/rsh249/bioinformatics)
3. https://github.com/dariober/bioinformatics-cafe
4. https://github.com/jdidion/biotools
5. https://github.com/stephenturner/oneliners
6. [Introduction to Applied Bioinformatics](https://github.com/applied-bioinformatics/An-Introduction-To-Applied-Bioinformatics)
7. https://github.com/danielecook/Awesome-Bioinformatics
8. [Introduction to DNA-Seq analysis - Workshop](https://github.com/mbourgey/Kyoto_DNAseq_workshop)
9. [Self-taught courses in bioinformatics](https://github.com/ossu/bioinformatics)
10. [BioInfoHacks: Bioinformatics Hacks](https://github.com/audy/bioinformatics-hacks)
11. [Bioinformatics training by Pacific Biosciences](https://github.com/PacificBiosciences/Bioinformatics-Training/wiki)

## A collection of useful reads on human reference genomes

- [Which human reference genome to use?](https://lh3.github.io/2017/11/13/which-human-reference-genome-to-use)
- You may be interested in checking out [awesome-sequencing-tech-resources](https://github.com/Nazeeefa/awesome-sequencing-tech-papers)

## Doing bioinformatics in terminal
#### Counts the number of reads in compressed FASTQ file
```
zcat < sample_lane.fastq.gz | awk '{i++}END{print i/4}'
```
#### See where sequence of interest in sequence files occurs
```
grep - n CATTAG *fastq
```
  

#### Counts the number of reads in compressed FASTQ file
```
zcat < sample_lane.fastq.gz | awk '{i++}END{print i/4}'
```

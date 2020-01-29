# ProTrack

The Clinical Proteomic Tumor Analysis Consortium (CPTAC) initiative has generated  a unique and extensive multi-omics data resource of deep proteogenomic profiles from several cancer types. To enable the broader community of biological and medical researchers to intuitively explore, query, and download data and analysis results from various CPTAC projects, we built a prototype user-friendly web application called “ProTrack” with the clear cell renal cell carcinoma (ccRCC) data set (http://ccrcc.cptac-data-view.org). Here we describe the salient features of this application which provides a dynamic, comprehensive, and granular visualization of CPTAC3 data.

### Data

Renal cell carcinoma (RCC), one of the top ten most commonly diagnosed cancers worldwide, is dominated by the clear cell histological subtype, which makes up 75% of all RCC cases [Clark et al]. To understand the molecular alterations underlying the ccRCC disease process, CPTAC has performed an extensive multi-omic characterization of 110 treatment-naive tumors and 84 paired normal adjacent tissues samples. In addition to clinical annotations, the underlying big-data resource includes molecular annotations for 11,355 proteins and 42,889 phosphopeptides, as well as whole genome sequencing (WGS), whole exome sequencing (WES), RNA sequencing (RNA-Seq), and methylation data. ProTrack organizes this data into top and bottom tracks of genetic and clinical annotations, including genomically confirmed ccRCC, non-ccRCC status; 3p copy number variation; an immune grouping for each sample; copy number variation for chromosomes 5q, 7p, 14q; chromosomes 2,3 and 3,5 translocations; genome instability; CpG island methylator phenotype (CIMP) status; grade; stage; and gender. Gene-level data can be represented by multiple tracks, when available, including mutation status ("Mut"), the beta value of CpG in the promoter region of the gene ("Methy"), the log ratio of copy number variation ("CNV (lr)"), the b-allele frequency of the copy number variation ("CNV (baf)") , gene expression levels ("mRNA"), gene-level protein abundance ("proteo"), and gene-level phosphoprotein abundance ("phospho"). See Clark et al for more details on the statistical summarization of the underlying data.

### References

TODO

### Development environment setup

These steps will install all required dependencies including development ones, run migrations and start dev server.

```bash
make dev
make migrate
make run
```

### Deployment

These steps will install production dependencies and build vuejs application to `static/dist` folder.

```bash
make prod
make build
```

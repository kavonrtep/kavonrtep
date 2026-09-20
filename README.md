<!-- Badge shorthands -->
[r]: https://img.shields.io/badge/R-276DC3?logo=r&logoColor=white
[py]: https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white
[rust]: https://img.shields.io/badge/Rust-000000?logo=rust&logoColor=white
[sh]: https://img.shields.io/badge/Shell-4EAA25?logo=gnubash&logoColor=white
[js]: https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black
[smk]: https://img.shields.io/badge/Snakemake-039475?logo=snakemake&logoColor=white
[galaxy]: https://img.shields.io/badge/Galaxy-2C3143?logo=galaxyproject&logoColor=white
[docker]: https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white
[apptainer]: https://img.shields.io/badge/Apptainer-1D3E6B?logo=linuxcontainers&logoColor=white

# Petr Novák

Bioinformatician at the [Laboratory of Molecular Cytogenetics](http://w3lamc.umbr.cas.cz/lamc/), [Biology Centre CAS](https://www.umbr.cas.cz/en/), České Budějovice.
I build tools for **annotation of repetitive DNA** — transposable elements, satellites, tandem repeats — in plant genomes.

[![RepeatExplorer](https://img.shields.io/badge/repeatexplorer.org-website-2C3143)](http://repeatexplorer.org/)
[![Galaxy server](https://img.shields.io/badge/RepeatExplorer-Galaxy%20server-2C3143?logo=galaxyproject&logoColor=white)](https://repeatexplorer-elixir.cerit-sc.cz/)
[![conda channel](https://img.shields.io/badge/conda-petrnovak-44A833?logo=anaconda&logoColor=white)](https://anaconda.org/petrnovak)

---

## Repeat annotation toolkit

Most of these tools work together: **DANTE** finds protein domains of transposable elements, **DANTE_LTR** and **DANTE_TIR** extend those hits to full-length elements, **TideCluster** and **TAREAN** handle tandem repeats, and **CARP** merges everything into one non-overlapping genome annotation.

| Tool | What it does | | |
|---|---|---|---|
| [**DANTE**](https://github.com/kavonrtep/dante) | Domain-based annotation of transposable elements using the REXdb protein database | ![R][r] ![Galaxy][galaxy] | ![stars](https://img.shields.io/github/stars/kavonrtep/dante?style=flat&label=%E2%98%85&color=555) ![conda](https://img.shields.io/conda/vn/petrnovak/dante?label=conda&color=44A833) |
| [**DANTE_LTR**](https://github.com/kavonrtep/dante_ltr) | Identification of complete LTR retrotransposons from DANTE domain hits | ![R][r] ![Galaxy][galaxy] | ![stars](https://img.shields.io/github/stars/kavonrtep/dante_ltr?style=flat&label=%E2%98%85&color=555) ![conda](https://img.shields.io/conda/vn/petrnovak/dante_ltr?label=conda&color=44A833) |
| [**DANTE_TIR**](https://github.com/kavonrtep/dante_tir) | DNA transposons with terminal inverted repeats, seeded by transposase domains | ![R][r] ![Galaxy][galaxy] | ![stars](https://img.shields.io/github/stars/kavonrtep/dante_tir?style=flat&label=%E2%98%85&color=555) ![conda](https://img.shields.io/conda/vn/petrnovak/dante_tir?label=conda&color=44A833) |
| [**TideCluster**](https://github.com/kavonrtep/TideCluster) | Tandem repeat detection and clustering in genome assemblies (TideHunter + mmseqs2 + BLAST) | ![Python][py] ![Galaxy][galaxy] | ![stars](https://img.shields.io/github/stars/kavonrtep/TideCluster?style=flat&label=%E2%98%85&color=555) ![conda](https://img.shields.io/conda/vn/petrnovak/tidecluster?label=conda&color=44A833) |
| [**RepeatExplorer2 / TAREAN**](https://github.com/kavonrtep/repex_tarean) | Graph-based repeat identification from unassembled reads; TAREAN reconstructs satellite consensus | ![Python][py] ![Galaxy][galaxy] | ![stars](https://img.shields.io/github/stars/kavonrtep/repex_tarean?style=flat&label=%E2%98%85&color=555) |
| [**CARP**](https://github.com/kavonrtep/CARP) | Comprehensive Annotation of Repeats Pipeline — integrates the tools above (plus LINE detection) into a single non-overlapping annotation | ![Python][py] ![Apptainer][apptainer] ![Galaxy][galaxy] | ![stars](https://img.shields.io/github/stars/kavonrtep/CARP?style=flat&label=%E2%98%85&color=555) ![conda](https://img.shields.io/conda/vn/bioconda/carp?label=bioconda&color=44A833) |
| [**kitehor**](https://github.com/kavonrtep/kitehor) | Sequence-agnostic higher-order repeat (HOR) detector for tandem repeat arrays | ![Rust][rust] | ![stars](https://img.shields.io/github/stars/kavonrtep/kitehor?style=flat&label=%E2%98%85&color=555) ![conda](https://img.shields.io/conda/vn/petrnovak/kitehor?label=conda&color=44A833) |
| [**te-cap**](https://github.com/kavonrtep/te_cap) | Divergence-tolerant TE boundary detector for LTR families, derived from CAP3 | ![Rust][rust] | ![stars](https://img.shields.io/github/stars/kavonrtep/te_cap?style=flat&label=%E2%98%85&color=555) |

<details>
<summary>Earlier tools</summary>

| Tool | What it does | |
|---|---|---|
| [repeat_annotation_pipeline](https://github.com/kavonrtep/repeat_annotation_pipeline) | RepeatExplorer-based assembly annotation (Galaxy tools) | ![R][r] ![Python][py] |
| [foursat](https://github.com/kavonrtep/foursat) | Visualisation of tandem repeat dotplots | ![R][r] |
| [tarean2probe](https://github.com/kavonrtep/tarean2probe) | Design of oligo FISH probe pools from TAREAN output | ![R][r] |
| [rexdb_scripts](https://github.com/kavonrtep/rexdb_scripts) | Helper scripts for the REXdb protein domain database | ![R][r] |

</details>

## Genome visualization & comparison

| Tool | What it does | | |
|---|---|---|---|
| [**dottir**](https://github.com/kavonrtep/dottir) | Modern Rust reimplementation of *Dotter*, the classic interactive dot-matrix plotter | ![Rust][rust] | ![stars](https://img.shields.io/github/stars/kavonrtep/dottir?style=flat&label=%E2%98%85&color=555) ![conda](https://img.shields.io/conda/vn/petrnovak/dottir?label=conda&color=44A833) |
| [**SynTrack**](https://github.com/kavonrtep/syntrack) | Multi-genome synteny browser with connection ribbons and propagated colouring | ![Python][py] | ![stars](https://img.shields.io/github/stars/kavonrtep/syntrack?style=flat&label=%E2%98%85&color=555) |
| [**SeqGrapheR**](https://github.com/kavonrtep/SeqGrapheR) | Interactive GUI for graph-based visualisation of read clusters | ![R][r] | ![stars](https://img.shields.io/github/stars/kavonrtep/SeqGrapheR?style=flat&label=%E2%98%85&color=555) ![conda](https://img.shields.io/conda/vn/petrnovak/r-seqgrapher?label=conda&color=44A833) |
| [**revis**](https://github.com/kavonrtep/revis) | Visualisation of RepeatExplorer2 comparative clustering output | ![R][r] | ![stars](https://img.shields.io/github/stars/kavonrtep/revis?style=flat&label=%E2%98%85&color=555) |
| [**granges_tools**](https://github.com/kavonrtep/granges_tools) | Command-line utilities built on GenomicRanges (GFF/BED manipulation) | ![R][r] | ![stars](https://img.shields.io/github/stars/kavonrtep/granges_tools?style=flat&label=%E2%98%85&color=555) |
| [shinyGenome](https://github.com/kavonrtep/shinyGenome) | Shiny app for interactive plotting of genome annotation (GFF) along chromosomes | ![R][r] | |

## Analysis pipelines

Containerised Snakemake workflows used in the lab.

| Pipeline | What it does | |
|---|---|---|
| [ont_genome_assembly_pipeline](https://github.com/kavonrtep/ont_genome_assembly_pipeline) | Oxford Nanopore assembly, contamination screening, QC and downstream analyses | ![Snakemake][smk] ![Apptainer][apptainer] |
| [yahs_pipeline](https://github.com/kavonrtep/yahs_pipeline) | Hi-C scaffolding with YaHS, including preprocessing and contact maps | ![Snakemake][smk] ![Apptainer][apptainer] |
| [illumina_preprocessing_pipeline](https://github.com/kavonrtep/illumina_preprocessing_pipeline) | Read QC, trimming and filtering for Illumina data | ![Snakemake][smk] ![Apptainer][apptainer] |
| [cenh3_chip_seq_pipeline](https://github.com/kavonrtep/cenh3_chip_seq_pipeline) · [peakBeast](https://github.com/kavonrtep/peakBeast) | ChIP-seq broad-peak analysis (epic2, MACS3, deepTools) for CENH3, and peakBeast for downstream peak handling | ![Snakemake][smk] ![Apptainer][apptainer] |
| [busco2aster](https://github.com/kavonrtep/busco2aster) | Species tree from BUSCO ortholog markers with ASTER | ![Snakemake][smk] |
| [jbrowse_prepare](https://github.com/kavonrtep/jbrowse_prepare) | Build JBrowse/Apollo track directories from a CSV table | ![Python][py] |

## Galaxy & packaging

| Repo | What it does | |
|---|---|---|
| [galaxy_packages](https://github.com/kavonrtep/galaxy_packages) | Galaxy Tool Shed wrappers for DANTE, DANTE_LTR, DANTE_TIR, TideCluster, CARP and RepeatExplorer2 | ![Galaxy][galaxy] |
| [galaxy_tools](https://github.com/kavonrtep/galaxy_tools) · [galaxy_tool_tests](https://github.com/kavonrtep/galaxy_tool_tests) | Additional wrappers and API-based tool testing with BioBlend | ![Galaxy][galaxy] ![Python][py] |
| [recipes](https://github.com/kavonrtep/recipes) | Conda recipes for the `petrnovak` channel | ![Shell][sh] |
| [dockerfiles](https://github.com/kavonrtep/dockerfiles) | Container definitions for lab tools | ![Docker][docker] |

## Teaching

| Repo | What it is | |
|---|---|---|
| [bioinformatics](https://github.com/kavonrtep/bioinformatics) | Practical exercises for the bioinformatics course — dotplots, alignments, assembly, annotation | ![Shell][sh] |
| [**Bioinformatics Playground**](https://kavonrtep.github.io/games/) | Interactive explorers for classic algorithms — dotplots, Needleman–Wunsch, Smith–Waterman, BLAST, MSA — *learn the algorithms by running them yourself* ([source](https://github.com/kavonrtep/games)) | ![JavaScript][js] [![pages](https://img.shields.io/badge/live-GitHub%20Pages-222?logo=github)](https://kavonrtep.github.io/games/) |
| [r_intro](https://github.com/kavonrtep/r_intro) | Introduction to R — fundamentals, data frames, tidyverse | ![R][r] |
| [protocols](https://github.com/kavonrtep/protocols) | Lab protocols, e.g. genome annotation in Galaxy | |

## Other

| Repo | What it is | |
|---|---|---|
| [hermit](https://github.com/kavonrtep/hermit) | Sandboxed AI data analyst for bioinformatics — Claude Code / Codex / Copilot CLI inside Apptainer with read-only data | ![Shell][sh] ![Apptainer][apptainer] |
| [candat](https://github.com/kavonrtep/candat) | Terminal text editor with emacs keybindings, built on Textual | ![Python][py] |

## Recent activity

<!--START_SECTION:activity-->
1. 🔒 Closed issue [#5](https://github.com/kavonrtep/galaxy_packages/issues/5) in [kavonrtep/galaxy_packages](https://github.com/kavonrtep/galaxy_packages)
<!--END_SECTION:activity-->

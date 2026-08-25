# External answer key — provenance

**File:** EXT_KEY_price2018_fitness_Keio_BW25113.tsv
**What it is:** Genome-wide mutant gene fitness for *E. coli* K-12 BW25113 (the Keio-collection parent strain), measured by RB-TnSeq (random-barcode transposon sequencing).
**Primary source:** Price MN, Wetmore KM, Waters RJ, et al. "Mutant phenotypes for thousands of bacterial genes of unknown function." *Nature* 557:503–509 (2018). doi:10.1038/s41586-018-0124-0. LBL Fitness Browser (fit.genomics.lbl.gov), organism "Keio".
**Retrieved via:** GitHub mirror dbernste/E_coli_GEM_validation, path Fitness_Data/E_coli_BW25113/fit_organism_Keio.tsv (raw, main branch), 2026-07-19.
**Columns:** orgId, locusId, sysName (= b-number), geneName, desc, then one column per assayed condition (fitness = normalized log2 mutant abundance change; ~0 = neutral, strongly negative = mutant depleted = gene needed).
**Glucose-minimal columns used as the phenotype:** those whose header contains "D-Glucose (C)".
**Externality:** measured by the Arkin/Deutschbauer lab (LBL), independently of this project and of AOP. The modeler did not set which genes are important — biology did.
**Note on coverage:** genes present in this table yielded enough transposon insertions to be assayed (i.e. are non-essential enough to sample); genes absent from it are candidates for essentiality (too few insertions), and are handled explicitly in the preregistration.

# Help4MultiQC plugin

This is a MultiQC plugin that allows to overload the help text of existing modules

### Installation 

```bash
python setup.py install
```

### Usage

```bash
multiqc --help4multiqc_config config.tsv ./
```

Where `config.tsv` follows the format : 

```
mname	sname	alt_text
FastQC	Sequence Counts	This is an alternative help for the sequencs counts section of the FastQC module
```

---
title: Make Small Molecule Mix
---

# Overview

Small Molecule Mix is a combination of thirty-one (31) small molecules (*e.g.*, rNTPs, amino acids, buffering salts, etc.) needed to fuel transcription and translation.

Here, we describe the components of Small Molecule Mix, how to make it, and how to store it properly.

::::{card}
:header: **Composition of Small Molecule Mix**
:::{table} 
:label: tbl:composition-table
:align: center

| **Reagent** | **Concentration in Energy Mix (mM)** | **Concentration in Final Reaction (mM)** |
| --- | --- | --- |
| HEPES-KOH (pH 7.6) | 125 | 50 |
| Potassium glutamate | 250 | 100 |
| Magnesium acetate | 18.75 | 7.5 |
| rATP  | 5 | 2 |
| rGTP | 5 | 2 |
| rCTP | 2.5 | 1 |
| rUTP | 2.5 | 1 |
| Amino Acids (each) | 0.75 | 0.3 |
| Creatine phosphate | 50 | 20 |
| Folinic acid | 0.05 | 0.02 |
| Spermidine | 5 | 2 |
| TCEP | 2.5 | 1 |

:::
::::

# Resources

::::{grid} 1 1 1 3

:::{card}
:header: **TODO: Lab-ready Protocol**
:algin: center

{button}`download <protocol-Make_tRNAs.pdf>`
:::

:::{card}
:header: **Assembly Worksheet**
{button}`download <Nucleus_v0.3.0_EMix-worksheet.xlsx>`
:::

:::{card}
:header: **TODO: Bill of Materials**
{button}`download <protocol-Make_tRNAs.pdf>`
:::

::::

<!-- ## Critical Reagents -->

::::{card }
:header: **Critical Reagents**

:::{table}
:label: tbl:critical-reagents
:align: center

:::{dropdown}
| **Reagent** | **Product Name** | **Manufacturer** | **Part #** | **Price** | Storage Conditions | **Link** |
| --- | --- | --- | --- | --- | --- | --- |
| Folinic acid | Folinic acid calcium salt hydrate | Sigma-Aldrich | F7878-100MG | $108 | 4C to 30C | [[link](https://www.sigmaaldrich.com/US/en/product/sial/f7878)] |

:::
::::

:::{card} **Prerequsite Protocols**

- [Make Amino Acid Mix (3.25 mM)](../make-amino-acid-mix/process-Make_Amino_Acid_Mix.md)

:::

# Protocol

**Prepare Folinic Acid Stock (5 mM).**
- [ ]  Weigh 12.5 mg folinic acid.
- [ ]  Dissolve to a final volume of 4.89 mL.
- [ ]  Aliquot and freeze at -20C.

**Make Stock Solutions.**
- [ ] Use the table below to prepare the specified stock solutions:

:::{table}
:label: tbl:stock-solutions
:align: center

| Reagent | **MW (g/mol)** | **Amount (g)** | **Final Volume (mL)** | **Storage** | **Needs pH adjustment?** | **Needs Sterilization?** |
| --- | --- | --- | --- | --- | --- | --- |
| Potassium Hydroxide (1 M) | 56.11 | 14.0 | 250 | 4C to 30C | no | no |
| HEPES-KOH (pH 7.6, 1 M) | 238.3 | 59.5 | 250 | 4C to 30C; dark | yes | no |
| Potassium glutamate (2.5 M) | 203.23 | 21.8 | 50 | 4C to 30C | no | no |
| Magnesium acetate (1 M) | 214.45 | 10.8 | 50 | 4C to 30C | no | no |
| Creatine phosphate (500 mM) | 327.14 | 1 | 9.43 | -25C to -15C | no | no |
| Folinic acid (5 mM) | 511.50 | See above  |  | -25C to -15C | no | no |
| Spermidine (500 mM) | 145.25 | 1 | 13.77 | -25C to -15C | no | no |
| Amino Acid Mix |  |  | see [Make Amino Acid Mix](../make-amino-acid-mix/process-Make_Amino_Acid_Mix.md)  | -85C to -15C | yes | yes |

:::

**Combine Small Molecule Mix components.**
- [ ] Use the table below to combine the previously prepared stock solutions into Small Molecule Mix:

:::{table}
:label: tlb:assembly
:align: center

| **Reagent** | **Stock Concentration (mM)** | **Concentration in Energy Mix (mM)** | **Volume to Add (uL)** |
| --- | --- | --- | --- |
| HEPES-KOH (pH 7.6) | 1000 | 125 | 62.5 |
| Potassium glutamate | 2500 | 250 | 50.0 |
| Magnesium acetate | 1000 | 18.75 | 9.38 |
| rATP | 100 | 5 | 25.0 |
| rGTP | 100 | 5 | 25.0 |
| rCTP | 100 | 2.5 | 12.5 |
| rUTP | 100 | 2.5 | 12.5 |
| Creatine phosphate | 500 | 50 | 50.0 |
| TCEP | 500 | 2.5 | 2.5 |
| Folinic acid | 5 | 0.05 | 5.0 |
| Spermidine | 500 | 5 | 5.0 |
| Amino Acid Mix | 3.25 | 0.75 | 115.4 |
| Ultrapure water |  n/a |  n/a | 15.82 |
| **Total** |  |  | 500 |

:::

**Storage.**
- [ ]  Aliquot Energy Mix into 1.5 mL microfuge tubes (between 50 uL and 100 uL per aliquot) and store at -80C.



---
title: Useful Tips and Tricks for Developer Notes
---

## Overview

Developer Notes (DevNotes) are written using MyST markdown, a flavor of markdown designed specifically for technical communication. The complete MyST markdown documentation can be found [here](https://mystmd.org/spec). 

The purpose of this document is to share some common MyST syntax patterns that we've found useful when writing DevNotes and gather them in one place. This document was prepared by looking at examples of previous DevNotes. We recommend exploring the markdown files of existing DevNotes to see these syntax patterns used in practice. See here for how to explore a DevNote. 

## Basic syntax

### Figures

:::{figure} https://github.com/rowanc1/pics/blob/main/sunset.png?raw=true
:label: fig:my-fig-0
my caption is really long and is being referenced completely...

:::

:::::{tab-set}


::::{tab-item} By file path

```
:::{figure} https://github.com/rowanc1/pics/blob/main/sunset.png?raw=true
:label: fig:my-fig-1
:align: center

Relaxing at the beach 
:::
```

::::{admonition} Will appear as...
:class: dropdown

:::{figure} https://github.com/rowanc1/pics/blob/main/sunset.png?raw=true
:label: fig:my-fig-1
:align: center

Relaxing 
:::
::::

::::{tab-item} By URL

```
:::{figure} https://github.com/rowanc1/pics/blob/main/sunset.png?raw=true
:label: fig:my-fig-2
:align: center

Relaxing at the beach 🏝 🌊 😎
:::
```

::::{admonition} Will appear as...
:class: dropdown

:::{figure} https://github.com/rowanc1/pics/blob/main/sunset.png?raw=true
:label: fig:my-fig-2
:align: center

Relaxing at the beach 🏝 🌊 😎
:::
::::


:::::



### Tables

### Referencing Figures and Tables within a document

As noted the `:label: fig:my-fig` allows you to references your figure within your document, for example {ref}`fig:my-fig-0`.

### Referencing the literature via DOI

## Connecting a Jupyter Notebook to your DevNote


## Figures

### Figures that include multiple panels

### Using Jupyter Notebooks to make sub-panels

## Tables

Here are the basic features of a table

### Tables for critical reagents

:::::{tab-set}

::::{tab-item} tab 1
<!-- :sync: tab0-1 -->
hello this is a text block 

```
| Condition | Description |
| --- | --- |
| No Folinic Acid  | Energy mix made without folinic acid. |
| Folinic  | Folinic acid dissolved in water, added to energy mix. |
| Folinic + MTHFS  | Folinic acid dissolved in water, added to energy mix + 0.07 µg/uL MTHFS supplemented to PURE reaction.  |
| 5,10-methenyl-THF | Folinic acid pre-converted using Shimizu’s method. |
| Positive Control | Standard NEB PURExpress reaction. |
| Negative Control | NEB PURExpress without input DNA. |
```


:::{admonition} Will appear as...
:class: dropdown
| Condition | Description |
| --- | --- |
| No Folinic Acid  | Energy mix made without folinic acid. |
| Folinic  | Folinic acid dissolved in water, added to energy mix. |
| Folinic + MTHFS  | Folinic acid dissolved in water, added to energy mix + 0.07 µg/uL MTHFS supplemented to PURE reaction.  |
| 5,10-methenyl-THF | Folinic acid pre-converted using Shimizu’s method. |
| Positive Control | Standard NEB PURExpress reaction. |
| Negative Control | NEB PURExpress without input DNA. |
:::
::::

::::{tab-item} tab 2
<!-- :sync: tab0-2 -->
hello this is a text block 

```
| Condition | Description |
| --- | --- |
| No Folinic Acid  | Energy mix made without folinic acid. |
| Folinic  | Folinic acid dissolved in water, added to energy mix. |
| Folinic + MTHFS  | Folinic acid dissolved in water, added to energy mix + 0.07 µg/uL MTHFS supplemented to PURE reaction.  |
| 5,10-methenyl-THF | Folinic acid pre-converted using Shimizu’s method. |
| Positive Control | Standard NEB PURExpress reaction. |
| Negative Control | NEB PURExpress without input DNA. |
```


:::{admonition} Will appear as...
:class: dropdown
| Condition | Description |
| --- | --- |
| No Folinic Acid  | Energy mix made without folinic acid. |
| Folinic  | Folinic acid dissolved in water, added to energy mix. |
| Folinic + MTHFS  | Folinic acid dissolved in water, added to energy mix + 0.07 µg/uL MTHFS supplemented to PURE reaction.  |
| 5,10-methenyl-THF | Folinic acid pre-converted using Shimizu’s method. |
| Positive Control | Standard NEB PURExpress reaction. |
| Negative Control | NEB PURExpress without input DNA. |
:::
::::

:::::

### Tables for DNA parts

### Tables to complement figures

### Creating a table from a Jupyter Notebook
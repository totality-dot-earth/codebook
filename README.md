# STR8D8A Codebook
Where data dictionaries live in honor and glory

For all the focus on making official data more openly available, the simple fact of publication is only the first step. For data to be useful, it must also be machine-readable, consistently formatted, complete, and clean. Many of the datasets made available on sites like data.gov do not meet this standard, and therefore require significant processing and munging before they can be used.

But even once the data has been prepared as described above, significant effort is still needed to extract value. In most cases, a key step in this process is to interpret or otherwise act upon the many alphanumeric codes that are used in these datasets. In some cases, these codings are specific to the department or agency that published the dataset, or even particular to the dataset itself. In other cases, however, these codings are actual or de facto standards that are developed by one or more bodies for shared use.

These shared codings are especially important to data scientists, analysts, and application developers, as they present an opportunity to connect application-specific data and logic to the these public data sources. Unfortunately, these codings are often hard to locate in complete form. When they can be found, they are rarely in a form that is ready to use without further work. This friction is unnecessary, and we want to get rid of it.

Codebook is simply a repository of these codings, freely available in this public repo.

| Coding Name | Description | Status |
| ----------- | ----------- | ------ |
| NAICS | North American Industry Classification System | [Done]() |
| CSA / CBSA | US Census Combined Statistical Areas and Core Based Statistical Areas | [Done]() |
| Census Class Code | Various codings commonly used in US Census data products | [Done]() |
| MTFCC | | [Done]() |

## Contributions
We welcome contributions to Codebook, and in the near future we will provide specific guidance on the suggested format for [pull requests](https://github.com/str8d8a/codebook/pulls).

## Requests
While we cannot make any blanket promises, our goal is for Codebook to eventually include the most commonly-used codings. So we certainly want to know if you are looking for a coding that is not currently in our collection. The best way to communicate one of these requests is to [file an issue](https://github.com/str8d8a/codebook/issues) on this repo.

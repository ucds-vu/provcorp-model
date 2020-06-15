Prov-Corp
=========              
A model for provenance-aware methods for the interoperability of linguistic corpora.

## Introduction
This repository is part of the Provenance for Linguistic Corpora Through Nanopublications paper written by Timo Lek, Anna de Groot, Tobias Kuhn, and Roser Morante (VU University Amsterdam).

## Content
* The public nanopublications that are generated as part of this project can be found in the 'np' directory.
* The SPARQL queries that are used to query the nanopublications can be found in the 'queries' directory, the output is in a separate folder.
* The docker-compose file that is used to start the Virtuose container to load the nanopublication and query them can be found in the 'src' directory. (https://hub.docker.com/r/tenforce/virtuoso/)
* The np script to use the java-nanopublication library can also be found in the 'src' directory. (https://github.com/Nanopublication/nanopub-java)
* The code that is used to generate the nanopublications can be found in the 'src/nanopubs' directory.

## Getting Started
NOTE: Since the np script of the java-nanopublication library is only working on Linux, the code also has to be executed on a Linux Operating System. Furthermore, Python 3.6, 'curl' and Java have to be installed.

### Step 0:
To be able to use the code one need to have access to the factbank_v1 and PARC3 (WSJ folders 00 and 01) corpora. These folders need to be placed in a folder called 'corpora' inside the 'src/nanopubs' directory.

### Step 1:
Running the code is straight forward. one only has to execute the 'run_all.sh' inside the 'src/nanopubs' directory. Note: To make sure that you get the correct results make sure that the 'results' folders are deleted from the 'src/nanopubs/Factbank' and 'src/nanopubs/PARC' directories.
On the first time that the np script is used it will download the most recent .jar library to execute the commands.

### Step 2:
Once the bash file has been executed all the nanopublications will be saved as NQuads in the 'src/data/toLoad' directory. These can now be queried using Virtuoso. To launch Virtuoso you can type docker-compose up in the 'src' directory.
NOTE: For Virtuoso container to work Docker has to be installed.

### Step 3
Once the container is active, you can go to 'localhost:8890/sparql' in the browser and execute the queries in the 'queries' directory.
NOTE: Some queries make use of of specific Trusty URIs that can change when the nanopublications are generated again. The correct URIs can therefore be found in the trusty files in results folders of the 'src/nanopubs/Factbank' and 'src/nanopubs/PARC' directories.

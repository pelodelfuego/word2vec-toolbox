word2vec-toolbox
===============

We provide here a __low level toolbox to manipulate word2vec__ vector space.

The idea is to have a proper __environement to study how word2vec captures the semantic relations__ between words, the project __just aim to explore possibilities__.

The project is organised in python package following this architecture:

├── data: _contains the data (models, dataset, word2vec voc file)_
├── notebook: _experiences and studies_
│   ├── classification: _detail results for the classification proof of concept_
│   └── dataExploration: _several studies about word2vec vector space_
├── thirdparty: _external tools_
└── toolbox: _the actual toolbox_

__Feel free to have a look at the guided tour__, it presents all the possibilities offered by the toolbox.


Overview
-------------
We can separate the project is 4 axes, each of them have a folder in the notebooks:

* __Exploration of data__
* __Domain__
* __Antonyms__
* __Taxonomy__


Data
-------
The repo comes with a __minimal__ environement to __run unit test__ and __notebooks__.

The complete data are available here:

[Link coming soon - end of january]

You'll need them if you want to reproduce experiences.

If you want to __use trained models__, be aware __all have been trained with the wikipedia corpus__, therefore make sure you __use the corresponding word2vec voc file__.

### Corpus

We used here the 2 corpus we worked here and trained the classifier with, both are __skip-gram__ and have respective parameters:

#### Text8
* size: 200
* window: 5
* sample: 1e-4
* negative: 5
* hs: 0

#### Wikipedia english
* size: 300
* window: 10
* sample: 1e-4
* negative: 5
* hs: 0


### Dataset and models

For classification tasks we used __wordnet__ (antonyms, taxonomy), and __manual annotation__(domain) as __ground truth__.<br>
All have been extracted and stored in files.

A lot of models have been trained, __only the best perfoming ones and the global summary log__ has been bundled in the repo.


General thought about word2vec
----------------------------------------------


Important results
-------------------------
Here is some interresting __results we found__ and __word2vec model limitation we highlighted__:

### Polar coordinates

### Human expert

### Several meaning


Conclusion
---------------


Credit
---------
This project has been partialy achieved during my research semester in NTU research lab, there for, I would like to thanks:

* [Pr Kim Jung Jae](https://www.linkedin.com/in/jung-jae-kim-75143533)
* [Luu Anh Tuan](https://www.linkedin.com/in/anh-tuan-luu-68592059)
* [Maciej Baranski](https://www.linkedin.com/in/maciej-baranski-18b66672)

for all the helpfull discussions we shared on this topic.

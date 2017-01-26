word2vec-toolbox
===============

We provide here a __low level toolbox to manipulate word2vec__ vector space.

The idea is to propose an __environement to study how word2vec captures the semantic relations__ between words, the project __just aim to explore possibilities__.

The project is organised in python package following this architecture:

├── data: _contains the data (models, dataset, word2vec voc file)_<br>
├── notebook: _experiences and studies_<br>
│   ├── classification: _detail results for the classification proof of concept_<br>
│   └── dataExploration: _several studies about word2vec vector space_<br>
├── thirdparty: _external tools_<br>
└── toolbox: _the actual toolbox_<br>

__Feel free to have a look at the guided tour__, it presents all the possibilities offered by the toolbox.

_Side note: sorry for the not pep8 style, I was not yet a real pythonic guy at this time :)_

Overview
-------------
We can separate the project is 4 axes, each of them have a folder in the notebooks:

* __[Exploration of data](https://github.com/pelodelfuego/word2vec-toolbox/tree/master/notebook/dataExploration)__
* __[Domain](https://github.com/pelodelfuego/word2vec-toolbox/blob/master/notebook/classification/domain.ipynb)__
* __[Antonyms](https://github.com/pelodelfuego/word2vec-toolbox/blob/master/notebook/classification/antonyms.ipynb)__
* __[Taxonomy](https://github.com/pelodelfuego/word2vec-toolbox/blob/master/notebook/classification/taxonomy.ipynb)__


Data
-------
The repo comes with a __minimal__ environement to __run unit test__ and __notebooks__.

The complete data are available here:

[Link coming soon - end of january]

You'll need them if you want to reproduce experiences.

If you want to __use trained models__, be aware __all have been trained with the wikipedia corpus__, therefore make sure you __use the corresponding word2vec voc file__.

### Corpus

We used here __2 corpus so 2 vector spaces.__

Both are __skip-gram__ and have the following respective parameters:

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

Desipte of the simple algorithm to produce it, having clear comprehension about word2vec is a challenge itself.<br>
We will try here to share __a vision of it - not to take for granted__.

The __generated vector space is a discretisation of the semantic__, just as a .JPG file attempt to describe a continuous plan space with a fixed resolution, word2vec tries to capture the infinites nuances of meaning of words with a finite number of dimensions.

Therefore, the main difference is a low resolution picture still understandable from a human point of view while __we are biased to understand and see the 'big picture' of a low resolution semantic__.

We __suspect__ _'understandable human level'_ semantic __to be approximated by a linear combinaisons of lower resolution tied together__ (notebook to come).

Beside this, as exposed in notebooks, __a cartesian approach of the vector space may not be the best fit__ to understand how the dimensions are tied together.


Important results
-------------------------

Here is some interesting __results we found__ and __word2vec model limitation we highlighted__:

### Polar coordinates

By exploring the data, __we shifted from cartesian to polar vector space__, it turns out that we can separate the concept in 2 parts:

* The semantic direction - angle
* How far to go in this direction - norm

This approach seems to provide good results to consider the taxonomic relations between concepts.
__While the angle provide the nature of the concept, the norm specify how specialized or precise to fully describe it__

### Human expert

Our classification tasks highlighted a problem: __due to the nature of data__ and the way it is learned,
__the human expert is not always able to decide the quality of the prediction__.

Indeed, __different human being would have different understanding of concept__ and therefore have __a different ground truth.__

__Can a single Human decide__ by a yes/no answer if __unambitious as the opposite of intelligent__ is a false positive ?<br>
Even a group of Human with different background would be unlikely to agree.

We also observed the __predicted results to challenge the edges of the ground truth__ in some cases.

### Several meaning

One limitation of word2vec is also __one word used in different contexts__, for exemple __skate is both a fish and a vehicle__.

Therefore, __the semantic position of a such concept would have a compromising position__, this may be resolved with enough dimensions.

It raises the question of __words being just a single dot to describe a continuous semantic space__, also at a human level and the need to create new words (or abstracted ones) or study etymologies.

Conclusion
---------------

One can affirme how versatile is word2vec as a tool is really impressive, we can run a lot of tasks based on what is captured.

Thus, this vectorial space despite of its limitations open a whole new word on NLP and on how we can understand semantic and langages.

Showing a different, discrete, but yet relevant description of the continus semantic field that constitute the world goes definitivly far beyond simple NLP tasks.

Up to each of us to invent new applications... =)


Credit
---------
This project has been partialy achieved during my research semester in NTU NLP research lab,<br>
therefore, I would like to thanks:

* [Pr Kim Jung Jae](https://www.linkedin.com/in/jung-jae-kim-75143533) - my advisor
* [Luu Anh Tuan](https://www.linkedin.com/in/anh-tuan-luu-68592059) - my collegue
* [Maciej Baranski](https://www.linkedin.com/in/maciej-baranski-18b66672) - my flatmate =)

for all the helpfull discussions we shared on this topic.

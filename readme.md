
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10794023.svg)](https://doi.org/10.5281/zenodo.10794023)

<h2 align="center"> Sentence-Level Annotated Dataset for Predicting Factuality of News and Bias of Media Outlets in Portuguese </h2>  

</br>
<p align="justify">Automated fact-checking and news credibility verification at scale require accurate prediction of news factuality and media bias. Here, we introduce a large sentence-level dataset, titled FactNews, composed of 6,191 sentences expertly annotated according to factuality and media bias definitions proposed by AllSides. We used the FactNews to assess the overall reliability of news sources by formulating two text classification problems for predicting sentence-level factuality of news reporting and bias of media outlets. Our experiments demonstrate that biased sentences present a higher number of words compared to factual sentences, besides having a predominance of emotions. Hence, the fine-grained analysis of subjectivity and impartiality of news articles showed promising results for predicting the reliability of the entire media outlet. Finally, due to the severity of fake news and political polarization in Brazil, and the lack of research for Portuguese, both dataset and baseline were proposed for Brazilian Portuguese. The following table describes in detail the FactNews labels, documents, and stories: </p>
</br>

</br>
<div align="center">

| Factual| Quotes | Biased | Total sentences | Total news stories | Total news documents |
| :---   | :---:  |   ---: |            ---: |               ---: |                  ---: |
| 4,242  | 1,391  | 558    | 6,161           | 100                | 300                   |

</div>
</br>

</br>
<div align="center">

| Media 1        | Media 2  | Media 3 | 
| :---           | :---:    |   ---: |  
| Folha de São Paulo   | Estadão  | O Globo    | 
</div>
</br>

</br>
<div align="center">

| Sentence-Level Media Bias Prediction     | Sentenve-Level Factuality Prediction  |
| :---                                     | :---:                                 |   
| 67% (F1-Score) by Fine-tuned mBert-case  | 88% (F1-Score) by Fine-tuned mBert-case|
</div>
</br>


<h2 align="left"> CITING </h2>
<p align="justify">
Vargas, F., Jaidka, K., Pardo, T.A.S., Benevenuto, F. (2023). <b>Predicting Sentence-Level Factuality of News and Bias of Media Outlets</b>. Proceedings of the 14th International Conference on Recent Advances in Natural Language Processing, pp.1197--1206. Varna, Bulgaria. https://aclanthology.org/2023.ranlp-1.127. 
</p>

<br>

<h2 align="left"> BIBTEX </h2>
<p align="justify">
@inproceedings{vargas-etal-2023-predicting,
    title = "Predicting Sentence-Level Factuality of News and Bias of Media Outlets",
    author = "Vargas, Francielle  and
      Jaidka, Kokil  and
      Pardo, Thiago  and
      Benevenuto, Fabr{\'\i}cio",
    editor = "Mitkov, Ruslan  and
      Angelova, Galia",
    booktitle = "Proceedings of the 14th International Conference on Recent Advances in Natural Language Processing",
    month = sep,
    year = "2023",
    address = "Varna, Bulgaria",
    publisher = "INCOMA Ltd., Shoumen, Bulgaria",
    url = "https://aclanthology.org/2023.ranlp-1.127",
    pages = "1197--1206",
    }
 </p> 
<br>


<h2 align="left"> FUNDING </h2>

![SSC-logo-300x171](https://github.com/franciellevargas/franciellevargas.github.io/blob/fc03a6672ab2937e413e4508a5061abed4a66098/img/google-logo-menor.png)
![SSC-logo-300x171](https://github.com/franciellevargas/franciellevargas.github.io/blob/fc03a6672ab2937e413e4508a5061abed4a66098/img/fapesp.jpg)



</br>



---
Title: Ideation - What, How, Why and Why not (By `Group ???`)
Date: 2024-03-03 14:00
Category: Progress Report
Tags: Group ???
---

_Author: Chau Cheuk Him, Hung Man Kay, Sean Michael Suntoso, Tai Ho Chiu Hero, Wong Ngo Yin_

The very first step of this group project, as always, is to formulate ideas and check their feasibility. In this blog post, we would like to discuss about the few ideas that we have. More specifically, we discussed about what exactly the topic is about, how NLP could be involved, and the reasons why the proposed topic should and should not be chosen.

## Idea 1: Congress Trading Analysis

#### Background

#### References

#### Code Skeleton

#### Challenges

## Idea 2: ESG Ratings Prediction

#### ESG Rating and its Significance 

The Environmental, Social, and Governance (ESG) score is often used to evaluate a company's strength of commitment to  sustainability and responsible business practices. It helps socially responsible investors on making investment decisions by providing insights into the company's sustainability performance.

While ESG rating agencies like MSCI, Sustainalytics and Bloomberg have different methodology, the following are generally considered:
- Environmental impact (greenhouse gass emissions, energy efficiency, etc.),
- Social responsibility (diversity and inclusion, product safety, etc.),
- Coperate governance practices (board composition and diversity, shareholder rights, etc.).

#### ESG Rating Prediction with NLP

A growing body of scholarly literature explores the application of natural language processing (NLP) techniques to extract structured data from ESG reports and subsequently analyze them using machine learning models. One such example is the ESGReveal methodology, which employs an LLM-based approach to harness NLP for the extraction of ESG data from corporate sustainability reports, ultimately generating ESG scores for companies.

Furthermore, several pre-trained language models, such as ESGBERT, are available and can be fine-tuned on ESG data to predict ESG scores for companies. These models employ transfer learning to capitalize on the knowledge acquired from extensive text data corpora and apply it to specialized tasks, including ESG scoring.

Another notable example in the literature is ESGify, a machine learning model capable of predicting ESG scores for companies based on their financial data. This model employs a combination of financial ratios and machine learning algorithms to anticipate a company's ESG score.

#### Challenges and Research Value

If we go with this topic, there might be a lot of challenges ahead since ESG score is usually done and audited manually. We also keep in mind that ESG is a hot topic that will interfered with investor decision, thus this project can be useful when doing due diligence of a company to invest.

#### References
- [What is #ESG Score and How it is Calculated | LinkedIn](https://www.linkedin.com/pulse/whats-esg-score-how-calculated-koviid-sharma/)
- [ESGReveal: An LLM-based approach for extracting structured data from ESG reports (arxiv.org)](https://arxiv.org/html/2312.17264v1)

## THE CONTECT BELOW SHOULD BE REMOVED BEFORE SUBMISSION

## How to Include a Link and Python Code

We chose [Investing.com](http://www.investing.com) to get the whole
year data of XRP and recalculated the return and 30 days volatility.

The code we use is as follows:
```python
import nltk
import pandas as pd
myvar = 8
DF = pd.read_csv('XRP-data.csv')
```


## How to Include a Quote

As a famous hedge fund manager once said:
>Fed watching is a great tool to make money. I have been making all my
>gazillions using this technique.



## How to Include an Image

Fed Chair Powell is working hard:

![Picture showing Powell]({static}/images/group-Fintech-Disruption_Powell.jpeg)

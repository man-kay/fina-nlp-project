# ESG Risk Level & Score Prediction with Language Models (By "TheWay")

## Abstract

## Data retrieval

- S&P 500 ESG Ratings
    - Contains ESG Risk Levels and Scores of companies;
    - Retrieved from https://www.kaggle.com/datasets/pritish509/.s-and-p-500-esg-risk-ratings;
    - Available at `data/raw/SP 500 ESG Risk Ratings.csv`.

- Scraped Motley Fool Earnings Call Transcripts
    - Contains Earnings Call Transcripts of companies;
    - Retrieved from https://www.kaggle.com/datasets/tpotterer/motley-fool-scraped-earnings-call-transcripts;
    - To download the dataset, run the following code snippet:
        ```bash
        pip install kaggle
        cd data/raw/
        kaggle datasets download -d tpotterer/motley-fool-scraped-earnings-call-transcripts
        ```
    - Alternatively, you may download it directly from [Kaggle](https://www.kaggle.com/datasets/tpotterer/motley-fool-scraped-earnings-call-transcripts) or [One Drive](https://connecthkuhk-my.sharepoint.com/:u:/g/personal/kathy09_connect_hku_hk/Ec35IH7l5kJBtMUkAjbn4l4BIKstenmtn4_IyzE7Sw08Jw?e=XgfpP0) and place it in  `data/raw/`.

## Model training and testing


## Acknowledgements
```bibtex
@misc{pritish_dugar_2023,
	title={S&P 500 ESG Risk Ratings},
	url={https://www.kaggle.com/ds/3660201},
	DOI={10.34740/KAGGLE/DS/3660201},
	publisher={Kaggle},
	author={Pritish Dugar},
	year={2023}
}
```


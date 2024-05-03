# ESG Risk Level & Score Prediction with Language Models (By "TheWay")

## Abstract

## File structure 
```
/project-root
│
├── /blogposts
│   ├── TheWay_01_Ideation-What-How-Why-and-Why-Not.md        # Blogpost 1: Introduction and ideation process for the project.
│   ├── TheWay_02_ESG-Risk-Level-and-Score-Prediction.md      # Blogpost 2: Deep dive into the ESG risk level and score prediction model.
│   └── /images                                               # Folder containing images used in blogposts 1 and 2.
│
├── /data
│   ├── /predicted
│   │   └── combined_predictions.csv                          # Contains the full dataset plus predictions on ESG score and risk level for deployment.
│   │
│   ├── /processed
│   │   ├── esg_score.csv                                     # Original dataset with ESG risk level and ESG risk score.
│   │   ├── transcript.csv                                    # Contains earning calls transcripts.
│   │   ├── transcript_esg.csv                                # Dataset with only ESG-related parts of the transcripts.
│   │   ├── train.csv                                         # Training dataset after applying train-test split.
│   │   ├── test.csv                                          # Testing dataset after applying train-test split.
│   │   ├── train_esg_shortened.csv                           # Final training dataset after applying NLP techniques to transcripts.
│   │   └── test_esg_shortened.csv                            # Final testing dataset after applying NLP techniques to transcripts.
│   │
│   └── /raw
│       └── SP_500_ESG_Risk_Ratings.csv                       # Original data source containing SP 500 ESG risk ratings.
│
└── /deploy                                                   # Contains the deployment-related scripts 
│   ├── deploy_model.py                                       # Python script for deploying the model using Flask.
│   └── index.html                                            # Webpage for the deployed model.
│
├── /notebooks
│   ├── /data_preprocessing
│   │   ├── 01_cleaning_esg.ipynb                           
│   │   ├── 01_cleaning_transcript.ipynb
│   │   ├── 02_ESGBert_text_extraction.ipynb
│   │   ├── 03_merging.ipynb
│   │   └── 04_shortening.ipynb
│   ├── /deployment
│   │   └── combine_best_results.ipynb                        # Here we use our best performing model to produce a .csv with our predicted class labels, and pass it to the deployment model 
│   ├── /esg_risk_level_predictions                           # Notebooks for all 3 models we have used for esg_risk_level prediction 
│   │   ├── finetuned_BERT_risk_level_classification.ipynb    # BERT model 
│   │   ├── finetuned_ESGBert_risk_level_prediction.ipynb     # ESG-BERT model 
│   │   └── finetuned_llama2_for_risk_level_prediction.ipynb  # LLaMA2 model 
│   └── /esg_score_prediction                                 # The models we used for esg_score prediction 
│       ├── finetuned_BERT_esg_score_prediction.ipynb         # BERT
│       └── finetuned_ESGBert_esg_score_prediction.ipynb      # ESG-BERT 
│
├── /results                                                  #  stores the .csv of our models' prediction 
│   ├── /bert_finetuned                                       # BERT
│       └── ...csv 
│   ├── /esgbert_finetuned                                    # ESG-BERT
│       └── ...csv 
│   └── /llama2_finetuned                                     # LLaMA2
│       └── ...csv 
│
├── .gitignore
└── README.md
```
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

## Deployment
For deployment, we first need to run the Flask App through the following command: 

### 1. Run the Flask App 
```python3 
python ./deploy/deploy_model.py 
```
### 2. Open the file `/deploy/index.html` 

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


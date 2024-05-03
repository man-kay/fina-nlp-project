# ESG Risk Level & Score Prediction with Language Models (By "TheWay")

## Project structure 
```
/project-root
│
├── /blogposts
│   ├── TheWay_01_Ideation-What-How-Why-and-Why-Not.md        # Blogpost 1: Introduction and ideation process for the project.
│   ├── TheWay_02_ESG-Risk-Level-and-Score-Prediction.md      # Blogpost 2: Deep dive into the ESG risk level and score prediction model.
│   └── /images                                               # Images used in blogposts 1 and 2.
│
├── /data
│   ├── /predicted
│   │   └── combined_predictions.csv                          # Processed data and predictions for deployment.
│   │
│   ├── /processed
│   │   ├── esg_score.csv                                     # Original dataset with ESG risk level and ESG risk score.
│   │   ├── transcripts.csv                                   # Contains earnings call transcripts.
│   │   ├── transcript_esg.csv                                # Dataset with only ESG-related parts of the transcripts.
│   │   ├── train.csv                                         # Training dataset after applying train-test split.
│   │   ├── test.csv                                          # Testing dataset after applying train-test split.
│   │   ├── train_esg_shortened.csv                           # Final training dataset after applying NLP techniques to further shorten transcripts.
│   │   └── test_esg_shortened.csv                            # Final testing dataset after applying NLP techniques to further shorten transcripts.
│   │
│   └── /raw                                                  # Raw data, see `Data Retrieval` below for more details.
│       ├── SP_500_ESG_Risk_Ratings.csv                       # Raw data containing SP 500 ESG risk ratings.
│       └── motley-fool-data.pkl                              # Raw data containing earnings call transcript.
|
└── /deploy                                                   # Deployment-related scripts 
│   ├── deploy_model.py                                       # Python script for deploying the model using Flask.
│   └── index.html                                            # Webpage for the deployed model.
│
├── /models                                                   # Saved fine-tuned models, see "Models" below for more details.
│   ├── /bert_for_risk_level_prediction                       # Fine-tuned BERT model for ESG risk level prediction
│       └── ... 
│   ├── /bert_for_score_prediction                            # Fine-tuned BERT model for ESG score prediction
│       └── ... 
│   └── /llama2_for_risk_level_prediction                     # Adapter config and weights of fine-tuned Llama2 model for ESG risk level prediction
│       └── ...
|
├── /notebooks
│   ├── /data_preprocessing                                   # Notebooks for data pre-processing
│   │   ├── 01_cleaning_esg.ipynb                             # Clean raw dataset containing ESG risk levels and scores
│   │   ├── 01_cleaning_transcript.ipynb                      # Clean dataset containing earnings call transcripts
│   │   ├── 02_ESGBert_text_extraction.ipynb                  # Extract ESG-related texts from earning calls transcripts
│   │   ├── 03_merging.ipynb                                  # Merge the two datasets and apply train-test-split
│   │   └── 04_shortening.ipynb                               # Further shorten the earnings call transcripts using NLP techniques
|   |
│   ├── /deployment
│   │   └── combine_best_results.ipynb                        # Generate a .csv file that contains ESG risk level and score predictions from the respective best model for deployment
|   |
│   ├── /esg_risk_level_predictions                           # Model training and testing for ESG risk level prediction 
│   │   ├── finetuned_BERT_risk_level_classification.ipynb    # BERT model 
│   │   ├── finetuned_ESGBert_risk_level_prediction.ipynb     # ESG-BERT model 
│   │   └── finetuned_llama2_for_risk_level_prediction.ipynb  # LLaMA2 model 
│   └── /esg_score_prediction                                 # Model training and testing for esg score prediction 
│       ├── finetuned_BERT_esg_score_prediction.ipynb         # BERT model
│       └── finetuned_ESGBert_esg_score_prediction.ipynb      # ESG-BERT model
│
├── /results                                                  # Model predictions (in .csv format)
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

## Models

- The best models for ESG risk level and score prediction are saved in `fina-nlp-project/models`.

- Refer to the section starting from `Load Model` in the respective notebook for procedures to load the saved model and generate predictions.
    - ESG risk level prediction: `fina-nlp-project/notebooks/esg_risk_level_prediction/finetuned_BERT_risk_level_classification.ipynb`
    - ESG score prediction: `fina-nlp-project/notebooks/esg_score_prediction/finetuned_BERT_esg_score_prediction.ipynb`

- Notice that the model weights are saved using [Git LFS](https://git-lfs.com/). It is possible that the `.safetensors` files retrieved are ammended and does not work properly. In that case, please download the model weights [One Drive](https://connecthkuhk-my.sharepoint.com/:f:/g/personal/kathy09_connect_hku_hk/Etmn9mxg-EVArc1YLjcv_ScBRYEc-ao4mcbhKplewQWNYw?e=YSy0Lg) and replace the original files.

## Deployment
For deployment, we first need to run the Flask App through the following command: 

#### 1. Run the Flask App using the following command
```bash
pip install flask_cors
python ./deploy/deploy_model.py 
```
#### 2. Open `/deploy/index.html` with a browser 

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


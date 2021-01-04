# Brewery Review NLP Project

## Final Capstone Project for Springboard Data Science Career Track

### March 2020 Cohort

![Brewery Review Word Cloud](reports/figures/word-cloud-beer-mug.png)

## Problem Statement

It's useful for review collection companies such as Google Places, Yelp, and TripAdvisor to summarize reviews into short descriptive sentences or phrases. For example, from Google Maps, "From scratch, Northern Italian dining."

**How can we generate short descriptions using reviews?**

We are limiting this project to breweries.

For example, "Spacious warehouse brewery with daily food trucks. Allows dogs. Features IPAs, Hazy IPAs, and high-gravity stouts."

### Scope

While the problem statement includes "generating short descriptions," this project report's primary purpose is training and evaluating an NLP model. We will address generating short descriptions in a future article.

#### Why Breweries?

The scope of this project is limited to breweries, mainly to keep annotation simple. For example, while "hazy" is a desired feature for beer, it does not generalize for all businesses or domains.

Additionally, beer and breweries are familiar domains for the researcher, the maintainer of the open-source project, [Open Brewery DB](https://www.openbrewerydb.org/).

### Problem Breakdown

The main problem is breaking down and summarizing text, but only pulling out words and phrases we value such as _brewery features, location, brewery names, and beer styles_. We can then use this information to construct some descriptive sentences.

A naive and extremely inefficient approach could be for a human to manually read through each brewery's reviews and develop a summarization sentence.

Another less naive but still inefficient approach could be to manually search for and find select words we want to highlight. Reading through a dozen or so reviews (or investigating the word cloud above) and one can quickly pick out common "valuable" words such as "selection," "spacious," "IPA," and many more.

However, even if we determine the word frequency of all brewery reviews, there are more words we might leave out.

Because of these complexities, machine learning and Natural Language Processing (NLP) will help us achieve our goals.

### Using NLP

We can use Named Entity Recognition to mark words and phrases to collect and use them to construct descriptive sentences.

We will be using [spaCy](https://spacy.io/) and transfer learning to update the named entity recognizer model.

## Data Wrangling

While there are some datasets available from review sites, this project's scope revolves around breweries, bottle shops, brewpubs, and "craft beer" bars. To maintain control over the data collection, it was determined scraping from a public website was the most reasonable course of action and would collect enough data for model training.

### Source - Beer Advocate

For this project, we scraped the beer review website [Beer Advocate](https://www.beeradvocate.com) (BA).

Other public resources were considered, such as Yelp and Google Places, but neither provided the kind of information required for this project. They also both had restrictions on what type of data you could pull via their API. A final prohibitive measure is that they are Javascripts apps, limiting scraping techniques, and increasing development time.

### Scraping Guidelines

Following a few guidelines to not overwhelm the BA website resources:

* Programmed a 1-second delay between requests,
* Performed requests during off-hours
* Added a custom User-Agent in case the administrator needed to contact me
* Only scraped data I needed
* Verified there was no available API to use

### Method

1. Gather cities
2. For each city, gather breweries
3. For each brewery, gather reviews
4. Save Cities, Breweries, and Reviews into a DB

All of the data is stored in an SQLite3 database.

#### DB Model Schema

* **Cities**
  * id (Integer)
  * name (String)
  * url (String)
  * ba_city_id (Integer)
* **Breweries**
  * id (Integer)
  * name (String)
  * street (String)
  * city_id (Integer)
  * url (String)
  * ba_brewery_id (Integer)
* **Reviews**
  * id (Integer)
  * text (Text)
  * date (Datetime)
  * rating (Float)
  * ba_brewery_id (Integer)

### Results

* 86 cities
* 4,984 breweries
* 45,417 reviews

### Lessons Learned

* It took ~5 hours to scrape ~5000 breweries. Each scrape took ~2 seconds with the delay. I completed the scrape between 12-14-2020 at 21:00 PST and 12-15-2020 at 04:00 PST.
* Using SQLite and SQLAlchemy was a good learning experience. A document-oriented database (document store), like MongoDB or AWS DynamoDB, would have served the same purpose and perhaps faster to implement.

## Exploratory Data Analysis

## Annotations

## Model Training & Tuning

## Evaluation

## Final model

## Conclusions

## Further Research

## Project Organization

------------

    ├── LICENSE
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── annotations    <- Annotation data used for training
    │   └── processed      <- The final, canonical data sets for modeling.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results-oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

------------

This project is based on the [cookiecutter data science project template](https://drivendata.github.io/cookiecutter-data-science/). #cookiecutterdatascience

# What makes a book loved by readers?

**Page Turners** is a Python data analysis project exploring Goodreads book ratings, popularity and publication trends using the Goodbooks-10k dataset.

The project combines data exploration, statistical analysis, visualization, a Jupyter notebook and an interactive Streamlit dashboard to investigate how readers evaluate books.

## Project overview
The aim of this project is to explore patterns in readers' ratings and understand how book popularity, rating distributions, user rating activity and publication years relate to readers' evaluations.

The analysis uses Python libraries such as Pandas, Matplotlib and Plotly to process the data, calculate descriptive statistics and create visualizations.

A **Jupyter notebook** presents the analysis step by step, while an interactive **Streamlit application** allows users to explore the results and compare individual books.

## Research questions
The project focuses on four main research questions:
1. **Popularity & ratings:** is there a relationship between the number of ratings a book receives and its average rating?
2. **Rating distributions:** how are ratings distributed across the five rating levels and how do these distributions differ between books?
3. **Reader behavior:** do more active readers rate books differently?
4. **Publication year:** is there a relationship between a book's publication year and its average rating?

## Dataset
The project uses the [Goodbooks-10k dataset](https://github.com/zygmuntz/goodbooks-10k), which contains metadata for approximately 10,000 books and nearly 6 million individual user ratings.
The dataset includes information about book titles, authors, publication years, average ratings, rating counts and user-generated tags.

The analysis primarily uses `books.csv` for book-level information and `ratings.csv` to investigate individual users' rating behavior.

## Analysis and key findings

### 1. Popularity & ratings
The relationship between the number of ratings and average book ratings is examined using descriptive statistics, Pearson correlation and Spearman correlation.

The results show a **negligible association** between popularity and average rating:
- Pearson correlation: **0.045**
- Spearman correlation: **0.065**

**This suggests that books receiving more ratings do not necessarily receive higher average ratings.**

### 2. Rating distributions
The distribution of ratings from 1 to 5 stars is examined both across the dataset and for individual books.

Overall, higher ratings are more common, with approximately **73.31%** of recorded ratings being either 4 or 5 stars.

The analysis also compares rating distributions across individual books through interactive visualizations in the Streamlit dashboard.

### 3. Reader behavior
The relationship between user rating activity and average rating is investigated using individual ratings from `ratings.csv`.
User activity is measured by the number of ratings assigned by each user. Pearson and Spearman correlations are calculated and users are divided into four activity groups.

The results indicate a very **weak negative association**:
- Pearson correlation: **-0.083**
- Spearman correlation: **-0.099**

The least active users assign an average rating of approximately 3.99 stars, compared to 3.88 stars among the most active users.
Although more active users tend to assign slightly lower ratings, the overall difference is small (approximately **0.11 stars**).

### 4. Publication year
The relationship between publication year and average rating is investigated using correlation analysis and visualizations grouped by year and decade.

The overall correlations are **close to zero**:
- Pearson correlation: **0.016**
- Spearman correlation: **-0.027**

These results indicate a negligible overall association between publication year and average rating, although some differences can be observed across individual years and decades.

The reported correlations refer to the full dataset of books with available publication years. In the Streamlit dashboard, correlations are recalculated dynamically based on the publication period selected by the user.

## Overall conclusions
The analysis suggests that **a book's popularity does not necessarily reflect how much readers appreciate it**.

The four research questions highlight the following findings:
- **Popularity & ratings:** books receiving more ratings do not necessarily achieve higher average ratings.
- **Rating distributions:** most ratings are positive, but rating patterns vary across individual books.
- **Reader behavior:** more active readers tend to assign slightly lower ratings, although the difference is small.
- **Publication year:** there is no clear overall relationship between publication year and average rating.

Overall, **none of the variables examined individually shows a strong association with average book ratings**. Readers' evaluations may depend on additional factors that are not captured by this analysis.

These results describe statistical associations and should not be interpreted as causal relationships.

For a more detailed explanation of the methodology and results, see [Analysis Documentation](analysis_datasets.md).

## Jupyter notebook
The [Page Turners notebook](notebooks/pageturners.ipynb) presents the complete analysis, combining explanatory text, code, tables and visualizations.

The notebook covers:
- Dataset loading and preliminary data exploration.
- Analysis of the four research questions.
- Visualization and interpretation of the results.
- Overall conclusions and limitations.

It reuses the functions defined in the `pageturners/` package, avoiding duplication of the analysis code.

## Interactive Streamlit application
An interactive dashboard was developed using Streamlit and Plotly to make the analysis accessible and easier to explore.

The application contains five pages:

| Page | What you can explore |
|---|---|
| **Overview** | Project summary, research questions, key findings and overall conclusions. |
| **Popularity & Ratings** | The relationship between the number of ratings and average book ratings, including Pearson and Spearman correlations. |
| **Rating distributions** | Overall rating frequencies and interactive distributions for individual books, searchable by title or author. |
| **Reader behavior** | User rating activity, correlation analysis and comparisons across four activity groups. |
| **Publication year** | Interactive rating trends by year or decade, with a selectable publication period and dynamically recalculated correlations. |

**Live application:** [Explore Page Turners](https://pageturners-apjsanp6cplbz5cwapjyd5.streamlit.app/)

## Technologies used

| Library / Tool | Purpose |
|---|---|
| **Python 3.14.7** | Main programming language used for the project. |
| **Pandas** | Data loading, cleaning, manipulation, grouping and statistical analysis. |
| **Matplotlib** | Static charts and visualizations used in the analysis scripts and notebook. |
| **Plotly** | Interactive charts in the Streamlit dashboard. |
| **SciPy** | Supports Spearman correlation calculations performed through Pandas. |
| **Ruff** | Code linting, import organization and formatting. |
| **Requests** | Automatic download of the original datasets. |
| **Streamlit** | Development and deployment of the interactive web application. |
| **Jupyter notebook** | Step-by-step presentation and reproduction of the analysis. |
| **IPykernel** | Python kernel used to execute the notebook. |
| **Git & GitHub** | Version control, project organization and code sharing. |

The required Python libraries are listed in `requirements.txt`.

## Installation and usage
Clone the repository:
```bash
git clone https://github.com/irene-barberis/pageturners.git
cd pageturners
```

### Python environment setup
The project was developed and tested using Python 3.14.7.

Create a virtual environment from the project root directory:
```bash
python -m venv .venv
```

Activate the virtual environment:
**Windows (PowerShell):**
```bash
.\.venv\Scripts\Activate.ps1
```

**macOS/Linux:**
```bash
source .venv/bin/activate
```

Install the required Python libraries:
```bash
python -m pip install -r requirements.txt
```

### Dataset setup
The project uses the [Goodbooks-10k repository](https://github.com/zygmuntz/goodbooks-10k). 

The original datasets are not included in this repository because of their size.

The original CSV files are automatically downloaded from the Goodbooks-10k repository when required and saved in `data/raw (dati_grezzi)/`.

If the files are already available locally, they are loaded directly without downloading them again.

The main analysis pipeline requires:
- `books.csv`: book metadata, including titles, authors, publication years and ratings.
- `ratings.csv`: individual user ratings used to analyze reader behavior.

To run the initial data exploration script (`scripts/data_exploration.py`), the additional files `book_tags.csv`, `tags.csv` and `to_read.csv` are also required.

The Streamlit application uses six preprocessed CSV files: 
- `data/books_for_app.csv`
- `data/popularity_correlations.csv`
- `data/overall_rating_distribution.csv`
- `data/reader_behavior_correlations.csv`
- `data/reader_activity_summary.csv`
- `data/publication_year_correlations.csv`

These files are generated by the analysis pipeline and allow the dashboard to run independently of the original data.

### Reproducing the analysis
To reproduce the analysis from the original Goodbooks-10k dataset,
run the main analysis script from the project root directory:

```bash
python -m scripts.run_analysis
```

The script runs all four research questions and automatically:
- Loads the original datasets.
- Calculates statistical measures and correlations.
- Generates the analysis visualizations.
- Saves the results as CSV files in `data/`.
- Saves the generated charts in `figures/`.
- Exports `books_for_app.csv` for the Streamlit dashboard.

The analysis is organized into reusable Python modules:
- `pageturners/data.py`: functions for downloading and loading datasets.
- `pageturners/analysis.py`: functions for statistical analysis.
- `pageturners/plots.py`: functions for generating visualizations.

The main script, `scripts/run_analysis.py`, coordinates these functions to reproduce the complete analysis.

### Running the Jupyter notebook
The notebook can be executed independently of the main analysis script.

After setting up the Python environment and installing the required libraries:
1. Open the project folder in Visual Studio Code.
2. Install the Jupyter extension if it is not already available.
3. Open `notebooks/pageturners.ipynb`.
4. Select the Python interpreter of the project's virtual environment as the notebook kernel.
5. Restart the kernel and run all cells from top to bottom.

The original datasets are automatically downloaded if they are not already available locally.

### Running the Streamlit application
The processed datasets and generated figures are included in the repository. Therefore, the Streamlit application can be launched without downloading the original datasets or rerunning the analysis pipeline.

Launch the interactive dashboard:
```bash
python -m streamlit run app.py
```
The application will open in a web browser.

## Project structure
The project follows a modular structure, separating reusable Python functions, analysis scripts, processed datasets, generated visualizations, a Jupyter Notebook and an interactive Streamlit dashboard.

```text
pageturners/
├── app.py                         # Interactive Streamlit dashboard
├── pageturners/                   # Reusable Python modules
│   ├── __init__.py
│   ├── data.py                    # Dataset download and loading
│   ├── analysis.py                # Statistical analysis
│   └── plots.py                   # Visualizations
├── scripts/
│   ├── data_exploration.py        # Dataset exploration 
│   └── run_analysis.py            # Complete analysis pipeline
├── notebooks/
│   └── pageturners.ipynb          # Step-by-step analysis presentation
├── data/                          # Processed data and results
│   ├── raw (dati_grezzi)          # Original datasets (not tracked by Git)
│   ├── books_for_app.csv
│   ├── popularity_correlations.csv
│   ├── overall_rating_distribution.csv
│   ├── reader_behavior_correlations.csv
│   ├── reader_activity_summary.csv
│   └── publication_year_correlations.csv
├── figures/                       # Generated charts
│   ├── average_rating_by_activity_group.png
│   ├── average_rating_by_decade.png
│   ├── average_rating_by_year.png
│   ├── overall_rating_distribution.png
│   ├── popularity_vs_rating.png
│   ├── publication_year_vs_rating.png
│   └── reader_activity_vs_rating.png
├── .streamlit/
│   └── config.toml                # Streamlit configuration
├── analysis_datasets.md           # Detailed analysis documentation
├── requirements.txt               # Python dependencies
├── .gitignore                     # Git exclusion rules
└── README.md                      # Project documentation
```

The `pageturners/` package contains reusable functions for data loading, statistical analysis and visualization.

The `scripts/` directory contains the initial data exploration script (`data_exploration.py`) and the main analysis pipeline (`run_analysis.py`), which runs all four research questions and generates the results and visualizations.

The `notebooks/` directory contains the Jupyter notebook, which reuses the package functions to present the analysis, visualizations and results.

The `data/` directory stores processed datasets and statistical results, while `figures/` contains the generated visualizations.

The original Goodbooks-10k datasets are stored in `data/raw (dati_grezzi)/` and excluded from version control because of their size.

## Documentation
Detailed information about data exploration, preparation, research methods, visualizations and findings is available in [analysis_datasets.md](analysis_datasets.md).
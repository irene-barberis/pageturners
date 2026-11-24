"""
Run the Page Turners data analysis and save the results.

This script uses the functions defined in the pageturners package
to generate analysis outputs and visualizations.
"""

# Import pandas to create and save summary tables
# Import pyplot to close figures after saving them
import matplotlib.pyplot as plt
import pandas as pd

# Import all the analysis functions for the four research questions
from pageturners.analysis import (
    calculate_activity_groups,
    calculate_user_stats,
    overall_rating_distribution,
    popularity_correlations,
    publication_year_correlations,
    reader_behavior_correlations,
)

# Import the function used to load the datasets
from pageturners.data import load_dataset

# Import all the plotting functions for the four research questions
from pageturners.plots import (
    plot_activity_groups,
    plot_average_rating_by_decade,
    plot_average_rating_by_year,
    plot_overall_rating_distribution,
    plot_popularity_vs_rating,
    plot_publication_year_vs_rating,
    plot_reader_activity,
)


def main():
    """
    Run the analysis for all four research questions and save the results.

    This function loads the datasets, performs the analyses, generates
    visualizations, and saves the outputs in the appropriate folders.
    """

    # RQ1 - POPULARITY VS RATING
    # Load book data, calculate correlations, and save the results

    books = load_dataset("books.csv")

    pearson, spearman = popularity_correlations(books)

    popularity_results = pd.DataFrame(
        {"method": ["Pearson", "Spearman"], "correlation": [pearson, spearman]}
    )

    popularity_results.to_csv("data/popularity_correlations.csv", index=False)

    fig = plot_popularity_vs_rating(books)
    fig.savefig("figures/popularity_vs_rating.png")
    plt.close(fig)

    print("RQ1 - Popularity vs rating completed.")

    # RQ2 - OVERALL RATING DISTRIBUTION
    # Calculate the percentage of ratings from 1 to 5 stars
    # Save the results as a CSV file and create a bar chart

    overall_percentages = overall_rating_distribution(books)

    rating_results = pd.DataFrame(
        {"stars": [1, 2, 3, 4, 5], "percentage": overall_percentages.values}
    )

    rating_results.to_csv("data/overall_rating_distribution.csv", index=False)

    fig = plot_overall_rating_distribution(overall_percentages)
    fig.savefig("figures/overall_rating_distribution.png")
    plt.close(fig)

    print("RQ2 - Overall rating distribution completed.")

    # RQ3 - READER BEHAVIOR
    # Analyze the relationship between user activity and average rating
    # Calculate correlations and compare four groups of users
    # Save two CSV files and two visualizations

    ratings = load_dataset("ratings.csv")

    user_stats = calculate_user_stats(ratings)

    pearson, spearman = reader_behavior_correlations(user_stats)

    reader_results = pd.DataFrame(
        {"method": ["Pearson", "Spearman"], "correlation": [pearson, spearman]}
    )

    reader_results.to_csv("data/reader_behavior_correlations.csv", index=False)

    fig = plot_reader_activity(user_stats)
    fig.savefig("figures/reader_activity_vs_rating.png")
    plt.close(fig)

    # Divide users into four groups based on their rating activity
    # and calculate the average rating for each group
    activity_summary = calculate_activity_groups(user_stats)

    activity_summary.to_csv("data/reader_activity_summary.csv", index=False)

    fig = plot_activity_groups(activity_summary)
    fig.savefig("figures/average_rating_by_activity_group.png")
    plt.close(fig)

    print("RQ3 - Reader behavior completed.")

    # RQ4 - PUBLICATION YEAR
    # Analyze the relationship between publication year and average rating
    # Calculate Pearson and Spearman correlations
    # Create three visualizations to explore rating trends over time

    pearson, spearman = publication_year_correlations(books)

    publication_results = pd.DataFrame(
        {"method": ["Pearson", "Spearman"], "correlation": [pearson, spearman]}
    )

    publication_results.to_csv("data/publication_year_correlations.csv", index=False)

    fig = plot_publication_year_vs_rating(books)
    fig.savefig("figures/publication_year_vs_rating.png")
    plt.close(fig)

    # Create a bubble chart showing the average rating by decade
    # Bubble sizes represent the number of books in each decade
    fig = plot_average_rating_by_decade(books)
    fig.savefig("figures/average_rating_by_decade.png")
    plt.close(fig)

    # Create a line plot showing average ratings by publication year
    # Only books published between 1980 and 2016 are included
    fig = plot_average_rating_by_year(books)
    fig.savefig("figures/average_rating_by_year.png")
    plt.close(fig)

    print("RQ4 - Publication year completed.")

    # EXPORT DATA FOR STREAMLIT
    # Select the book information needed by the interactive dashboard
    # Save a smaller dataset to avoid loading all raw data in Streamlit

    columns_for_app = [
        "book_id",
        "title",
        "authors",
        "average_rating",
        "ratings_1",
        "ratings_2",
        "ratings_3",
        "ratings_4",
        "ratings_5",
        "original_publication_year",
    ]

    books[columns_for_app].to_csv("data/books_for_app.csv", index=False)

    print("Streamlit dataset exported successfully.")


# Run the analysis when this script is executed directly
if __name__ == "__main__":
    main()

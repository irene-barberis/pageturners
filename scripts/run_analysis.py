
"""
Run the Page Turners data analysis and save the results.

This script uses the functions defined in the pageturners package
to generate analysis outputs and visualizations.
"""

# Import pandas to create and save summary tables
import pandas as pd

# Import pyplot to close figures after saving them
import matplotlib.pyplot as plt

# Import the function used to load the datasets
from pageturners.data import load_dataset

# Import all the analysis functions for the four research questions
from pageturners.analysis import (
    popularity_correlations,
    overall_rating_distribution,
    calculate_user_stats,
    reader_behavior_correlations,
    calculate_activity_groups,
    publication_year_correlations
)

# Import all the plotting functions for the four research questions
from pageturners.plots import (
    plot_popularity_vs_rating,
    plot_overall_rating_distribution,
    plot_reader_activity,
    plot_activity_groups,
    plot_publication_year_vs_rating,
    plot_average_rating_by_decade,
    plot_average_rating_by_year
)

def main():
    """
    Run the analysis for all four research questions and save the results.

    This function loads the datasets, performs the analyses, generates
    visualizations, and saves the outputs in the appropriate folders.
    """

    # RQ1 - POPULARITY VS RATING
    # Load book data, calculate correlations, and save the results

    # Load the books dataset
    books = load_dataset("books.csv")

    # Calculate Pearson and Spearman correlations
    pearson, spearman = popularity_correlations(books)

    # Create a DataFrame containing the correlation results
    popularity_results = pd.DataFrame({
        "method": ["Pearson", "Spearman"],
        "correlation": [pearson, spearman]
    })

    # Save the correlation results as a CSV file
    popularity_results.to_csv(
        "data/popularity_correlations.csv",
        index=False
    )

    # Create the popularity vs rating scatter plot
    fig = plot_popularity_vs_rating(books)

    # Save the figure in the figures folder
    fig.savefig("figures/popularity_vs_rating.png")

    # Close the figure to free memory
    plt.close(fig)

    # Print a confirmation message
    print("RQ1 - Popularity vs rating completed.")


    # RQ2 - OVERALL RATING DISTRIBUTION
    # Calculate the percentage of ratings from 1 to 5 stars
    # Save the results as a CSV file and create a bar chart

    # Calculate the overall percentage of each star rating
    overall_percentages = overall_rating_distribution(books)

    # Create a DataFrame with star ratings and their percentages
    rating_results = pd.DataFrame({
        "stars": [1, 2, 3, 4, 5],
        "percentage": overall_percentages.values
    })

    # Save the rating distribution results as a CSV file
    rating_results.to_csv(
        "data/overall_rating_distribution.csv",
        index=False
    )

    # Create the overall rating distribution bar chart
    fig = plot_overall_rating_distribution(overall_percentages)

    # Save the figure in the figures folder
    fig.savefig("figures/overall_rating_distribution.png")

    # Close the figure to free memory
    plt.close(fig)

    # Print a confirmation message
    print("RQ2 - Overall rating distribution completed.")



    # RQ3 - READER BEHAVIOR
    # Analyze the relationship between user activity and average rating
    # Calculate correlations and compare four groups of users
    # Save two CSV files and two visualizations

    # Load the ratings dataset
    ratings = load_dataset("ratings.csv")

    # Calculate the number of ratings and average rating for each user
    user_stats = calculate_user_stats(ratings)

    # Calculate Pearson and Spearman correlations between
    # the number of ratings and the average rating per user
    pearson, spearman = reader_behavior_correlations(user_stats)

    # Create a DataFrame containing the correlation results
    reader_results = pd.DataFrame({
        "method": ["Pearson", "Spearman"],
        "correlation": [pearson, spearman]
    })

    # Save the correlation results as a CSV file
    reader_results.to_csv(
        "data/reader_behavior_correlations.csv",
        index=False
    )

    # Create the scatter plot of reader activity versus average rating
    fig = plot_reader_activity(user_stats)

    # Save the scatter plot in the figures folder
    fig.savefig("figures/reader_activity_vs_rating.png")

    # Close the figure to free memory
    plt.close(fig)

    # Divide users into four groups based on their rating activity
    # and calculate the average rating for each group
    activity_summary = calculate_activity_groups(user_stats)

    # Save the activity group summary as a CSV file
    activity_summary.to_csv(
        "data/reader_activity_summary.csv",
        index=False
    )

    # Create the line plot comparing the four activity groups
    fig = plot_activity_groups(activity_summary)

    # Save the activity group plot in the figures folder
    fig.savefig("figures/average_rating_by_activity_group.png")

    # Close the figure to free memory
    plt.close(fig)

    # Print a confirmation message
    print("RQ3 - Reader behavior completed.")



    # RQ4 - PUBLICATION YEAR
    # Analyze the relationship between publication year and average rating
    # Calculate Pearson and Spearman correlations
    # Create three visualizations to explore rating trends over time

    # Calculate Pearson and Spearman correlations between
    # original publication year and average book rating
    pearson, spearman = publication_year_correlations(books)

    # Create a DataFrame containing the correlation results
    publication_results = pd.DataFrame({
        "method": ["Pearson", "Spearman"],
        "correlation": [pearson, spearman]
    })

    # Save the correlation results as a CSV file
    publication_results.to_csv(
        "data/publication_year_correlations.csv",
        index=False
    ) 

    # Create a scatter plot showing the relationship between
    # publication year and average rating
    fig = plot_publication_year_vs_rating(books)

    # Save the scatter plot in the figures folder
    fig.savefig("figures/publication_year_vs_rating.png")

    # Close the figure to free memory
    plt.close(fig)

    # Create a bubble chart showing the average rating by decade
    # Bubble sizes represent the number of books in each decade
    fig = plot_average_rating_by_decade(books)

    # Save the bubble chart in the figures folder
    fig.savefig("figures/average_rating_by_decade.png")

    # Close the figure to free memory
    plt.close(fig)

    # Create a line plot showing average ratings by publication year
    # Only books published between 1980 and 2016 are included
    fig = plot_average_rating_by_year(books)

    # Save the line plot in the figures folder
    fig.savefig("figures/average_rating_by_year.png")

    # Close the figure to free memory
    plt.close(fig)

    # Print a confirmation message
    print("RQ4 - Publication year completed.")


    # EXPORT DATA FOR STREAMLIT
    # Select the book information needed by the interactive dashboard
    # Save a smaller dataset to avoid loading all raw data in Streamlit

    # Select the columns used in the dashboard
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
        "original_publication_year"
    ]

    # Save the selected book information as a CSV file
    books[columns_for_app].to_csv(
        "data/books_for_app.csv",
        index=False
    )

    # Print a confirmation message
    print("Streamlit dataset exported successfully.")


# Run the analysis when this script is executed directly
if __name__ == "__main__":
    main()
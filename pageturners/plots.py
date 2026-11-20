
"""Functions for creating the Page Turners visualizations."""

import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
from pageturners.analysis import ratings_over_time

# RQ1 - POPULARITY VS RATING
# Visualize the relationship between book popularity and average rating
# using a scatter plot, where each point represents a book
# Use a logarithmic x-axis to better display differences in popularity

def plot_popularity_vs_rating(books):
    """
    Create a scatter plot of book popularity and average rating.

    Each point represents a book, with the x-axis showing the number
    of ratings (popularity) and the y-axis showing the average rating.

    Parameters
    ----------
    books : pandas.DataFrame
        Dataset containing 'work_ratings_count' and 'average_rating'.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Scatter plot of book popularity versus average rating.

    Notes
    -----
    The x-axis uses a logarithmic scale to better visualize books
    with very different numbers of ratings.
    """

    # Create a figure and an axes object
    # fig represents the entire figure, while ax represents the plotting area
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a scatter plot using the number of ratings on the x-axis
    # and the average rating on the y-axis
    # alpha controls the transparency of the points
    ax.scatter(
        books["work_ratings_count"],
        books["average_rating"],
        alpha=0.3
    )

    # Apply a logarithmic scale to the x-axis
    # This makes it easier to visualize books with very different rating counts
    ax.set_xscale("log")

    # Add a title and labels to explain the variables
    ax.set_title("Popularity vs average rating")
    ax.set_xlabel("Number of ratings (log scale)")
    ax.set_ylabel("Average rating")

    # Return the figure so it can be displayed or saved in another file
    return fig



# RQ2 - OVERALL RATING DISTRIBUTION
# Visualize the percentage of ratings from 1 to 5 stars
# using a bar chart to understand how readers evaluate books

def plot_overall_rating_distribution(overall_percentages):
    """
    Create a bar chart showing the overall rating distribution.

    Parameters
    ----------
    overall_percentages : pandas.Series
        Series containing the percentage of ratings for each star level.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Bar chart showing the percentage of each star rating.
    """

    # Create a figure and an axes object
    # fig represents the entire figure, while ax represents the plotting area
    fig, ax = plt.subplots(figsize=(8, 5))

    # Create a bar chart with star ratings on the x-axis
    # and the corresponding percentages on the y-axis
    ax.bar(
        [1, 2, 3, 4, 5],
        overall_percentages.values
    )

    # Add a title and labels to explain the variables
    ax.set_title("Overall rating distribution")
    ax.set_xlabel("Star rating")
    ax.set_ylabel("Percentage of ratings (%)")

    # Display all five star categories on the x-axis
    ax.set_xticks([1, 2, 3, 4, 5])

    # Return the figure so it can be displayed or saved in another file
    return fig



# RQ3 - READER ACTIVITY VS AVERAGE RATING
# Visualize the relationship between the number of ratings
# submitted by each user and their average rating
# Each point in the scatter plot represents one user

def plot_reader_activity(user_stats):
    """
    Create a scatter plot showing the relationship between reader activity and average rating.

    Parameters
    ----------
    user_stats : pandas.DataFrame
        DataFrame containing 'number_of_ratings' and 'average_rating' for each user.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Scatter plot of reader activity versus average rating.
    """

    # Create a figure and an axes object
    # fig represents the entire figure, while ax represents the plotting area
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a scatter plot with the number of ratings on the x-axis
    # and the average rating assigned by each user on the y-axis
    # alpha controls the transparency of the points
    ax.scatter(
        user_stats["number_of_ratings"],
        user_stats["average_rating"],
        alpha=0.3
    )

    # Add a title and labels to explain the variables
    ax.set_title("Reader activity vs average rating")
    ax.set_xlabel("Number of ratings per user")
    ax.set_ylabel("Average rating per user")

    # Return the figure so it can be displayed or saved in another file
    return fig



# AVERAGE RATING BY ACTIVITY GROUP
# Compare the average ratings assigned by four groups of users
# based on their rating activity: Low, Medium-low, Medium-high, and High
# Use a line plot with markers to show how average ratings change
# across groups with increasing levels of activity

def plot_activity_groups(activity_summary):
    """
    Create a line plot showing the average rating across user activity group.

    Parameters
    ----------
    activity_summary : pandas.DataFrame
        DataFrame containing 'activity_group' and 'mean_rating' for each group.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Line plot of average ratings for each user activity group.
        
        Notes
    -----
    The y-axis is restricted to the interval from 3.8 to 4.1
    to highlight small differences between groups.
    """

    # Create a figure and an axes object
    # fig represents the entire figure, while ax represents the plotting area
    fig, ax = plt.subplots(figsize=(9, 5))

    # Create a line plot connecting the four activity groups
    # Markers highlight the average rating of each group
    ax.plot(
        activity_summary["activity_group"],
        activity_summary["mean_rating"],
        marker="o"
    )

    # Set the y-axis limits to highlight small differences
    # The narrow scale makes small differences more visible
    ax.set_ylim(3.8, 4.1)

    # Add a grid to make the values easier to compare
    ax.grid(True, alpha=0.3)

    # Add a title and labels to explain the variables
    ax.set_title("Average rating by user activity group")
    ax.set_xlabel("User activity group")
    ax.set_ylabel("Average rating")

    # Return the figure so it can be displayed or saved in another file
    return fig


# RQ4 - PUBLICATION YEAR VS AVERAGE RATING
# Visualize the relationship between a book's original publication year
# and its average rating using a scatter plot
# Include only books published from the year 1000 onwards
# to avoid extremely old publication dates in the visualization

def plot_publication_year_vs_rating(books):
    """
    Create a scatter plot of publication year and average book rating.

    Parameters
    ----------
    books : pandas.DataFrame
        DataFrame containing 'original_publication_year' and 'average_rating'.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Scatter plot of publication year and average rating.
    
    Notes
    -----
    Books with missing publication years or publication years
    before 1000 are excluded from the visualization.
    """

    # Remove books with missing publication years
    books_with_year = books.dropna(
        subset=["original_publication_year"]
    )

    # Keep books published from the year 1000 onwards
    books_with_year = books_with_year[
        books_with_year["original_publication_year"] >= 1000
    ]

    # Create a figure and an axes object
    # fig represents the entire figure, while ax represents the plotting area
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a scatter plot with publication year on the x-axis
    # and average rating on the y-axis
    # Each point represents one book
    ax.scatter(
        books_with_year["original_publication_year"],
        books_with_year["average_rating"],
        alpha=0.3
    )

    # Add a title and labels to explain the variables
    ax.set_title("Publication year vs average rating")
    ax.set_xlabel("Original publication year")
    ax.set_ylabel("Average rating")

    # Return the figure so it can be displayed or saved in another file
    return fig


# AVERAGE RATING BY DECADE
# Visualize how average book ratings change across publication decades
# Use a bubble chart where each point represents one decade
# The size of each bubble represents the number of books in that decade
# Include only books published from 1800 onwards

def plot_average_rating_by_decade(books):
    """
    Create a bubble chart of average ratings by publication decade.

    Parameters
    ----------
    books : pandas.DataFrame
        DataFrame containing 'original_publication_year' and 'average_rating'.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Bubble chart of average ratings by decade.
        
        Notes
    -----
    Only books published from 1800 onwards are included.
    Bubble sizes represent the number of books in each decade.
    """

    # Remove books with missing publication years
    books_with_year = books.dropna(
        subset=["original_publication_year"]
    )

    # Keep books published from 1800 onwards
    books_with_year = books_with_year[
        books_with_year["original_publication_year"] >= 1800
    ]

    # Use the analysis function to calculate average ratings by decade
    decade_summary = ratings_over_time(books_with_year, grouping="Decade")

    # Create a figure and an axes object
    # fig represents the entire figure, while ax represents the plotting area
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a bubble chart with decades on the x-axis
    # and average ratings on the y-axis
    # Bubble sizes represent the number of books in each decade
    ax.scatter(
        decade_summary["period"],
        decade_summary["average_rating"],
        s=decade_summary["book_count"] * 2,
        alpha=0.5
    )

    # Add a title and labels to explain the variables
    ax.set_title("Average rating by publication decade")
    ax.set_xlabel("Publication decade")
    ax.set_ylabel("Average rating")

    # Return the figure so it can be displayed or saved in another file
    return fig


# AVERAGE RATING BY PUBLICATION YEAR
# Visualize how average book ratings change over time
# Calculate the average rating for each publication year
# Include only books published between 1980 and 2016

def plot_average_rating_by_year(books):
    """
    Create a line plot of average book ratings by publication year.

    Parameters
    ----------
    books : pandas.DataFrame
        Dataset containing book information, including the columns
        'original_publication_year', 'average_rating', and 'book_id'.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Figure showing the average rating for each publication year.
        
        Notes
    -----
    Only books published between 1980 and 2016 are included.
    Books with missing publication years are excluded.
    """

    # Remove books with missing publication years
    books_with_year = books.dropna(
        subset=["original_publication_year"]
    )

    # Keep books published between 1980 and 2016
    books_recent = books_with_year[
        books_with_year["original_publication_year"].between(1980, 2016)
    ]

    # Use the analysis function to calculate average ratings by year
    year_summary = ratings_over_time(books_recent, grouping="Year")

    # Create a figure and an axes object
    # fig represents the entire figure, while ax represents the plotting area
    fig, ax = plt.subplots(figsize=(10, 6))

    # Create a line plot with publication years on the x-axis
    # and average ratings on the y-axis
    # Markers highlight the average rating for each year
    ax.plot(
        year_summary["period"],
        year_summary["average_rating"],
        marker="o"
    )

    # Add a grid to make the values easier to compare
    ax.grid(True, alpha=0.3)

    # Add a title and labels to explain the variables
    ax.set_title("Average rating by publication year")
    ax.set_xlabel("Original publication year")
    ax.set_ylabel("Average rating")

    # Return the figure so it can be displayed or saved in another file
    return fig

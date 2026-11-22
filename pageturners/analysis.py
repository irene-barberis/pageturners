import pandas as pd 

# RQ1 - POPULARITY VS RATING
# Calculate the relationship between book popularity and average rating
# using Pearson and Spearman correlation coefficients

def popularity_correlations(books):
    """
    Calculate Pearson and Spearman correlations between book popularity
    and average rating.

    Parameters
    ----------
    books : pandas.DataFrame
    Dataset containing 'work_ratings_count' and 'average_rating'.

    Returns
    -------
    pearson : float
        Pearson correlation coefficient.
    spearman : float
        Spearman correlation coefficient.
    """

    pearson = books["work_ratings_count"].corr(
        books["average_rating"]
    )

    spearman = books["work_ratings_count"].corr(
        books["average_rating"],
        method="spearman"
    )

    return pearson, spearman


# RQ2 - RATING DISTRIBUTIONS
# Calculate the overall distribution of ratings from 1 to 5 stars
# to understand how readers evaluate books across the dataset

def overall_rating_distribution(books):
    """
    Calculate the overall percentage of ratings from 1 to 5 stars.

    Parameters
    ----------
    books : pandas.DataFrame
    Dataset containing the columns 'ratings_1', 'ratings_2',
    'ratings_3', 'ratings_4', and 'ratings_5'.

    Returns
    -------
    overall_percentages : pandas.Series
        Percentage of ratings for each star category.
    """

    rating_columns = [
        "ratings_1",
        "ratings_2",
        "ratings_3",
        "ratings_4",
        "ratings_5"
    ]

    # Count all ratings for each star category across all books in the dataset
    overall_counts = books[rating_columns].sum()

    # Calculate the total number of ratings across all star categories
    overall_total = overall_counts.sum()

    # Calculate the percentage of ratings for each star category
    overall_percentages = overall_counts / overall_total * 100

    # Return the calculated percentages
    return overall_percentages


# RQ3 - READER BEHAVIOR
# Calculate the number of ratings and the average rating for each user

def calculate_user_stats(ratings):
    """
    Calculate the number of ratings and average rating for each user.

    Parameters
    ----------
    ratings : pandas.DataFrame
        Dataset containing 'user_id' and 'rating'.

    Returns
    -------
    user_stats : pandas.DataFrame
        DataFrame containing each user's ID, number of ratings,
        and average rating.
    """


    # Group ratings by user and calculate individual statistics
    user_stats = ratings.groupby("user_id").agg(
        number_of_ratings=("rating", "count"),
        average_rating=("rating", "mean")
    ).reset_index()

    # Return the user-level statistics
    return user_stats


# Calculate the relationship between user activity and average rating
# using Pearson and Spearman correlation coefficients

def reader_behavior_correlations(user_stats):
    """
    Calculate Pearson and Spearman correlations between user activity and average rating.

    Parameters
    ----------
    user_stats : pandas.DataFrame
        DataFrame containing each user's ID, 'number of ratings', and 'average rating' for each user.

    Returns
    -------
    pearson : float
        Pearson correlation coefficient.
    spearman : float
        Spearman correlation coefficient.
    """

    # Calculate Pearson correlation
    pearson = user_stats["number_of_ratings"].corr(
        user_stats["average_rating"],
        method="pearson"
    )

    # Calculate Spearman correlation
    spearman = user_stats["number_of_ratings"].corr(
        user_stats["average_rating"],
        method="spearman"
    )

    # Return both correlation coefficients
    return pearson, spearman


# READER ACTIVITY GROUPS
# Divide users into four groups based on their rating activity
# and compare the average ratings assigned by each group

def calculate_activity_groups(user_stats):
    """
    Calculate average ratings for four user activity groups.

    Parameters
    ----------
    user_stats : pandas.DataFrame
        DataFrame containing each user's ID, number of ratings, and average rating.

    Returns
    -------
    activity_summary : pandas.DataFrame
        DataFrame containing the activity group, number of users
        and mean rating for each group.
    """

    # Create a copy to avoid modifying the original DataFrame
    user_stats = user_stats.copy()

    # Divide users into four groups based on rating activity
    user_stats["activity_group"] = pd.qcut(
        user_stats["number_of_ratings"],
        q=4, 
        labels=["Low", "Medium-low", "Medium-high", "High"]
    )

    # Calculate the number of users and mean rating for each group
    activity_summary = (
        user_stats.groupby("activity_group", observed=True)
        .agg(
            number_of_users=("user_id", "count"),
            mean_rating=("average_rating", "mean")
        )
        .reset_index()
    )

    # Return the summary table
    return activity_summary


# RQ4 - PUBLICATION YEAR AND RATINGS
# Analyze the relationship between a book's original publication
# year and its average rating using Pearson and Spearman correlations

def publication_year_correlations(books):
    """
    Calculate Pearson and Spearman correlations between publication year and average rating.

    Parameters
    ----------
    books : pandas.DataFrame
        DataFrame containing 'original_publication_year' and 'average_rating'.

    Returns
    -------
    pearson : float
        Pearson correlation coefficient.
    spearman : float
        Spearman correlation coefficient.
        
    Notes
    -----
    Books with missing publication years are excluded.
    """

    # Remove books with missing publication years
    books_with_year = books.dropna(
        subset=["original_publication_year"]
    )

    # Calculate Pearson correlation
    pearson = books_with_year["original_publication_year"].corr(
        books_with_year["average_rating"]
    )

    # Calculate Spearman correlation
    spearman = books_with_year["original_publication_year"].corr(
        books_with_year["average_rating"],
        method="spearman"
    )

    # Return both correlation coefficients
    return pearson, spearman


# RATINGS OVER TIME
# Group books by publication year or decade and calculate
# the average rating and number of books for each period

def ratings_over_time(books, grouping="Year"):
    """
    Calculate average ratings and book counts by year or decade.

    Parameters
    ----------
    books : pandas.DataFrame
        DataFrame containing 'book_id', 'original_publication_year', and 'average_rating'.
    grouping : str, default "Year"
        Type of grouping: 'Year' or 'Decade'.
        
    Returns
    -------
    summary : pandas.DataFrame
        DataFrame containing the publication year/decade, average rating, and book count for each period.
    """

    # Create a copy to avoid modifying the original DataFrame
    books = books.copy()
    
    # Exclude books with missing publication years
    books = books.dropna(subset=["original_publication_year"])

    # Group books by publication year
    if grouping == "Year":
        books["period"] = books["original_publication_year"].astype(int)

    # Group books by publication decade
    elif grouping == "Decade":
        books["period"] = (
            books["original_publication_year"] // 10 * 10
        ).astype(int)
        
    else:
        raise ValueError("Grouping must be 'Year' or 'Decade'.")

    # Calculate the average rating and number of books per period
    summary = books.groupby("period", as_index=False).agg(
        average_rating=("average_rating", "mean"),
        book_count=("book_id", "count")
    )

    # Return the summary table
    return summary
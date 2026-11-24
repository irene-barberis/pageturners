"""
Explore and validate the Goodbooks-10k datasets.

The script examines dataset structures, missing values,
relationships, duplicate records, and data anomalies.
"""

import pandas as pd


def explore_dataset(df, name):
    """
    Display basic information about a dataset.

    Parameters
    ----------
    df : pandas.DataFrame
        Dataset to explore.
    name : str
        Name of the dataset.

    Returns
    -------
    None
    """
    print(f"\n--- {name.upper()} DATASET ---")

    print("\nFirst five rows:")
    print(df.head())

    print("\nDataset shape:")
    print(df.shape)

    print("\nDataset information:")
    df.info()

    print("\nDescriptive statistics:")
    print(df.describe())

    print("\nMissing values:")
    print(df.isnull().sum())


# Load the datasets
books = pd.read_csv("data/raw (dati_grezzi)/books.csv")
ratings = pd.read_csv("data/raw (dati_grezzi)/ratings.csv")
book_tags = pd.read_csv("data/raw (dati_grezzi)/book_tags.csv")
tags = pd.read_csv("data/raw (dati_grezzi)/tags.csv")
to_read = pd.read_csv("data/raw (dati_grezzi)/to_read.csv")


# Explore all datasets
datasets = {
    "books": books,
    "ratings": ratings,
    "book_tags": book_tags,
    "tags": tags,
    "to_read": to_read,
}

for name, df in datasets.items():
    explore_dataset(df, name)


# Checking dataset relationships (ratings and books)

# count the number of unique book IDs in the ratings dataset
print("Unique book IDs in ratings:")
print(ratings["book_id"].nunique())

# count the number of unique book IDs in the books dataset
print("Unique book IDs in books:")
print(books["book_id"].nunique())

# check if all book IDs in ratings are also present in books
print("Are all ratings book IDs present in books book IDs?")
print(ratings["book_id"].isin(books["book_id"]).all())


# Checking dataset relationships (to_read and books)

# count the number of unique book IDs in the to_read dataset
print("Unique book IDs in to_read:")
print(to_read["book_id"].nunique())

# check if all book IDs in to_read are also present in books
print("Are all to_read book IDs present in books?")
print(to_read["book_id"].isin(books["book_id"]).all())


# Checking dataset relationships (book_tags and books)

# count the number of unique book IDs in the book_tags dataset
print("Unique book IDs in book_tags:")
print(book_tags["goodreads_book_id"].nunique())

# check if all book IDs in book_tags are also present in books
print("Are all book_tags book IDs present in books?")
print(book_tags["goodreads_book_id"].isin(books["goodreads_book_id"]).all())


# Checking dataset relationships (book_tags and tags)

# count the number of unique tag IDs in the book_tags dataset
print("Unique tag IDs in book_tags:")
print(book_tags["tag_id"].nunique())

# count the number of unique tag IDs in the tags dataset
print("Unique tag IDs in tags:")
print(tags["tag_id"].nunique())

# check if all tag IDs in book_tags are also present in tags
print("Are all book_tags tag IDs present in tags?")
print(book_tags["tag_id"].isin(tags["tag_id"]).all())


# Checking duplicate records

# Count fully duplicated rows in the books dataset
print("Duplicate rows in books:")
print(books.duplicated().sum())

# check whether book_id contains duplicates values
print("Duplicate rows in books_id:")
print(books["book_id"].duplicated().sum())

# Check for fully duplicated rows in the ratings dataset
print("Duplicate rows in ratings:")
print(ratings.duplicated().sum())

# Check whether the same user rated the same book more than once
print("Duplicate user-book combinations in ratings:")
print(ratings.duplicated(subset=["user_id", "book_id"]).sum())

# Check for fully duplicated rows in the to_read dataset
print("Duplicate rows in to_read:")
print(to_read.duplicated().sum())

# Check whether the same user added the same book more than once
print("Duplicate user-book combinations in to_read:")
print(to_read.duplicated(subset=["user_id", "book_id"]).sum())

# Check for fully duplicated rows in the book_tags dataset
print("Duplicate rows in book_tags:")
print(book_tags.duplicated().sum())

# Check whether the same tag is assigned more than once to the same book
print("Duplicate book-tag combinations:")
print(book_tags.duplicated(subset=["goodreads_book_id", "tag_id"]).sum())


# Display all rows with duplicated book-tag combinations
duplicate_tags = book_tags[
    book_tags.duplicated(subset=["goodreads_book_id", "tag_id"], keep=False)
]

print(duplicate_tags.sort_values(["goodreads_book_id", "tag_id"]))


# Initial data cleaning

# Remove fully duplicated rows from book_tags
# Store the cleaned data in a new DataFrame
book_tags_clean = book_tags.drop_duplicates()

# Some book-tag combinations remain duplicated because
# they have different count values.

# Check the number of rows before and after removing duplicates
print("Original rows:", len(book_tags))
print("Rows after cleaning:", len(book_tags_clean))
print("Removed rows:", len(book_tags) - len(book_tags_clean))

# Check remaining duplicated book-tag combinations after cleaning
remaining_duplicates = book_tags_clean[
    book_tags_clean.duplicated(subset=["goodreads_book_id", "tag_id"], keep=False)
]

# Display remaining duplicates sorted by book and tag
print(remaining_duplicates.sort_values(["goodreads_book_id", "tag_id"]))


# Check for fully duplicated rows in the tags dataset
print("Duplicate rows in tags:")
print(tags.duplicated().sum())

# Check whether tag_id contains duplicate values
print("Duplicate tag IDs:")
print(tags["tag_id"].duplicated().sum())

# Check whether tag names are repeated
# Different tag IDs may have the same tag name
print("Duplicate tag names:")
print(tags["tag_name"].duplicated().sum())


# Handling missing values in books

# Select books with a missing publication year
missing_year_books = books[books["original_publication_year"].isna()]

# Count books with a missing publication year
print("Books with missing publication year:")
print(len(missing_year_books))


# Keep only books with a known publication year
books_with_year = books.dropna(subset=["original_publication_year"])

# Check the number of remaining books
print("Books with publication year:", len(books_with_year))

# Check the number of excluded books
print("Excluded books:", len(books) - len(books_with_year))


# Check the minimum and maximum publication years
print("Minimum publication year:")
print(books_with_year["original_publication_year"].min())

print("Maximum publication year:")
print(books_with_year["original_publication_year"].max())

# Display descriptive statistics for publication years
print("Publication year statistics:")
print(books_with_year["original_publication_year"].describe())

# Identify books published before 1800
old_books = books_with_year[books_with_year["original_publication_year"] < 1800]

# Count books published before 1800
print("Books published before 1800:")
print(len(old_books))

# Display the oldest books
print(
    old_books[["title", "authors", "original_publication_year"]]
    .sort_values("original_publication_year")
    .to_string(index=False)
)


# Checking rating values

# Check the minimum and maximum average rating
print("Minimum average rating:")
print(books["average_rating"].min())

print("Maximum average rating:")
print(books["average_rating"].max())

# Count books with average ratings outside the valid range
invalid_ratings = books[(books["average_rating"] < 1) | (books["average_rating"] > 5)]

print("Books with invalid average ratings:")
print(len(invalid_ratings))


# Checking ratings count

# Check the minimum and maximum number of ratings
print("Minimum ratings count:")
print(books["ratings_count"].min())

print("Maximum ratings count:")
print(books["ratings_count"].max())

# Count books with zero or negative ratings
invalid_ratings_count = books[books["ratings_count"] <= 0]

print("Books with zero or negative ratings:")
print(len(invalid_ratings_count))


# Checking anomalous tag counts

# Check the minimum and maximum tag count
print("Minimum tag count:")
print(book_tags_clean["count"].min())

print("Maximum tag count:")
print(book_tags_clean["count"].max())

# Select records with negative tag counts
negative_tag_counts = book_tags_clean[book_tags_clean["count"] < 0]

# Count records with negative tag counts
print("Records with negative tag counts:")
print(len(negative_tag_counts))

# Display the six records with negative tag counts
print(negative_tag_counts.to_string(index=False))


# Identify the names of tags with negative counts
negative_tags_details = negative_tag_counts.merge(tags, on="tag_id", how="left")

# Display the negative counts and their tag names
print(
    negative_tags_details[
        ["goodreads_book_id", "tag_id", "tag_name", "count"]
    ].to_string(index=False)
)

# Remove records with negative tag counts
book_tags_clean = book_tags_clean[book_tags_clean["count"] >= 0].copy()

# Verify that no negative counts remain
print("Remaining negative counts:")
print((book_tags_clean["count"] < 0).sum())


# Checking rating distribution counts

# Select the columns containing the number of ratings by star
rating_columns = ["ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5"]

# Check the minimum value in each rating column
print("Minimum values by rating category:")
print(books[rating_columns].min())

# Count negative values in each rating column
print("Negative values by rating category:")
print((books[rating_columns] < 0).sum())


# Checking consistency of rating counts

# Calculate the sum of ratings from 1 to 5 stars for each book
books["total_star_ratings"] = books[
    ["ratings_1", "ratings_2", "ratings_3", "ratings_4", "ratings_5"]
].sum(axis=1)

# Select books where the two rating totals are different
inconsistent_ratings = books[books["total_star_ratings"] != books["work_ratings_count"]]

# Count books with inconsistent rating totals
print("Books with inconsistent rating counts:")
print(len(inconsistent_ratings))

# Display the first 10 inconsistent records
print(
    inconsistent_ratings[["title", "work_ratings_count", "total_star_ratings"]]
    .head(10)
    .to_string(index=False)
)


# Checking consistency with work-level rating counts

# Compare the sum of star ratings with work_ratings_count
matching_work_ratings = books["total_star_ratings"] == books["work_ratings_count"]

# Count books with matching values
print("Books with matching work rating counts:")
print(matching_work_ratings.sum())

# Count books with different values
print("Books with different work rating counts:")
print((~matching_work_ratings).sum())

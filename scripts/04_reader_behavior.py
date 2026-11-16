"""
RQ3 - Reader behavior.

Investigate whether more active readers tend to rate books
differently by analyzing individual rating activity,
calculating correlations, and comparing activity groups.
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the ratings dataset
ratings = pd.read_csv("data/raw (dati_grezzi)/ratings.csv")

# Calculate rating activity and average rating for each user
user_stats = ratings.groupby("user_id").agg(
    number_of_ratings=("rating", "count"),
    average_rating=("rating", "mean")
).reset_index()

print(user_stats.head())

# Descriptive statistics of user rating behavior
print("\nDescriptive statistics:")
print(user_stats[["number_of_ratings", "average_rating"]].describe())

# Correlation between user activity and average rating
pearson_corr = user_stats["number_of_ratings"].corr(
    user_stats["average_rating"],
    method="pearson"
)

spearman_corr = user_stats["number_of_ratings"].corr(
    user_stats["average_rating"],
    method="spearman"
)

print("\nCorrelation between rating activity and average rating:")
print(f"Pearson correlation: {pearson_corr:.3f}")
print(f"Spearman correlation: {spearman_corr:.3f}")

# Save correlation results for the Streamlit dashboard
correlation_results = pd.DataFrame({
    "method": ["Pearson", "Spearman"],
    "correlation": [pearson_corr, spearman_corr]
})

correlation_results.to_csv(
    "data/reader_behavior_correlations.csv",
    index=False
)

# Scatterplot: user activity vs average rating
plt.figure(figsize=(10, 6))

plt.scatter(
    user_stats["number_of_ratings"],
    user_stats["average_rating"],
    alpha=0.1,
    s=5
)

plt.title("User rating activity vs average rating")
plt.xlabel("Number of ratings per user")
plt.ylabel("Average rating per user")

plt.grid(alpha=0.3)
plt.savefig("figures/reader_activity_vs_rating.png", dpi=300)
plt.close()


# Divide users into four groups based on rating activity
user_stats["activity_group"] = pd.qcut(
    user_stats["number_of_ratings"],
    q=4,
    labels=["Low", "Medium-low", "Medium-high", "High"]
)

# Calculate average rating for each activity group
activity_summary = (
    user_stats.groupby("activity_group", observed=True)
    .agg(
        number_of_users=("user_id", "count"),
        mean_rating=("average_rating", "mean")
    )
    .reset_index()
)

# Save activity group summary for the Streamlit app
activity_summary.to_csv(
    "data/reader_activity_summary.csv",
    index=False
)


print("\nAverage rating by user activity group:")
print(activity_summary)


# Line chart: average rating by user activity group
plt.figure(figsize=(9, 6))

plt.plot(
    activity_summary["activity_group"],
    activity_summary["mean_rating"],
    marker="o",
    linewidth=2,
    color="steelblue"
)

plt.title("Average rating by user activity group")
plt.xlabel("User activity group")
plt.ylabel("Average rating")

plt.ylim(3.8, 4.1)
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("figures/average_rating_by_activity_group.png", dpi=300)
plt.close()
import pandas as pd

# Loading  the data from each file
price_df = pd.read_csv('data/airbnb_price.csv')
room_type_df = pd.read_excel('data/airbnb_room_type.xlsx')
last_review_df = pd.read_csv('data/airbnb_last_review.tsv', delimiter='\t')

# Clean 'room_type' data
room_type_df['room_type'] = room_type_df['room_type'].str.lower()

# Merge DataFrames on 'listing_id'
merged_df = pd.merge(price_df, room_type_df, on='listing_id')
merged_df = pd.merge(merged_df, last_review_df, on='listing_id')

# Convert 'last_review' to datetime format
merged_df['last_review'] = pd.to_datetime(merged_df['last_review'])

# Find the earliest and most recent review dates
earliest_review = merged_df['last_review'].min()
most_recent_review = merged_df['last_review'].max()

# Count the number of private room listings
private_rooms_count = merged_df[merged_df['room_type'] == 'private room'].shape[0]

# Convert 'price' to numeric and calculate the average listing price
merged_df['price'] = merged_df['price'].str.replace(' dollars', '').astype(float)
average_price = merged_df['price'].mean()

# Combine variables into a DataFrame
review_dates = pd.DataFrame({
    'first_reviewed': [earliest_review],
    'last_reviewed': [most_recent_review],
    'nb_private_rooms': [private_rooms_count],
    'avg_price': [round(average_price, 2)]
})

print(review_dates)

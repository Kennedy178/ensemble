
# 🗽 New York City Airbnb Data Analysis

This project explores the **New York City Airbnb market** by combining and analyzing data from **multiple file formats** (`.csv`, `.tsv`, and `.xlsx`) to extract insights about listings, pricing, and reviews.

## 📂 Project Overview

New York City is one of the most-visited cities in the world, leading to a high demand for temporary lodging through platforms like Airbnb.

This project combines Airbnb data from three different files to:

Here’s a clean, professional **README.md** draft for your Airbnb NYC project:

---

# 🗽 New York City Airbnb Data Analysis

This project explores the **New York City Airbnb market** by combining and analyzing data from **multiple file formats** (`.csv`, `.tsv`, and `.xlsx`) to extract insights about listings, pricing, and reviews.

## 📂 Project Overview

New York City is one of the most-visited cities in the world, leading to a high demand for temporary lodging through platforms like Airbnb.

This project combines Airbnb data from three different files to:

* **Clean and process listing data** (e.g., prices, room types, and reviews)
* **Merge datasets** from multiple formats into one comprehensive DataFrame
* **Analyze trends** in review dates, room availability, and pricing

---

## 📊 Data Sources

1️⃣ **`data/airbnb_price.csv`**

* Contains listing IDs, nightly prices, and locations.
* **Columns:** `listing_id`, `price`, `nbhood_full`

2️⃣ **`data/airbnb_room_type.xlsx`**

* Details Airbnb room descriptions and types.
* **Columns:** `listing_id`, `description`, `room_type`

3️⃣ **`data/airbnb_last_review.tsv`**

* Provides host names and the last review date for each listing.
* **Columns:** `listing_id`, `host_name`, `last_review`

---

## 🔧 Data Processing Steps

1. **Load Data**

   * CSV, Excel, and TSV files loaded using **pandas**.

2. **Clean Room Type Data**

   * Standardized `room_type` values to lowercase.

3. **Merge DataFrames**

   * All three datasets merged on the common key: `listing_id`.

4. **Convert Data Types**

   * Converted `last_review` to datetime format.
   * Removed `' dollars'` text from `price` and converted to `float`.

5. **Analysis Performed**

   * Found **earliest and most recent review dates**.
   * Counted total **private room listings**.
   * Calculated **average nightly price**.

---

## 📈 Key Insights

✅ **Earliest review:** 2019-01-01
✅ **Most recent review:** 2019-07-09
✅ **Number of private room listings:** 11,356
✅ **Average listing price:** \$141.78 per night

---


## 📦 Output

The script prints a summary DataFrame:

```
  first_reviewed last_reviewed  nb_private_rooms  avg_price
0     2019-01-01    2019-07-09             11356     141.78
```

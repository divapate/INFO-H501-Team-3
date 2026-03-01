import json
from collections import defaultdict

left_file = "restaurants_indy_philly.json"
right_file = "yelp_academic_dataset_review_no_text.json"
output_file = "indy_philly_restaurant_reviews.json"

# Step 1: Load reviews grouped by business_id
reviews_dict = defaultdict(list)

with open(right_file, "r", encoding="utf-8") as f:
    for line in f:
        review = json.loads(line)
        reviews_dict[review["business_id"]].append(review)

# Step 2: LEFT JOIN
with open(left_file, "r", encoding="utf-8") as left_f, \
     open(output_file, "w", encoding="utf-8") as out_f:

    for line in left_f:
        restaurant = json.loads(line)
        business_id = restaurant["business_id"]

        if business_id in reviews_dict:
            for review in reviews_dict[business_id]:
                joined_record = {**restaurant, **review}
                out_f.write(json.dumps(joined_record) + "\n")
        else:
            # Restaurant with no reviews
            out_f.write(json.dumps(restaurant) + "\n")

print("Done! Created:", output_file)
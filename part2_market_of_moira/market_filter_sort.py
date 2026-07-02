import pandas as pd

#Load the dataset
file_path = "Moira_Market_Items.csv"
df = pd.read_csv(file_path)

#Filter based on criteria
filtered = df [
  (df ["Price"] < 800) &
  (df ["Durability"] > 85) &
  (df ["Compatibility"] >= 0.80)
].copy()

#Merge Sort Implementation
def merge_sort(data, key1, key2):
  if len(data) <= 1:
    return data
  mid = len(data) // 2
  left = merge_sort(data[:mid], key1, key2)
  right = merge_sort(data [mid:], key1, key2)
  return merge(left, right, key1, key2)
  
def merge(left, right, key1, key2):
  result = []
  while left and right:
    l = left [0]
    r = right [0]
    if (l[key1], l[key2]) > (r[key1], r[key2]):
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  result.extend(left or right)
  return result
  
#Convert to list of dicts for sorting
filtered_dicts = filtered.to_dict(orient="records")
sorted_items = merge_sort(filtered_dicts, "Compatibility", "Durability")

#Convert back to DataFrame for display
sorted_df = pd.DataFrame (sorted_items)

#Display table
print("Filtered and Sorted Moira Market Items:")
print(sorted_df.head(10))

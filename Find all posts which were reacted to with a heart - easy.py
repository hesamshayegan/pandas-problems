# stratascratch - easy

import pandas as pd

facebook_reactions.head()

likes = facebook_reactions.loc[facebook_reactions["reaction"] == "heart", "post_id"]

merged = pd.merge(
        likes,
        facebook_posts,
        on="post_id",
        how="inner"
    )

result = merged.drop_duplicates()

# .loc[rows, columns] is designed for 2-dimensional selection:

# First argument → row filter
# Second argument → columns to select



# same but different indexing (instead of using loc)

# df = facebook_reactions
# df1 = df[df["reaction"]=="heart"]
# df1 = df1["post_id"]
# df_posts = facebook_posts
# df_m = df_posts.merge(df1, how="inner", on="post_id")
# df_m.drop_duplicates()
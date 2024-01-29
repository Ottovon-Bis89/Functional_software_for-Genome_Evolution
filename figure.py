# import plotly.graph_objects as go
# import pandas as pd

# # Create example data
# BV_types = ["BV Negative"] * 9 + ["BV Intermediate"] * 9 + ["BV Positive"] * 9
# BV_types_2 = (["BV Negative"] * 3 + ["BV Intermediate"] * 3 + ["BV Positive"] * 3) * 3
# BV_types_3 = (["BV Negative", "BV Intermediate", "BV Positive"] * 3) * 3
# count = [20,4,5,1,0,2,0,0,4,10,3,0,0,5,3,0,6,0,10,0,4,2,0,0,9,0,0]

# # Create a dataframe in long format
# data = pd.DataFrame({
#     'Baseline': BV_types,
#     '3 months': BV_types_2,
#     '6 months': BV_types_3,
#     'count': count
# })

# # Create a Sankey diagram
# fig = go.Figure(data=[go.Sankey(
#     node = dict(
#       pad = 15,
#       thickness = 20,
#       line = dict(color = "black", width = 0.5),
#       label = ["BV Negative", "BV Intermediate", "BV Positive", "BV Negative", "BV Intermediate", "BV Positive", "BV Negative", "BV Intermediate", "BV Positive"],
#       color = "blue"
#     ),
#     link = dict(
#       source = data['Baseline'].map({"BV Negative": 0, "BV Intermediate": 1, "BV Positive": 2}),
#       target = data['3 months'].map({"BV Negative": 3, "BV Intermediate": 4, "BV Positive": 5}),
#       value = data['count']
#     ))])

# fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
# fig.show()


# import plotly.graph_objects as go
# import pandas as pd

# # Create example data
# BV_types = ["BV Negative"] * 9 + ["BV Intermediate"] * 9 + ["BV Positive"] * 9
# BV_types_2 = (["BV Negative"] * 3 + ["BV Intermediate"] * 3 + ["BV Positive"] * 3) * 3
# BV_types_3 = (["BV Negative", "BV Intermediate", "BV Positive"] * 3) * 3
# count = [20,4,5,1,0,2,0,0,4,10,3,0,0,5,3,0,6,0,10,0,4,2,0,0,9,0,0]

# # Create a dataframe in long format
# data = pd.DataFrame({
#     'Baseline': BV_types,
#     '3 months': BV_types_2,
#     '6 months': BV_types_3,
#     'count': count
# })

# # Create a Sankey diagram
# fig = go.Figure(data=[go.Sankey(
#     node = dict(
#       pad = 15,
#       thickness = 20,
#       line = dict(color = "black", width = 0.5),
#       label = ["BV Negative", "BV Intermediate", "BV Positive", "BV Negative", "BV Intermediate", "BV Positive", "BV Negative", "BV Intermediate", "BV Positive"],
#       color = "blue"
#     ),
#     link = dict(
#       source = data['Baseline'].map({"BV Negative": 0, "BV Intermediate": 1, "BV Positive": 2}).tolist() + data['3 months'].map({"BV Negative": 3, "BV Intermediate": 4, "BV Positive": 5}).tolist(),
#       target = data['3 months'].map({"BV Negative": 3, "BV Intermediate": 4, "BV Positive": 5}).tolist() + data['6 months'].map({"BV Negative": 6, "BV Intermediate": 7, "BV Positive": 8}).tolist(),
#       value = data['count'].tolist() + data['count'].tolist()
#     ))])

# fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
# fig.show()

import plotly.graph_objects as go
import pandas as pd

# Create example data
BV_types = ["BV Negative"] * 9 + ["BV Intermediate"] * 9 + ["BV Positive"] * 9
BV_types_2 = (["BV Negative"] * 3 + ["BV Intermediate"] * 3 + ["BV Positive"] * 3) * 3
BV_types_3 = (["BV Negative", "BV Intermediate", "BV Positive"] * 3) * 3
count = [20,4,5,1,0,2,0,0,4,10,3,0,0,5,3,0,6,0,10,0,4,2,0,0,9,0,0]

# Create a dataframe in long format
data = pd.DataFrame({
    'Baseline': BV_types,
    '3 months': BV_types_2,
    '6 months': BV_types_3,
    'count': count
})

# Create a Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["BV Negative", "BV Intermediate", "BV Positive", "BV Negative", "BV Intermediate", "BV Positive", "BV Negative", "BV Intermediate", "BV Positive"],
      color = ["green", "purple", "red", "green", "purple", "red", "green", "purple", "red"]
    ),
    link = dict(
      source = data['Baseline'].map({"BV Negative": 0, "BV Intermediate": 1, "BV Positive": 2}).tolist() + data['3 months'].map({"BV Negative": 3, "BV Intermediate": 4, "BV Positive": 5}).tolist(),
      target = data['3 months'].map({"BV Negative": 3, "BV Intermediate": 4, "BV Positive": 5}).tolist() + data['6 months'].map({"BV Negative": 6, "BV Intermediate": 7, "BV Positive": 8}).tolist(),
      value = data['count'].tolist() + data['count'].tolist()
    ))])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()

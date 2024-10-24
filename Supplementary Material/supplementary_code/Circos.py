
from pycirclize import Circos
import pandas as pd

# Create matrix data (16 x 16) for the 16 chromosomes of the yeast genome
row_names = list(("Chr1", "Chr2", "Chr3", "Chr4", "Chr5", "Chr6", "Chr7", "Chr8", "Chr9", "Chr10","Chr11", "Chr12", "Chr13", "Chr14", "Chr15", "Chr16"))
col_names = row_names

# if there is interation, give 1, otherwise give 0.
matrix_data = [
    [0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
	[0,	0,	0,	0,	1,	0,	0,	1,	1,	0,	0,	1,	0,	0,	0,	0],
	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
	[0, 1,	0,	0,	1,	0,	0,	1,	0,	1,	1,	0,	1,	1,	0,	1],
	[1,	1,	1,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
	[0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0],
	[0,	0,	0,	0,	1,	0,	0,	1,	1,	1,	1,	0,	1,	1,	0,	0],
	[1,	0,	1,	0,	0,	1,	0,	0,	0,	0,	0,	1,	0,	0,	0,	0],
	[1,	0,	0,	0,	0,	1,	0,	0,	0,	0,	0,	0,	0,	0,	0,	0],
	[0,	0,	1,	0,	1,	0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	0],
	[0,	0,	1,	0,	0,	1,	0,	1,	1,	0,	0,	1,	0,	0,	0,	0],
	[0,	0,	0,	0,	1,	0,	0,	1,	1,	1,	1,	0,	1,	1,	0,	0],
	[0,	1,	0,	0,	1,	0,	0,	1,	1,	1,	1,	0,	0,	1,	0,	0],
	[0,	0,	1,	0,	1,	0,	0,	1,	1,	0,	0,	0,	0,	0,	0,	0],
	[0,	1,	0,	0,	1,	0,	0,	1,	1,	1,	1,	0,	0,	0,	0,	0],
	[1,	0,	1,	0,	1,	1,	0,	1,	1,	0,	1,	0,	0,	0,	0,	0],
]

matrix_df = pd.DataFrame(matrix_data, index=row_names, columns=col_names)

# Initialize from matrix (Can also directly load tsv matrix file)
circos = Circos.initialize_from_matrix(
    matrix_df,
    space=3,
    r_lim=(93, 100),
    cmap="tab10",
    ticks_interval=500,
    label_kws=dict(r=94, size=12, color="white"),
)

# print(matrix_df)
fig = circos.plotfig()
fig.show()
fig.savefig("ciros")
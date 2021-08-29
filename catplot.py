import matplotlib.pyplot as plt
import pandas as pd
import seaborn

fpath = '''D:\\dissertation\\git\\image_alignment\\final_output\\best_alignments.csv'''

df = pd.read_csv(fpath, header=0)

xvals = []
yvals = []
images = []
for x in df['image']:
    floats = [m for m in x.split("_")]
    floats = [float(m) for m in x.split("_")]
    xvals.append(int(floats[1]))
    yvals.append(int(100*floats[2]))

cc = df['CC2']

list_of_tuples = list(zip(xvals, yvals, cc))

new_df = pd.DataFrame(list_of_tuples, columns=['Max Features',
                                               'Proportion good matches (%)', 'Correlation Coefficient'])

# print(new_df)
# seaborn.heatmap(new_df, vmin=0, vmax=1)
pt = seaborn.catplot(x='Proportion good matches (%)', y="Correlation Coefficient", hue="Max Features",
                data=new_df, height=4)
pt.set(ylim=(0,1))
pt.savefig("preview/catplot_all.jpg")
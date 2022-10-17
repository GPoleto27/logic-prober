from re import S
import pandas as pd
import seaborn as sns
import numpy as np

# Read the data
df = pd.read_csv("avg_runtime_report.csv")
# n_vars,n_lines,avg_time

# Seaborn save plot
sns.set_theme(style="whitegrid")

palette = sns.color_palette("YlGnBu", 4)

sns_plot = sns.lineplot(x="n_vars", y="avg_time", hue="n_lines", palette=palette, data=df)
# set title
sns_plot.set_title("Tempo médio de execução em relação ao № de variáveis")
# set x label
sns_plot.set_xlabel("Número de variáveis")
# set y label
sns_plot.set_ylabel("Tempo médio de execução (s)")
# set hue label
sns_plot.legend(title="Número de expressões")
# save plot
sns_plot.figure.savefig("avg_runtime_n_vars.png")

sns_plot.set(xscale="log", yscale="log")
# set title
sns_plot.set_title("Tempo médio de execução em relação ao № de variáveis (escala logarítmica)")
sns_plot.figure.savefig("avg_runtime_n_vars_log.png")

# clear
sns_plot.clear()

palette = sns.color_palette("YlGnBu", 7)

sns_plot = sns.lineplot(x="n_lines", y="avg_time", hue="n_vars", palette=palette, data=df)
# set title
sns_plot.set_title("Tempo médio de execução em relação ao № de linhas")
# set x label
sns_plot.set_xlabel("Número de expressões")
# set y label
sns_plot.set_ylabel("Tempo médio de execução (s)")
# set hue label
sns_plot.legend(title="Número de variáveis")
# save plot
sns_plot.figure.savefig("avg_runtime_n_lines.png")


sns_plot.set(xscale="log", yscale="log")
# set title
sns_plot.set_title("Tempo médio de execução em relação ao № de linhas (escala logarítmica)")
sns_plot.figure.savefig("avg_runtime_n_lines_log.png")

# clear plot
sns_plot.clear()

palette = sns.color_palette("YlGnBu", 2)

# generate a list for n_vars from dataframe where n_lines=1000
n_vars = df.loc[df['n_lines'] == 1000, 'n_vars'].tolist()
# generate a list for avg_time from dataframe where n_lines=1000
avg_time = df.loc[df['n_lines'] == 1000, 'avg_time'].tolist()

y = [2**i for i in n_vars]

f_x = [n_vars, y]
F_x = [n_vars, avg_time]
# compute correlation coefficient between f(x) and F(x)
corr = np.corrcoef(f_x, F_x)

sns_plot.set(xscale="log", yscale="log")

sns_plot = sns.lineplot(x=n_vars, y=y, color=palette[0], label="f(x)=2^x")
sns_plot = sns.lineplot(x=n_vars, y=avg_time, palette=palette, label="F(x)")
# set title
sns_plot.set_title("Tempo médio de execução em relação ao № de variáveis (escala logarítmica)")
# set x label
sns_plot.set_xlabel("Número de variáveis")
# set y label
sns_plot.set_ylabel("Tempo médio de execução (s)")
# set hue label
sns_plot.legend(title="Número de expressões")
# save plot
sns_plot.figure.savefig("avg_runtime_n_vars_log_scatter.png")

sns_plot.clear()

# plot correlation coefficient between f(x) and F(x)
sns_plot = sns.heatmap(corr, annot=True, cmap="YlGnBu")
# set title
sns_plot.set_title("Correlação entre f(n)=2^n e F(n)")
# set x label
sns_plot.set_xlabel("f(n)=2^n")
# set y label
sns_plot.set_ylabel("Tempo de execução (s) por número de variáveis")
# save plot
#sns_plot.figure.savefig("correlation_runtime_by_n_vars.png")

# mean correlation coefficient
mean_corr = np.mean(corr)
print("Mean correlation coefficient: ", mean_corr)

# clear plot
sns_plot.clear()

palette = sns.color_palette("YlGnBu", 2)

# generate a list for n_lines from dataframe where n_vars=16
n_lines = df.loc[df['n_vars'] == 16, 'n_lines'].tolist()
# generate a list for avg_time from dataframe where n_vars=16
avg_time = df.loc[df['n_vars'] == 16, 'avg_time'].tolist()

# generate a list for f(x)=x
x = [i for i in range(1, len(n_lines)+1)]
y = [i for i in range(1, len(n_lines)+1)]

f_x = [x, y]
F_x = [n_lines, avg_time]
# compute correlation coefficient between f(x) and F(x)
corr = np.corrcoef(f_x, F_x)

# plot correlation coefficient between f(x) and F(x)
sns_plot = sns.heatmap(corr, annot=True, cmap="YlGnBu")
# set title
sns_plot.set_title("Correlação entre f(n)=n e F(n)")
# set x label
sns_plot.set_xlabel("f(n)=n")
# set y label
sns_plot.set_ylabel("Tempo de execução (s) por número de expressões")
# save plot
sns_plot.figure.savefig("correlation_runtime_by_n_lines.png")

# mean correlation coefficient
mean_corr = np.mean(corr)
print("Mean correlation coefficient: ", mean_corr)

sns_plot.clear()
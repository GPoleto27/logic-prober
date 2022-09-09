import pandas as pd
import seaborn as sns

# Read the data
df = pd.read_csv("avg_runtime_report.csv")
# n_vars,n_lines,avg_time

# Seaborn save plot
sns.set_theme(style="whitegrid")

palette = sns.color_palette("rocket_r", 4)

sns_plot = sns.lineplot(x="n_vars", y="avg_time", hue="n_lines", palette=palette, data=df)
# set title
sns_plot.set_title("Tempo médio de execução em relação ao número de variáveis")
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
sns_plot.set_title("Tempo médio de execução em relação ao número de variáveis (escala logarítmica)")
sns_plot.figure.savefig("avg_runtime_n_vars_log.png")

# clear plot
sns_plot.clear()

palette = sns.color_palette("rocket_r", 7)

sns_plot = sns.lineplot(x="n_lines", y="avg_time", hue="n_vars", palette=palette, data=df)
# set title
sns_plot.set_title("Tempo médio de execução em relação ao número de linhas")
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
sns_plot.set_title("Tempo médio de execução em relação ao número de linhas (escala logarítmica)")
sns_plot.figure.savefig("avg_runtime_n_lines_log.png")

# clear plot
sns_plot.clear()

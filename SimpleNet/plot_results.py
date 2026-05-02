import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the results
df = pd.read_csv('/home/ad6b8/Documents/MLinCVProject/SimpleNet/results/MVTec_LOCO_Results/simplenet_mvtec_loco/run/results.csv')

# Drop the Mean row for plotting the bar chart
df_plot = df[df['Row Names'] != 'Mean']

categories = df_plot['Row Names'].str.replace('mvtec_', '').str.replace('_', ' ').str.title()
instance_auroc = df_plot['instance_auroc']
full_pixel_auroc = df_plot['full_pixel_auroc']
anomaly_pixel_auroc = df_plot['anomaly_pixel_auroc']

x = np.arange(len(categories))
width = 0.25

fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width, instance_auroc, width, label='Image AUROC')
rects2 = ax.bar(x, full_pixel_auroc, width, label='Pixel AUROC')
rects3 = ax.bar(x + width, anomaly_pixel_auroc, width, label='PRO Score')

ax.set_ylabel('AUROC / PRO Score')
ax.set_title('SimpleNet Performance on MVTec LOCO')
ax.set_xticks(x)
ax.set_xticklabels(categories, rotation=45, ha='right')
ax.legend()

fig.tight_layout()
plt.savefig('/home/ad6b8/Documents/MLinCVProject/SimpleNet/results/MVTec_LOCO_Results/simplenet_mvtec_loco/run/simplenet_loco_performance.png')
print("Graph saved to /home/ad6b8/Documents/MLinCVProject/SimpleNet/results/MVTec_LOCO_Results/simplenet_mvtec_loco/run/simplenet_loco_performance.png")

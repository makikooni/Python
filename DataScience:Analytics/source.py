""" source of data: https://www.kaggle.com/datasets/uciml/mushroom-classification 
This dataset includes descriptions of hypothetical samples corresponding to 23 species
of gilled mushrooms in the Agaricus and Lepiota Family Mushroom drawn from The Audubon
Society Field Guide to North American Mushrooms (1981). 
"""
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("mushroom_data.csv")
columns = df.columns.tolist()
print(df.isnull().sum())

def plot_graphs(df):
    output_directory = "/Users/makikooni/Github/mushroom_data/Figures"
    columns = df.columns.tolist()
    
    
    unique_palette = sns.color_palette("Set2", n_colors=len(columns)) 
    sns.set_palette(unique_palette)
    
    for column in columns:
        plt.figure(figsize=(10, 6))
        unique_values = df[column].nunique()
        value_counts = df[column].value_counts()
        
        if unique_values >= 5 or max(value_counts) / sum(value_counts) > 0.9:
            sns.countplot(data=df, x=column, order=df[column].value_counts().index)
            plt.title(column + " Value Counts")
            plt.xticks(rotation=30, fontsize=10)
            plt.xlabel(column, fontsize=12)
            

            for i, count in enumerate(value_counts):
                plt.text(i, count + 10, str(count), ha='center', fontsize=10)
                
        else:
            value_counts = df[column].value_counts()
            pie_chart = plt.pie(value_counts, labels=value_counts.index, startangle=140)
            plt.title(column + " Value Distribution")
            
            percentages = [f"{(val / sum(value_counts)) * 100:.1f}%" for val in value_counts]
            legend_labels = [f"{index} - {percentage}" for index, percentage in zip(value_counts.index, percentages)]
            
            plt.legend(pie_chart[0], legend_labels, loc="upper right", bbox_to_anchor=(1.3,1 ))
        
            
        output_filename = os.path.join(output_directory, f"{column}_countplot.png")
        plt.tight_layout()
        plt.savefig(output_filename)
        plt.close()

def find_modes(df,column_choice):
    total_rows = len(df)
    modes = df.mode()

    mode_values = {}  # Create a dictionary to store mode values

    for column in df.columns:
        mode_value = modes.loc[0, column]
        mode_count = (df[column] == mode_value).sum()
        mode_percentage = (mode_count / total_rows) * 100
        mode_values[column] = (mode_value, mode_percentage)
        
        if column == column_choice:
            print(f"Mode of the column {column} is: {mode_value}, Percentage: {mode_percentage:.2f}%")
    
    return mode_values

#find_modes(df,'Habitat')
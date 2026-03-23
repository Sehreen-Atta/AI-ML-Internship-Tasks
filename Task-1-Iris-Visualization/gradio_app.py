import gradio as gr
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
iris = sns.load_dataset("iris")

# Function to plot histogram
def plot_hist(feature):
    plt.figure()
    iris[feature].hist()
    plt.title(f"{feature} Distribution")
    return plt

# Gradio interface
app = gr.Interface(
    fn=plot_hist,
    inputs=gr.Dropdown(choices=list(iris.columns[:-1]), label="Select Feature"),
    outputs="plot",
    title="🌸 Iris Dataset Visualizer",
    description="Select a feature to see its distribution"
)

# Run app
app.launch()
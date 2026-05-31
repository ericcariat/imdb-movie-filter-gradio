import gradio as gr
from data_utils import read_database

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)


# read data 
print("Reading database...")
df = read_database("imdb_top_1000.csv")
# check df is valid and has some data 
if df is not None and not df.empty:
    print("Database read successfully!")
else:    
    print("Failed to read database or database is empty.") 

demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
    api_name="predict"
)

demo.launch()

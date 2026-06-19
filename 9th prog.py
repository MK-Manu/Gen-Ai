!pip install wikipedia-api pydantic ipywidgets

import wikipediaapi
from pydantic import BaseModel
import ipywidgets as widgets
from IPython.display import display

class Institution(BaseModel):
    founder:str="N/A"
    founded:str="N/A"
    branches:str="N/A"
    employees:str="N/A"
    summary:str="N/A"

wiki = wikipediaapi.Wikipedia(
    user_agent="MyApp/1.0",
    language="en"
)

def fetch(b):
    page = wiki.page(box.value)

    if page.exists():
        data = Institution(summary=page.summary[:300])

        text = page.text

        for line in text.split("\n"):
            if "Founder" in line:
                data.founder=line
            elif "Founded" in line:
                data.founded=line
            elif "Branch" in line:
                data.branches=line
            elif "employees" in line.lower():
                data.employees=line

        print("\nFounder:",data.founder)
        print("\nFounded:",data.founded)
        print("Branches:",data.branches)
        print("Number of Employees:",data.employees)
        print("Summary:",data.summary)

box = widgets.Text(description="Institution:")
button = widgets.Button(description="Fetch")

button.on_click(fetch)

display(box,button)

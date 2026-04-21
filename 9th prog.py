import wikipediaapi, re
from pydantic import BaseModel
from typing import Optional

class Details(BaseModel):
    founder: Optional[str] = None
    founded: Optional[str] = None
    branches: Optional[str] = None
    employees: Optional[str] = None
    summary: Optional[str] = None

def get(name):
    page = wikipediaapi.Wikipedia(
        user_agent="MyApp/1.0 (student@example.com)", language='en'
    ).page(name)

    if not page.exists(): return print("Page not found")

    find = lambda p,t: (re.search(p,t).group(1) if re.search(p,t) else None)

    d = Details(
        founder = find(r'by ([A-Z][a-zA-Z\s\.]+)', page.summary),
        founded = find(r'\b(19|20)\d{2}\b', page.summary),
        branches= find(r'(\d+)\s+(?:campuses|branches)', page.text),
        employees=find(r'(\d{1,3}(?:,\d{3})*) employees', page.text),
        summary = '\n'.join(page.summary.split('.')[:4])
    )

    print("Institution:\n", name)
    print(f"Founder: {d.founder or 'N/A'}")
    print(f"Founded: {d.founded or 'N/A'}")
    print(f"Branches: {d.branches or 'N/A'}")
    print(f"Number of Employees: {d.employees or 'N/A'}")
    print("Summary:\n", d.summary)

get(input("Enter Institution: "))

# < begin copyright > 
# Copyright Ryan Marcus 2018
# 
# This file is part of seminar_site.
# 
# seminar_site is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# seminar_site is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with seminar_site.  If not, see <http://www.gnu.org/licenses/>.
# 
# < end copyright > 
import json
import pystache
import dateparser
import os.path
import os
import shutil


def process_dates(seminars):
    """sorts the seminars by the date, and adds a "short_date" field

    The short_date field will be in MM/DD/YY format. """
    
    for s in seminars:
        dt = dateparser.parse(s["date"])
        s["short_date"] = dt.strftime("%m/%d/%y")
        s["dt"] = dt

    seminars = sorted(seminars,
                      key=lambda x: x["dt"],
                      reverse=True)
    return seminars

def process_papers(seminars):
    """Copies relevant papers listed in the input into the output.

    Assumes the "id" field already exists (used for naming each PDF)
    """
    
    for s in seminars:
        paper_path = s["paper_path"]
        paper_name = "{}.pdf".format(s["id"])
        paper_out = os.path.join("output", "papers", paper_name)
        s["paper_url"] = "papers/{}".format(paper_name)
        shutil.copy(paper_path, paper_out)
    return seminars

def assign_ids(seminars):
    """assigns IDs sequentially to the seminars """
    for idx, s in enumerate(reversed(seminars)):
        s["id"] = "seminar{}".format(idx)
    return seminars

def assign_short_titles(seminars):
    """prepares short titles (< 50 characters) for each seminar,
    under the key "short_title" """

    for s in seminars:
        s["short_title"] = (s["title"]
                            if len(s["title"]) < 49 else
                            s["title"][:45] + "...")
    return seminars
        


# if the output directory exists, delete it.
# Then, recreate the needed directories.
if os.path.exists("output"):
    shutil.rmtree("output")
os.makedirs("output")
os.makedirs("output/papers")

# load the data. 
with open("data.json", "r") as f:
    data = json.load(f)

assert "seminars" in data

print("Processing", len(data["seminars"]), "seminars...")

# verify that each entry has the required fields
required_fields = ["title", "speaker", "abstract", "date"]
for s in data["seminars"]:
    for req_f in required_fields:
        assert req_f in s
        
    s["paper_path"] = os.path.join("papers", s["paper"])
    if not os.path.exists(s["paper_path"]):
        raise FileNotFoundError(s["paper_path"])
    

print("All data validated.")

# seminar processing steps
steps = [process_dates, assign_ids,
         process_papers, assign_short_titles]

seminars = data["seminars"]

for step in steps:
    seminars = step(seminars)

# load the template
with open("template.mustache", "r") as f:
    template = f.read()

# render the template into the output
with open("output/index.html", "w") as f:
    f.write(pystache.render(template, {"seminars": seminars}))

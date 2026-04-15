import os

#==============================================
# SECTION 1: Project Setup
#==============================================

print("=" * 42)
print("   OpenTrack - Open Source Project")
print("   Project Lead: Prodipta")
print("=" * 42)

project = ("OpenTrack", "1.0", 2026, "Python", "Prodipta")

print("Name :", project[0], "| Version :", project[1], "| Started :", project[2])
print("First 3 fields :", project[:3])
print("Language count :", project.count("Python"), " Language index :", project.index("Python"))

# project[0] = "test" - TypeError: tuples are immutable

contributors = []

#==============================================
# CONTRIBUTORS INPUT
#==============================================

for i in range(4):
    print(f"\nEnter Contributor {i+1}")
    
    while True:
        name = input("Name: ")
        if name.replace(" ", "").isalpha():
            break
        print("Invalid! Name must contain only letters and spaces.")
        
    role = input("Role: ")
    language = input("Language: ")
    if language.replace(" ","").isalpha():
            language = language.title()
    else:
        print("Invalid! Language must contain only letters and spaces.")
        language = "Unknown"
    
    while True:
        commits = input("Commits: ")
        if commits.isdigit():
            commits = int(commits)
            break
        print("Invalid! Commits must be a number.")
        
    while True:
        country = input("Country: ")
        if country.replace(" ", "").isalpha():
            country = country.title()
            break
        print("Invalid! Country must contain only letters and spaces.")
        
    contributors.append({
        "name": name,
        "role": role,
        "language": language,
        "commits": commits,
        "country": country
    })
    
names = sorted([c["name"] for c in contributors])
print("\nSorted names :", names)
print("Last name :", names[-1], "First two :", names[:2])

for c in contributors:
    c.update({"status": "Active"})
    
print("Contributor 1 status :", contributors[0].get("status"))
backup = contributors[0].copy()
print("Backup :", backup)

#==============================================
# ISSUES INPUT
#==============================================


issues = []

valid_priorities = ["Critical", "High", "Medium", "Low"]
valid_status = ["Open", "In Progress", "Resolved"]
valid_types = ["Bug", "Feature"]

for i in range(5):
    print(f"\nEnter Issue {i+1}")
    
    issue_id = input("ID: ")
    title = input("Title: ")
    
    while True:
        issue_type = input("Type (Bug/Feature): ").title()
        if issue_type in valid_types:
            break
        print("Invalid! Type must be 'Bug' or 'Feature'.")
        
    while True:
        priority = input("Priority (Critical/High/Medium/Low): ").title()
        if priority in valid_priorities:
            break
        print("Invalid! Priority must be one of: Critical, High, Medium, Low.")
        
    while True:
        status = input("Status (Open/In Progress/Resolved): ").title()
        if status in valid_status:
            break
        print("Invalid! Status must be one of: Open, In Progress, Resolved.")
        
    while True:
        reporter = input("Reporter: ")
        if reporter.replace(" ", "").isalpha():
            break
        print("Invalid! Reporter must contain only letters and spaces.")
        
    issues.append({
        "id": issue_id,
        "title": title,
        "type": issue_type,
        "priority": priority,
        "status": status,
        "reporter": reporter
    })
    
#==============================================
# ANALYSIS
#==============================================

open_count = 0
for i in issues:
    if i["status"] == "Open":
        open_count += 1
print("\nTotal Open Issues :", open_count)

issues[0]["priority"] = "Critical"
print("First issue -> Priority updated to Critical.")

print("Last two issues :", issues[-2:])

reporters = set(i["reporter"] for i in issues)
tech_stack = set(c["language"] for c in contributors)

tech_stack.add("Rust")
tech_stack.discard("Go")

print("\nreporters :", reporters)
print("tech_stack :", tech_stack)
print("union :", reporters.union(tech_stack))
print("intersection :", reporters.intersection(tech_stack))

priority_set = {i["priority"] for i in issues}
print("Critical present :", "YES - flag for immediate review." if "Critical" in priority_set else "NO")

priority_count = {}
for i in issues:
    p = i["priority"]
    priority_count[p] = priority_count.get(p, 0) + 1
    
status_groups = {}
for i in issues:
    status_groups.setdefault(i["status"], []).append(i["title"])
    
print("\npriority_keys :", priority_count.keys())
print("priority_values :", priority_count.values())

for k, v in status_groups.items():
    print("Status Groups ->", k, ":", v)
    
report_count = {}
for i in issues:
    r = i["reporter"]
    report_count[r] = report_count.get(r, 0) + 1
    
top_reporter = ""
end=max_count = 0
for k, v in report_count.items():
    if v > max_count:
        max_count = v
        top_reporter = k
    
print("\nTop Reporter :", top_reporter, "with", max_count, "issues reported.")

issues[0].pop("type")

#==============================================
# FILE HANDLING
#==============================================

folder = project[0].lower().replace(" ", "_")

if not os.path.exists(folder):
    os.mkdir(folder)

report_path = os.path.join(folder, "project_report.txt")
csv_path = os.path.join(folder, "issues.csv")

try:
    with open(report_path, "w") as f:
        f.write("==============================================\n")
        f.write(f"{project[0]} - Project Report\n")
        f.write("==============================================\n")
        f.write(f"Contributors ({len(contributors)}):\n")
        f.write(f"Issues ({len(issues)}):\n")
        f.write(f"Top Reporter: {top_reporter} ({max_count} issues)\n")
    
    with open(csv_path, "w") as f:
        f.write("id,title,priority,status,reporter\n")
        for i in issues:
            f.write(f"{i['id']},{i['title']},{i['priority']},{i['status']},{i['reporter']}, {i['status']}\n")
            
            
except IOError:
    print("Error writing files.")
print("Files saved :", os.listdir(folder))

#==============================================
# File Reading
#==============================================

try: 
    with open(report_path, "r") as f:
        print("\n--- read() ---")
        print(f.read())

    with open(report_path, "r") as f:
        print("\n--- readline() ---")
        print("Line 1 :", f.readline())
        print("Line 2 :", f.readline())
    
    with open(report_path, "r") as f:
        lines = f.readlines()
        filtered = [l for l in lines if "Critical" in l or "High" in l]
        print("\n--- readlines() with filter ---")
        print("Total Lines :", len(lines), " Critical/High lines :", len(filtered))
    
except FileNotFoundError:
    print("Report file not found.")
    

#==============================================
# BONUS
#==============================================

urgent = [i["title"] for i in issues if i["priority"] in ["Critical", "High"]]
print("\nUrgent issues :", urgent, "Count:", len(urgent))

with open(report_path, "a") as f:
    f.write("\nUrgent Issues:\n")
    for u in urgent:
        f.write(u + "\n")
        
with open(report_path, "r") as f:
    lines = f.readlines()
    print("\nLast 6 lines:")
    for l in lines[-6:]:
        print(l.strip())
        
#==============================================
#Final Summary
#==============================================

print("\n" + "=" * 42)
print(f"   {project[0]} — FINAL SUMMARY")
print("=" * 42)
print(f"Project : {project[0]}     Version : {project[1]}     Lead : {project[4]}")
print(f"Contributors : {len(contributors)}   Names : {names}")
print(f"Tech Stack   : {tech_stack}")
print(f"Issues : {len(issues)}   Open : {open_count}   Reporters : {len(reporters)}")
print(f"Top Reporter : {top_reporter} ({max_count} issues)")
print(f"{'  '.join([f'{k}:{v}' for k,v in priority_count.items()])}")
print(f"Report : {report_path}")
print(f"CSV    : {csv_path}")
print("=" * 42)
print(f"{project[0]} complete. Thank you for contributing to open source!")
print("=" * 42)
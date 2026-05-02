import re

def parse_and_print_table():
    log_file = 'loco_evaluation.log'
    try:
        with open(log_file, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Log file not found yet.")
        return

    categories = [
        "breakfast_box",
        "juice_bottle",
        "pushpins",
        "screw_bag",
        "splicing_connectors"
    ]
    
    results = {cat: {"Logical": "[Run to evaluate]", "Structural": "[Run to evaluate]"} for cat in categories}
    
    current_category = None
    for line in lines:
        if "Evaluating dataset" in line:
            for cat in categories:
                if cat in line:
                    current_category = cat
                    break
        elif "Logical AUROC:" in line and current_category:
            match = re.search(r"Logical AUROC: ([\d\.]+), Structural AUROC: ([\d\.]+)", line)
            if match:
                results[current_category]["Logical"] = f"{float(match.group(1))*100:.1f}%"
                results[current_category]["Structural"] = f"{float(match.group(2))*100:.1f}%"

    print("| Category | Logical Anomaly AUROC | Structural Anomaly AUROC |")
    print("| :--- | :---: | :---: |")
    for cat in categories:
        name = cat.replace('_', ' ').title()
        log = results[cat]["Logical"]
        struc = results[cat]["Structural"]
        print(f"| {name} | {log} | {struc} |")

if __name__ == "__main__":
    parse_and_print_table()

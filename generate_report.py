import json
from fibonacci import main

def generate_report():
    result = main()

    report = {
        "status": "success",
        "message": result["message"],
        "terms": result["n"],
        "fibonacci_series": result["fibonacci"]
    }

    # JSON report
    with open("report.json", "w") as f:
        json.dump(report, f, indent=4)

    # Text report
    with open("report.txt", "w") as f:
        f.write("Execution Report\n")
        f.write("=================\n")
        f.write(f"Message: {report['message']}\n")
        f.write(f"Number of terms: {report['terms']}\n")
        f.write(f"Fibonacci Series: {report['fibonacci_series']}\n")

    print("Report generated successfully")


if __name__ == "__main__":
    generate_report()

from tools.summary_generator import generate_summary

def test_summary_generator():
    result = generate_summary("Trial A: Eligible\nTrial B: Ineligible")
    print(result)

if __name__ == "__main__":
    test_summary_generator()

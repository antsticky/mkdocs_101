from frontend.src.models import MyBaseModel2

def run_example() -> None:
    """
    Demonstrates usage of MyBaseModel2.
    """
    alms = MyBaseModel2(c=1, d="a")
    print(alms)

if __name__ == "__main__":
    run_example()

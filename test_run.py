from main import run
import os


def assert_equal(result: list, correct: list, name: str) -> None:
    """
    A function to assert correct implementation of functions
    """
    if result == correct:
        print(f"Test {name}: ✅")
    else:
        print(f"Test {name} : ❌")
        print(f"Expected {correct}, got {result}")


def assert_list(result: list, name: str) -> None:
    """
    A function to asset result is a list
    """
    if isinstance(result, list):
        print(f"Test {name}: ✅")
    else:
        print(f"Test {name} : ❌")
        print(f"Output {result} is not a list")


def assert_sentiment(result: list, name: str) -> None:
    """
    A function to assert output contains sentiment
    """
    if "positive" in result and "negative" in result and "neutral" in result:
        print(f"Test {name}: ✅")
    else:
        print(f"Test {name} : ❌")
        print(f"Output {result} contains sentiment")


def images_present(path: str, name: str) -> bool:
    """
    A function to check that images with specific filenames
    have been created
    """
    if any(os.scandir(path)):
        print(f"Test {name}: ✅")
    else:
        print(f"Test {name} : ❌")
        print(f"{path} contains no images")

if __name__ == "__main__":
    # test correct implementation of basic file
    print("main.py module test")
    test_out = run("data/raw/reviews.json")

    assert_list(test_out, "List Output")
    assert_sentiment(test_out, "Contains Sentiment")
    images_present("images/", "Images Present")

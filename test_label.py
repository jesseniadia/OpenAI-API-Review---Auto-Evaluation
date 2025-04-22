from label import get_sentiment
from test_run import assert_equal

from config import out_list, error_message


if __name__ == "__main__":
    print("get_sentiment function test")

    in_data = [
        "this ring smells weird, don't recomend",
        "I love this ring, I use it all the time when working out.",
        "I will never buy another brand again, I love this ring",
        "It's an ok ring. Some features could be better but for the price its fine.",
        "its a ring",
        "Bought this ring and it came broken. rip-off."
    ]

    assert_equal(get_sentiment(in_data), out_list, "Functionality")

    error_data1 = []

    assert_equal(get_sentiment(error_data1), error_message, "Error due to Empty List")

    error_data2 = [1, 2, 3, 4, 5]

    assert_equal(get_sentiment(error_data2), error_message, "Error due to wrong Type")

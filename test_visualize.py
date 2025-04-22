from visualize import make_plot
from test_run import images_present

from config import out_list


if __name__ == "__main__":
    print("make_plot function test")

    handle = make_plot(out_list)
    images_present("images/", "Images Present")

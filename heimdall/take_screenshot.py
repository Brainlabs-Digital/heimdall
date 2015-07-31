from heimdall import screenshot


if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser(description='Save a screenshot.')
    parser.add_argument('url', help='url to screenshot')
    parser.add_argument('-width', help='width of the viewport', type=int)
    parser.add_argument('-height', help='width of the viewport', type=int)

    args = parser.parse_args()

    screenshot(**vars(args))

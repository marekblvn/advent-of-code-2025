
def main() -> None:
    pass

if __name__ == "__main__":
    from sys import prefix, base_prefix
    if (prefix == base_prefix):
        print("You are not using a virtual environment!")
        exit(0)
    main()
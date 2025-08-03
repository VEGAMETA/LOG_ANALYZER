from app.processor import Processor


def main() -> None:
    Processor()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        exit(1)

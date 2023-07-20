from fuzzy_media_renamer.args import parser

def main() -> None:
    args = parser.parse_args()

    print(args)

if __name__ == "__main__":
    main()

import os

TEXT = (
    "I sent your apology to Mr. Hart at midnight, word-perfect, "
    "except autocorrect addressed it 'Dear Heart' and signed me "
    "'your devoted assistant.' He replied: 'Apology accepted, sweetheart.'"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

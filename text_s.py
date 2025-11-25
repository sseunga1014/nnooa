import argparse
from collections import Counter
from pathlib import Path
import re


def analyze_text(path: Path) -> None:
    if not path.exists():
        print(f"파일을 찾을 수 없습니다: {path}")
        return

    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    words = re.findall(r"\w+", text.lower())

    print(f"=== 텍스트 분석: {path.name} ===")
    print(f"총 라인 수: {len(lines)}")
    print(f"총 단어 수: {len(words)}")
    print(f"총 문자 수: {len(text)}")

    counter = Counter(words)
    print("\n상위 10개 단어:")
    for word, count in counter.most_common(10):
        print(f"{word:15s} : {count}")


def main():
    parser = argparse.ArgumentParser(
        description="텍스트 파일 기본 통계 & 단어 빈도 분석기"
    )
    parser.add_argument("file", help="분석할 텍스트 파일 경로")
    args = parser.parse_args()

    analyze_text(Path(args.file))


if __name__ == "__main__":
    main()

import time
from pathlib import Path
from typing import List, Tuple

import requests


def load_urls(path: Path) -> List[str]:
    if not path.exists():
        print(f"URL 목록 파일이 없습니다: {path}")
        return []
    lines = [l.strip() for l in path.read_text(encoding="utf-8").splitlines()]
    return [l for l in lines if l and not l.startswith("#")]


def check_url(url: str, timeout: float = 5.0) -> Tuple[int, float, str]:
    """
    url 상태 코드, 응답 시간(sec), 에러 메시지(없으면 빈 문자열) 반환
    """
    start = time.time()
    try:
        resp = requests.get(url, timeout=timeout)
        elapsed = time.time() - start
        return resp.status_code, elapsed, ""
    except Exception as e:
        elapsed = time.time() - start
        return 0, elapsed, str(e)


def main():
    url_file = Path("urls.txt")
    urls = load_urls(url_file)
    if not urls:
        print("urls.txt 에 URL을 한 줄에 하나씩 적어주세요.")
        return

    print("=== URL 모니터링 결과 ===")
    for url in urls:
        status, elapsed, err = check_url(url)
        if status:
            print(f"{url:40s} | {status:3d} | {elapsed:5.2f}s")
        else:
            print(f"{url:40s} | ERR | {elapsed:5.2f}s | {err}")


if __name__ == "__main__":
    main()

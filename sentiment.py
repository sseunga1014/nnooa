from typing import List, Tuple

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report


def build_dataset() -> Tuple[List[str], List[int]]:
    """
    실제로는 CSV 로딩 등으로 대체 가능.
    여기서는 데모용 소규모 한글 문장 데이터셋 사용.
    label: 1=긍정, 0=부정
    """
    texts = [
        "이 영화 진짜 재미있다 최고다",
        "완전 감동적인 결말이었다",
        "배우 연기가 너무 좋았어요",
        "스토리가 지루하고 별로였다",
        "시간 낭비였다 다시 보고 싶지 않다",
        "음악이 아름답고 분위기가 좋았다",
        "전개가 엉망이고 이해가 안 됐다",
        "생각보다 훨씬 재밌게 봤다",
        "연출이 촌스럽고 유치했다",
        "마지막 장면이 인상 깊었다",
    ]
    labels = [1, 1, 1, 0, 0, 1, 0, 1, 0, 1]
    return texts, labels


def train_model() -> Pipeline:
    X, y = build_dataset()
    pipe = Pipeline(
        [
            ("vect", CountVectorizer()),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )
    pipe.fit(X, y)
    print("=== 학습 데이터에 대한 간단 평가 ===")
    print(classification_report(y, pipe.predict(X)))
    return pipe


def interactive_demo(model: Pipeline) -> None:
    print("\n한글 감성분석 데모입니다. 종료하려면 빈 줄 엔터.")
    while True:
        text = input("\n문장을 입력하세요: ").strip()
        if not text:
            print("종료합니다.")
            break
        pred = model.predict([text])[0]
        proba = model.predict_proba([text])[0][pred]
        label = "긍정" if pred == 1 else "부정"
        print(f"▶ 예측: {label} (확률 {proba:.2f})")


def main():
    model = train_model()
    interactive_demo(model)


if __name__ == "__main__":
    main()

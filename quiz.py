#!/usr/bin/env python3
"""which-tee-are-you — a tiny dev-personality quiz. No dependencies."""

QUESTIONS = [
    (
        "Your commit messages are usually:",
        [
            ("fix bug", "a"),
            ("A haiku about the bug", "b"),
            ("500 words explaining why it wasn't really a bug", "c"),
        ],
    ),
    (
        "It's Friday 5pm. There's a hotfix ready.",
        [
            ("Ship it. YOLO.", "a"),
            ("Ship it, but I whisper 'sorry' to production", "b"),
            ("Absolutely not, see you Monday", "c"),
        ],
    ),
    (
        "Your IDE theme is:",
        [
            ("Whatever came default, I don't care", "a"),
            ("Something with 'dracula' or 'midnight' in the name", "b"),
            ("I have 6 themes and switch based on mood", "c"),
        ],
    ),
    (
        "When something breaks in prod:",
        [
            ("git blame, find the human responsible", "a"),
            ("'It works on my machine' energy", "b"),
            ("Cry, then fix it, then cry again", "c"),
        ],
    ),
]

RESULTS = {
    "a": ("Terminal Debugger", "ready to deploy, always. https://gemzy.co.in/en/products/terminal-debugger-black"),
    "b": ("Chai Pe Charcha", "chill, discusses architecture over chai. Coming soon on gemzy.co.in"),
    "c": ("It Works on My Machine", "chaotic but honest. Coming soon on gemzy.co.in"),
}


def ask(question, options):
    print(f"\n{question}")
    for i, (opt_text, tag) in enumerate(options):
        label = "abc"[i]
        print(f"   {label}) {opt_text}")
    while True:
        choice = input("> ").strip().lower()
        for i, (opt_text, tag) in enumerate(options):
            if choice == "abc"[i]:
                return tag
        print("Pick a, b, or c.")


def main():
    print("=" * 50)
    print("which-tee-are-you — a quiz for developers")
    print("=" * 50)

    answers = []
    for question, options in QUESTIONS:
        answers.append(ask(question, options))

    tally = {"a": 0, "b": 0, "c": 0}
    for a in answers:
        tally[a] += 1
    winner = max(tally, key=lambda k: tally[k])

    name, desc = RESULTS[winner]
    print("\n" + "=" * 50)
    print(f"You are: {name}")
    print(desc)
    print("=" * 50)


if __name__ == "__main__":
    main()

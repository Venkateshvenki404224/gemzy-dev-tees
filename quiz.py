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
    (
        "Your relationship with AI-assisted coding:",
        [
            ("I ask it to write the whole thing and pray", "vibe"),
            ("I use it for boilerplate, I write the logic", "b"),
            ("I read the output line by line before I run it", "c"),
        ],
    ),
]

RESULTS = {
    "a": ("Terminal Debugger", "ready to deploy, always.", "https://gemzy.co.in/en/products/terminal-debugger-black"),
    "b": ("Code Trust The Process", "you know what you're doing, you're just not sure if the code does.", "https://gemzy.co.in/en/products/code-trust-the-process-white"),
    "c": ("It Works on My Machine", "chaotic but honest. Proven correct 100% of the time on your machine.", "https://gemzy.co.in/en/products/it-works-on-my-machine-black"),
    "vibe": ("ERROR 404: Sleep Not Found", "you shipped at 2am and you'll do it again.", "https://gemzy.co.in/en/products/error-404-sleep-not-found-black"),
}


def ask(question, options):
    print(f"\n{question}")
    for i, (opt_text, tag) in enumerate(options):
        label = "abcde"[i]
        print(f"   {label}) {opt_text}")
    valid = ["abcde"[i] for i in range(len(options))]
    while True:
        choice = input("> ").strip().lower()
        if choice in valid:
            _, tag = options["abcde".index(choice)]
            return tag
        print(f"Pick {'/'.join(valid)}.")


def main():
    print("=" * 50)
    print("which-tee-are-you — a quiz for developers")
    print("=" * 50)

    answers = []
    for question, options in QUESTIONS:
        answers.append(ask(question, options))

    tally = {}
    for a in answers:
        tally[a] = tally.get(a, 0) + 1
    winner = max(tally, key=lambda k: tally[k])

    name, desc, link = RESULTS[winner]
    print("\n" + "=" * 50)
    print(f"You are: {name}")
    print(desc)
    print(link)
    print("=" * 50)


if __name__ == "__main__":
    main()

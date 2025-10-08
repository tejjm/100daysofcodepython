class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

    def __repr__(self):
        return f"Question(text={self.text!r}, answer={self.answer!r})"
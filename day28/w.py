import random, json

class Question:
    def __init__(self, prompt: str, answer: str, category: str):
        self.prompt = prompt
        self.answer = answer
        self.category = category
    
class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.tracker = []
    
    def add_question(self, question):
        self.questions.append(question)
    
    def shuffle_questions(self):
        random.shuffle(self.questions)

    def ask(self):
        for question in self.questions:
            answer = input(question.prompt).strip().lower()
            self.check_answer(question, answer)

    def add_tracker(self, tracker):
        self.tracker.append(tracker)

    def check_answer(self, question, answer):
        if answer == question.answer:
            print("That is correct!")
            for tracker in self.tracker:
                tracker.update(question.category)
        else:
            print("Incorrect answer.")
            for tracker in self.tracker:
                tracker.update(question.category, True)

class ScoreTracker:
    def __init__(self, name=""):
        self.scores = [{"category": "pitching", "correct": 0, "incorrect": 0}, {"category": "hitting", "correct": 0, "incorrect": 0}, {"category": "general", "correct": 0, "incorrect": 0}]
        self.leaderboard = []
        self.name = name

    def update(self, category: str, miss=False):
        for score in self.scores:
            if score['category'] == category:
                if miss:
                    score['incorrect'] = score.get("incorrect", 0) + 1
                else:
                    score['correct'] = score.get("correct", 0) + 1

    def show_score(self):
        correct = 0
        total_questions = 0
        for score in self.scores:
            correct += score['correct']
            total_questions += score['correct']
            total_questions += score['incorrect']
            print(f"{score['category'].capitalize()}: {score['correct']}/{(score['correct'] + score['incorrect'])} correct - {(score['correct'] / (score['correct'] + score['incorrect'])) * 100:.0f}%")
        print(f"\n{correct} out of {total_questions} questions correct. Final Score: {(correct / total_questions) * 100:.0f}%")
        self.leaderboard.append({self.name: correct})
    
    def save_score(self, filename: str):
        with open(filename, "w") as file:
            json.dump(self.leaderboard, file, indent=2)
    
    def load_leaderboard(self, filename: str):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.leaderboard = data
        except FileNotFoundError:
            return []

    def get_high_score(self):
        for scores in self.leaderboard:
            if self.name in scores:
                return scores[self.name]
        return 0

class Player:
    def __init__(self, name, tracker):
        self.name = name
        self.high_score = tracker.get_high_score()
        
def main():
    q_one = Question("Which pitcher holds the all-time MLB record for career wins with 511? ",
                     "cy young", "pitching")
    q_two = Question("Who is the only player in MLB history to hit a walk-off inside-the-park grand slam? ",
                     "roberto clemente", "hitting")
    q_three = Question("How many stitches are on a standard official Major League Baseball? ", "108",
                       "general")
    q_four = Question("Which player holds the modern-day record for the longest hitting streak, at 56 games? ",
                      "joe dimaggio", "hitting")
    q_five = Question("Who holds the Major League Baseball record for the most career home runs? ",
                      "barry bonds", "hitting")
    q_six = Question("In 2024, which player became the first in MLB history to achieve a '50/50' season (50 home runs and 50 stolen bases)? ", "shohei ohtani", "hitting")
    q_seven = Question("Who is the MLB all-time leader in career strikeouts for a pitcher? ",
                       "nolan ryan", "pitching")
    q_eight = Question("As of the end of the 2025 season, which active pitcher leads all others in career strikeouts? ",
                "justin verlander", "pitching")
    
    tracker = ScoreTracker()
    tracker.load_leaderboard("leaderboard.json")

    while True:
        name = input("Please enter name: ").lower()
        name_exists = any(name in entry for entry in tracker.leaderboard)
        if name_exists:
            print("Name already in use.")
        else:
            break

    player = Player(name, tracker)
    tracker.name = player.name
    quiz = Quiz()
    
    quiz.add_tracker(tracker)
    quiz.add_question(q_one)
    quiz.add_question(q_two)
    quiz.add_question(q_three)
    quiz.add_question(q_four)
    quiz.add_question(q_five)
    quiz.add_question(q_six)
    quiz.add_question(q_seven)
    quiz.add_question(q_eight)
    quiz.shuffle_questions()
    quiz.ask()
    tracker.show_score()
    tracker.save_score("leaderboard.json")

if __name__ == "__main__":
    main()
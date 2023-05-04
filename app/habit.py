    @staticmethod
    def habits_with_periodicity(periodicity):
        """
        Returns a list of all habits with the same periodicity.
        """
        habits = []
        with open("habit_tracker_database.txt", "r") as f:
            for line in f:
                habit = line.strip().split(',')
                if habit[2] == str(periodicity):
                    habits.append(habit)
        return habits

    @staticmethod
    def longest_run_streak(habit_name):
        """
        Returns the longest run streak for a given habit.
        """
        longest_streak = 0
        current_streak = 0
        with open("habit_tracker_database.txt", "r") as f:
            for line in f:
                habit = line.strip().split(',')
                if habit[0] == habit_name:
                    if habit[5] == '1':
                        current_streak += 1
                    else:
                        longest_streak = max(longest_streak, current_streak)
                        current_streak = 0
        return longest_streak

import json
from dataclasses import dataclass


@dataclass
class Activity:
    activity: str
    activity_type: str
    cost: int
    people: int


def load_data() -> list[Activity]:
    activities: list[Activity] = []
    with open('activities.json') as f:
        for activity in json.load(f):
            activities.append(Activity(activity['activity'],
                                       activity['type'],
                                       activity['cost'],
                                       activity['people']))

        return activities


def generate_activity(activities: list[Activity]) -> None:
    try:
        people: int = int(input('How many people are you? '))
        cost: int = int(input('How much are you willing to spend per person ($)? '))
    except ValueError:
        print('Error: Please only enter numerical values.')
        return

    matched_activities: list[Activity] = []
    # Activities
    for activity in activities:
        activity_cost: int = activity.cost
        activity_people: int = activity.people

        if activity_cost <= cost and activity_people <= people:
            matched_activities.append(activity)  # type: ignore

    for i, matched in enumerate(matched_activities, 1):
        print(f'{i}: {matched.activity}: {matched.cost}$ per person [{people}p: {people * matched.cost}$]')


def main() -> None:
    activities: list[Activity] = load_data()
    generate_activity(activities)


if __name__ == '__main__':
    main()

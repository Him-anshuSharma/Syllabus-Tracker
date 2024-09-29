from flask import Flask, render_template
from datetime import datetime, timedelta

app = Flask(__name__)

# Sample dynamic data for the timeline
timeline_data = [
    {"date": "September 2024", "tasks": ["Complete Surgery till 30th September"]},
    {"date": "October 2024", "tasks": ["Terminals (1st - 13th)", "Gynaecology & Obstetrics (14th - 31st)"]},
    {"date": "November 2024", "tasks": ["Medicine (1st - 30th)"]},
    {"date": "December 2024", "tasks": ["Medicine (1st - 31st)"]}
]

def get_next_target_details(timeline):
    current_date = datetime.now()
    next_target = None

    for month in timeline:
        for task in month['tasks']:
            if 'Complete Surgery' in task:
                target_date = datetime(2024, 9, 30, 23, 59, 59)  # End of the day for surgery completion
            elif 'Terminals' in task:
                target_date = datetime(2024, 10, 1, 0, 0, 0)  # Start of Terminals
            elif 'Gynaecology' in task:
                target_date = datetime(2024, 10, 14, 0, 0, 0)  # Start of Gynaecology & Obstetrics
            elif 'Medicine' in task and month['date'] == "November 2024":
                target_date = datetime(2024, 11, 1, 0, 0, 0)  # Start of Medicine in November
            elif 'Medicine' in task and month['date'] == "December 2024":
                target_date = datetime(2024, 12, 1, 0, 0, 0)  # Start of Medicine in December
            
            if target_date > current_date:
                if next_target is None or target_date < next_target:
                    next_target = target_date

    return next_target

@app.route('/')
def index():
    next_target = get_next_target_details(timeline_data)
    current_date = datetime.now()
    return render_template('timeline.html', next_target=next_target, timeline=timeline_data, current_date=current_date)

if __name__ == '__main__':
    app.run(debug=True)

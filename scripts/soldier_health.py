import csv

def check_health(sensor_file='../data/sensor_data.csv'):
    """
    Reads soldier vitals from CSV and prints alerts for risky conditions.
    """
    with open(sensor_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            hr = int(row['heart_rate'])
            temp = float(row['temp'])
            movement = float(row['movement'])
            if hr > 100 or temp > 38 or movement < 0.1:
                print(f"ALERT: Soldier {row['id']} at risk! HR:{hr}, Temp:{temp}, Movement:{movement}")
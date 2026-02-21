import sys
import os
import cv2

# -----------------------------
# Fix for module import path
# -----------------------------
# Add parent directory to sys.path so scripts/ can be imported
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Now imports will work
from scripts.enemy_detection import detect_enemies
from scripts.threat_alert import threat_alert
from scripts.soldier_health import check_health
from scripts.night_vision import night_vision

# -----------------------------
# Main Simulation
# -----------------------------

# Load pre-recorded battlefield video
cap = cv2.VideoCapture('../data/drone_feed.mp4')

# Danger zone coordinates for alert (can adjust)
danger_zone = (100, 100, 500, 400)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Apply night vision effect
    frame_nv = night_vision(frame)

    # Detect enemies
    frame_detected, enemies = detect_enemies(frame_nv)

    # Trigger threat alert
    threat_alert(enemies, danger_zone)

    # Check soldier health
    check_health()  # reads CSV file

    # Draw danger zone rectangle on frame
    x1, y1, x2, y2 = danger_zone
    cv2.rectangle(frame_detected, (x1, y1), (x2, y2), (255,255,0), 2)

    # Show simulation dashboard
    cv2.imshow("Smart Defense Dashboard", frame_detected)

    # Press 'q' to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
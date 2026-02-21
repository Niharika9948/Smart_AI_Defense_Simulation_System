def threat_alert(enemies, danger_zone=(100,100,500,400)):
    """
    Trigger alert if any enemy enters the danger zone.
    danger_zone = (x1, y1, x2, y2)
    """
    dx1, dy1, dx2, dy2 = danger_zone
    for (x, y, w, h) in enemies:
        if x < dx2 and x+w > dx1 and y < dy2 and y+h > dy1:
            print("ALERT: Threat detected in danger zone!")
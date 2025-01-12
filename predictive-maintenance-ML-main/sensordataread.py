from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://nandininj26:C9eCrZZQ5G4l9ISm@cluster0.aadz9.mongodb.net/")
db = client["PredictiveMaintenance"]

# Updated dataset
dataset = [
    ["M", 302.6, 310.2, 2157, 17.2, 94, 0, "No Failure"],
    ["M", 302.6, 310.2, 1563, 39, 97, 0, "No Failure"],
    ["M", 302.6, 310.2, 1631, 31, 100, 0, "No Failure"],
    ["L", 302.5, 310.2, 1547, 36.9, 103, 0, "No Failure"],
    ["L", 302.6, 310.3, 1479, 40.4, 105, 0, "No Failure"],
    ["M", 302.4, 310.1, 1379, 48.9, 107, 1, "Heat Dissipation Failure"],
    ["L", 302.4, 310.1, 1906, 21.2, 110, 0, "No Failure"]
]

# Insert data into MongoDB
for i, row in enumerate(dataset):
    doc = {
          # M or L
        "air_temperature": row[1],
        "process_temperature": row[2],
        "rotational_speed": row[3],
        "torque": row[4],
        "tool_wear": row[5],
        "failure_type": row[7],
        "target": row[6]  # 0 or 1
    }
    db.sensor_readings.insert_one(doc)

print("Dataset inserted into MongoDB collection.")
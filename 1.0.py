import random

drivers = {
    #FERRARI
    "Hamilton": {"stats": {'tour rapide': 85, 'vitesse': 90, 'experiance': 95, 'depassement': 88, 'fiabilité': 88}, "team": "Ferrari"},
    "Leclerc": {"stats": {'tour rapide': 92, 'vitesse': 90, 'experiance': 82, 'depassement': 89, 'fiabilité': 84}, "team": "Ferrari"},

    #RED BULL
    "Verstappen": {"stats": {'tour rapide': 96, 'vitesse': 97, 'experiance': 91, 'depassement': 94, 'fiabilité': 92}, "team": "Red Bull"},
    "Hadjar": {"stats": {'tour rapide': 84, 'vitesse': 84, 'experiance': 76, 'depassement': 82, 'fiabilité': 80}, "team": "Red Bull"},

    #MCLAREN
    "Norris": {"stats": {'tour rapide': 91, 'vitesse': 90, 'experiance': 83, 'depassement': 90, 'fiabilité': 87}, "team": "McLaren"},
    "Piastri": {"stats": {'tour rapide': 89, 'vitesse': 88, 'experiance': 78, 'depassement': 86, 'fiabilité': 86}, "team": "McLaren"},

    #MERCEDES
    "Russell": {"stats": {'tour rapide': 90, 'vitesse': 89, 'experiance': 85, 'depassement': 87, 'fiabilité': 88}, "team": "Mercedes"},
    "Antonelli": {"stats": {'tour rapide': 84, 'vitesse': 85, 'experiance': 70, 'depassement': 82, 'fiabilité': 83}, "team": "Mercedes"},

    #ASTON MARTIN
    "Alonso": {"stats": {'tour rapide': 87, 'vitesse': 86, 'experiance': 97, 'depassement': 85, 'fiabilité': 84}, "team": "Aston Martin"},
    "Stroll": {"stats": {'tour rapide': 79, 'vitesse': 78, 'experiance': 76, 'depassement': 73, 'fiabilité': 79}, "team": "Aston Martin"},

    #ALPINE
    "Gasly": {"stats": {'tour rapide': 85, 'vitesse': 84, 'experiance': 80, 'depassement': 83, 'fiabilité': 84}, "team": "Alpine"},
    "Colapinto": {"stats": {'tour rapide': 82, 'vitesse': 83, 'experiance': 70, 'depassement': 81, 'fiabilité': 82}, "team": "Alpine"},

    #WILLIAMS
    "Albon": {"stats": {'tour rapide': 86, 'vitesse': 85, 'experiance': 80, 'depassement': 84, 'fiabilité': 86}, "team": "Williams"},
    "Sainz": {"stats": {'tour rapide': 87, 'vitesse': 86, 'experiance': 85, 'depassement': 83, 'fiabilité': 86}, "team": "Williams"},

    #HAAS
    "Ocon": {"stats": {'tour rapide': 84, 'vitesse': 83, 'experiance': 82, 'depassement': 81, 'fiabilité': 85}, "team": "Haas"},
    "Bearman": {"stats": {'tour rapide': 80, 'vitesse': 81, 'experiance': 72, 'depassement': 79, 'fiabilité': 80}, "team": "Haas"},

    #RB
    "Lawson": {"stats": {'tour rapide': 84, 'vitesse': 83, 'experiance': 78, 'depassement': 82, 'fiabilité': 83}, "team": "RB"},
    "Lingard": {"stats": {'tour rapide': 81, 'vitesse': 85, 'experiance': 70, 'depassement': 82, 'fiabilité': 78}, "team": "RB"},

    #AUDI
    "Hulkenberg": {"stats": {'tour rapide': 83, 'vitesse': 82, 'experiance': 90, 'depassement': 80, 'fiabilité': 85}, "team": "Audi"},
    "Bortoleto": {"stats": {'tour rapide': 80, 'vitesse': 79, 'experiance': 75, 'depassement': 78, 'fiabilité': 82}, "team": "Audi"},

    #Cadillac
   "Perez": {"stats": {'tour rapide': 85, 'vitesse': 84, 'experiance': 94, 'depassement': 85, 'fiabilité': 90}, "team": "Cadillac"},
    "Bottas": {"stats": {'tour rapide': 81, 'vitesse': 82, 'experiance': 93, 'depassement': 80, 'fiabilité': 89}, "team": "Cadillac"}
}

teams = {
    "Ferrari": {'strategie': 90, 'durabilite': 91, 'moteur': 93, 'aero': 92, 'chassie': 92},
    "Red Bull": {'strategie': 96, 'durabilite': 95, 'moteur': 97, 'aero': 96, 'chassie': 97},
    "McLaren": {'strategie': 91, 'durabilite': 90, 'moteur': 89, 'aero': 91, 'chassie': 90},
    "Mercedes": {'strategie': 88, 'durabilite': 89, 'moteur': 86, 'aero': 88, 'chassie': 87},
    "Aston Martin": {'strategie': 85, 'durabilite': 84, 'moteur': 83, 'aero': 85, 'chassie': 84},
    "Alpine": {'strategie': 83, 'durabilite': 82, 'moteur': 81, 'aero': 82, 'chassie': 82},
    "Williams": {'strategie': 80, 'durabilite': 79, 'moteur': 78, 'aero': 79, 'chassie': 79},
    "Haas": {'strategie': 78, 'durabilite': 77, 'moteur': 76, 'aero': 76, 'chassie': 75},
    "RB": {'strategie': 82, 'durabilite': 81, 'moteur': 80, 'aero': 81, 'chassie': 80},
    "Audi": {'strategie': 84, 'durabilite': 85, 'moteur': 88, 'aero': 84, 'chassie': 85},
    "Cadillac": {'strategie': 79, 'durabilite': 78, 'moteur': 77, 'aero': 78, 'chassie': 78}
}


tracks = {
    "Bahrain": {"moteur": 5, "durabilite": 3, "aero": 2, "chassie": 2},
    "Jeddah": {"moteur": 8, "durabilite": 2, "aero": 6, "chassie": 4},
    "Australia": {"moteur": 6, "durabilite": 4, "aero": 5, "chassie": 5},
    "Monaco": {"moteur": -5, "durabilite": 2, "aero": 9, "chassie": 10},
    "Silverstone": {"moteur": 7, "durabilite": 5, "aero": 8, "chassie": 7},
    "Spa": {"moteur": 9, "durabilite": 4, "aero": 6, "chassie": 5},
    "Monza": {"moteur": 10, "durabilite": -7, "aero": -3, "chassie": 5},
    "Suzuka": {"moteur": 6, "durabilite": 5, "aero": 9, "chassie": 8},
    "Brazil": {"moteur": 7, "durabilite": 6, "aero": 6, "chassie": 6},
    "Abu Dhabi": {"moteur": 5, "durabilite": 4, "aero": 5, "chassie": 5}
}


def calculate_driver_rating(stats):
    return sum(stats.values()) / len(stats)

def calculate_team_rating(team, track):
    return (
        team['strategie'] +
        team['durabilite'] + track['durabilite'] +
        team['moteur'] + track['moteur'] +
        team['aero'] + track['aero'] +
        team['chassie'] + track['chassie']
    ) / 5


def simulate_race(track_name, track):
    results = []

    for driver_name, data in drivers.items():
        driver_score = calculate_driver_rating(data["stats"])
        team_score = calculate_team_rating(teams[data["team"]], track)

        total = driver_score + team_score + random.randint(-10, 10)
        results.append((driver_name, total))

    results.sort(key=lambda x: x[1], reverse=True)

    print(f"\n🏁 {track_name} Results:")
    for i, (name, _) in enumerate(results):
        print(f"{i+1}. {name}")

    return results


def simulate_season():
    standings = {driver: 0 for driver in drivers}
    points = [25,18,15,12,10,8,6,4,2,1]

    for track_name, track in tracks.items():
        results = simulate_race(track_name, track)

        for i, (driver, _) in enumerate(results[:10]):
            standings[driver] += points[i]

    print("\n🏆 FINAL STANDINGS:")
    final = sorted(standings.items(), key=lambda x: x[1], reverse=True)

    for i, (driver, pts) in enumerate(final):
        print(f"{i+1}. {driver} - {pts} pts")

simulate_season()
game_backlog = {
    "name": ["Sekiro", "Wildfire", "Assassin's Creed", "HellDivers 2"],

    "genre": {"action": ["Sekiro", "Helldivers",],
                "rpg": ["Baldur's Gate 3", "The Wicher 3"],
                "fps": ["DOOM", "GhostRunner"]},
}

#Will print Sekiro
print(game_backlog["genre"]["action"][0])

game_backlog2 = [
    {
        "name": "Wildfire",
        "genre": "Stelth",
        "length": 20,
    },
        {
        "name": "CrossCode",
        "genre": "RPG",
        "length": 110,
    },
        {
        "name": "GhostRuneer 2",
        "genre": "Stelth",
        "length": 25,
    },
]

#Will print Wildfire
print(game_backlog2[0]["name"])
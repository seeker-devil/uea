# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (Ibarra, Tulcán, Quito)
# Segunda dimensión: Semanas (4 semanas)
# Tercera dimensión: Días de la semana (7 días)
temperaturas = [
    [   # Ibarra
        [   # Semana 1
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 26}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 24},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 30}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 20},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 23},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 29}
        ]
    ],
    [   # Tulcán
        [   # Semana 1
            {"day": "Lunes", "temp": 17},
            {"day": "Martes", "temp": 19},
            {"day": "Miércoles", "temp": 20},
            {"day": "Jueves", "temp": 18},
            {"day": "Viernes", "temp": 21},
            {"day": "Sábado", "temp": 22},
            {"day": "Domingo", "temp": 23}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 16},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 21},
            {"day": "Jueves", "temp": 22},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 26}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 18},
            {"day": "Martes", "temp": 21},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 24},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 19},
            {"day": "Martes", "temp": 20},
            {"day": "Miércoles", "temp": 22},
            {"day": "Jueves", "temp": 21},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 24},
            {"day": "Domingo", "temp": 26}
        ]
    ],
    [   # Quito
        [   # Semana 1
            {"day": "Lunes", "temp": 21},
            {"day": "Martes", "temp": 22},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 23},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 27}
        ],
        [   # Semana 2
            {"day": "Lunes", "temp": 22},
            {"day": "Martes", "temp": 23},
            {"day": "Miércoles", "temp": 24},
            {"day": "Jueves", "temp": 25},
            {"day": "Viernes", "temp": 26},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 28}
        ],
        [   # Semana 3
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 25},
            {"day": "Jueves", "temp": 26},
            {"day": "Viernes", "temp": 27},
            {"day": "Sábado", "temp": 28},
            {"day": "Domingo", "temp": 29}
        ],
        [   # Semana 4
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 27},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 29},
            {"day": "Domingo", "temp": 30}
        ]
    ]
]
nombres_ciudades = ["Ibarra", "Tulcán", "Quito"]

# Calcular el promedio de temperaturas para cada ciudad y semana
for index, ciudad in enumerate(temperaturas):
    print(f"Ciudad: {nombres_ciudades[index]}")
    for semana_index, semana in enumerate(ciudad):
        suma = 0
        conteo = 0
        for dia in semana:
            suma += dia['temp']
            conteo += 1
        promedio = suma / conteo
        print(f"  Promedio Semana {semana_index + 1}: {promedio:.2f}")

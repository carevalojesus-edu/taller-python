

if __name__ == '__main__':
    
    personas = [
        {"nombre": "Christian", "edad": 30},
        {"nombre": "Juan", "edad": 20},
        {"nombre": "Maria", "edad": 25},
        {"nombre": "Jose", "edad": 40},
    ]

    for persona in personas:
        if persona["edad"] > 23:
            print(persona["nombre"])
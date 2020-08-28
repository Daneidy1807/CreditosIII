contactos =[
    {
        'nombre':'Antonio',
        'email': 'antonio@antonio.com'
    },
    {
        'nombre':'Fernando',
        'email': 'fernando@fernando.com'
    },
    {
        'nombre':'Salvador',
        'email': 'salvador@salvador.com'
    }
]
contactos[0]['nombre']="andrea"
print(contactos[0]['nombre'])

for contacto in contactos:
    print(f"Nombre de los contactos: {contacto['nombre']}")
    print(f"Email de los contactos: {contacto['email']}")
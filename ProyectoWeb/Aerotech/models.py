from django.db import models

class Empleado(models.Model):
    DEPARTAMENTOS = [
        ('Dirección', 'Dirección'),
        ('Mantenimiento', 'Mantenimiento'),
        ('Logística', 'Logística'),
    ]
    dni = models.CharField(max_length=9, unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    departamento = models.CharField(max_length=50, choices=DEPARTAMENTOS)
    password = models.CharField(max_length=100, default="")   # PRUEBA PARA VER SI FUNCIONA EL LOGGER y pss VACIA




    def __str__(self):
        return f" Nombre {self.nombre} Apellidos {self.apellidos}"
    
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return self.nombre
    
class Equipo(models.Model):
    MODELOS = [
        ('aaaaaa000', 'aaaaaa000'),
        ('aaaaaaa111', 'aaaaaaa111'),
        ('aaaaaaa999', 'aaaaaaa999'),
        ('aaaaaaa888', 'aaaaaaa888'),
    ]

    MARCAS = [
        ('Ikertronic', 'Ikertronic'),
        ('JonAndertech', 'JonAndertech'),
    ]

    TIPOS = [
        ('Deshumidificador de Aire', 'Deshumidificador de Aire'),
        ('Depuradora', 'Depuradora'),
        ('Aire Acondicionado', 'Aire Acondicionado'),
    ]
        
    numero_serie = models.CharField(max_length=100, unique=True)
    modelo = models.CharField(max_length=50, choices=MODELOS)
    marca = models.CharField(max_length=50, choices=MARCAS)
    tipo = models.CharField(max_length=50, choices=TIPOS)
    fecha_adquisicion = models.DateField()
    fecha_puesta_marcha = models.DateField()
    planta = models.CharField(max_length=100)
    proveedores = models.ManyToManyField(Proveedor, related_name='proveedores')
    empleados = models.ManyToManyField(Empleado, related_name="equipos_asignados")


    def __str__(self):
        return f"{self.modelo} - {self.numero_serie}"

class Ticket(models.Model):
    URGENCIA = [
        ('alta', 'Alta'),
        ('media', 'Media'),
        ('baja', 'Baja')
        ]
    
    TIPO = [
        ('averia', 'Avería'),
        ('mejora', 'Mejora'),
        ('mantenimiento', 'Mantenimiento')
    ]

    ESTADO = [
        ('abierto', 'Abierto'), 
        ('cerrado', 'Cerrado')
    ]

    referencia = models.CharField(max_length=100, unique=True)
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_apertura = models.DateField(auto_now_add=True)
    fecha_resolucion = models.DateField(null=True, blank=True)
    urgencia = models.CharField(max_length=10, choices=URGENCIA)
    tipo = models.CharField(max_length=15, choices=TIPO)
    estado = models.CharField(max_length=10, choices=ESTADO)
    empleado = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True) 
    equipos = models.ManyToManyField(Equipo) 

    def __str__(self):
        return f"{self.titulo} - {self.referencia}"  
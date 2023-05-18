from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, User

task_complejidad=[
    (1, 'Baja'),
    (2, 'Media'),
    (3, 'Alta')
]

solicitud_estado=[
    (1, 'Pendiente'),
    (2, 'En proceso'),
    (3, 'En espera del cliente'),
    (4, 'Resuelto')
]
class CustomUserManager(BaseUserManager):
    def _create_user(self, email, password, first_name, last_name, mobile, **extra_fields):
        if not email:
            raise ValueError("Email must be provided")
        if not password:
            raise ValueError("Password is not provided")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            **extra_fields
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, first_name, last_name, mobile,**extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_ejecutivo', False)
        extra_fields.setdefault('is_cliente', False)
        return self._create_user(email, password, first_name, last_name, mobile ,**extra_fields)

    def create_superuser(self, email, password, first_name, last_name, mobile , **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', False)
        extra_fields.setdefault('is_ejecutivo', False)
        extra_fields.setdefault('is_cliente', False)
        return self._create_user(email, password, first_name, last_name, mobile, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    first_name = models.CharField(max_length=240)
    last_name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=50, null=True)
    adress = models.CharField(max_length=250, null=True)

    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_ejecutivo = models.BooleanField(default=False)
    is_cliente = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

class Categoria(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    code = models.CharField(max_length=48)
    def __str__(self):
        return self.title

class Subcategoria(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=48)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Task(models.Model):
    nombre = models.CharField(max_length=100)
    complejidad = models.IntegerField(
        null=False, blank=False,
        choices=task_complejidad
    )
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=48, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subcategoria = models.ForeignKey(Subcategoria, on_delete=models.CASCADE,null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Respuesta(models.Model):
    code = models.CharField(max_length=48, null=True)
    description = models.CharField(null=False, max_length=255)
    comentario = models.CharField(blank=True, null=True, max_length=100)
    requerimiento = models.ForeignKey(Task, blank=True, null=True, on_delete=models.CASCADE)
    formulario = models.URLField(blank=True, null=True)
    def __str__(self):
        return self.requerimiento.nombre

class Solicitud(models.Model):
    comentario = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(
        null=False, blank=False,
        choices=solicitud_estado, default=solicitud_estado[0][0]
    )
    datecompleted = models.DateTimeField(null=True, blank=True)
    requerimiento = models.ForeignKey(Task, on_delete=models.CASCADE)

    def __str__(self):
        return self.comentario
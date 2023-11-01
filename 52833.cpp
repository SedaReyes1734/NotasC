#include <stdio.h>
#include <string.h>

struct Estudiante {
    char nombre[50];
    int id;
    float notas[5]; // Supongamos que hay 5 asignaturas
};

void consultarNotas(struct Estudiante est) {
    printf("Notas de %s (ID: %d):\n", est.nombre, est.id);
    for (int i = 0; i < 5; i++) {
        printf("Asignatura %d: %.2f\n", i + 1, est.notas[i]);
    }
}

float calcularPromedio(struct Estudiante est) {
    float sum = 0.0;
    for (int i = 0; i < 5; i++) {
        sum += est.notas[i];
    }
    return sum / 5;
}

int main() {
    int numEstudiantes;
    printf("Cuantos estudiantes quiere registrar: ");
    scanf("%d", &numEstudiantes);

    struct Estudiante estudiantes[numEstudiantes];

    for (int i = 0; i < numEstudiantes; i++) {
        printf("Ingrese el nombre del estudiante %d: ", i + 1);
        scanf("%s", estudiantes[i].nombre);
        printf("Ingrese el ID del estudiante %d: ", i + 1);
        scanf("%d", &estudiantes[i].id);

        for (int j = 0; j < 5; j++) {
            printf("Ingrese la nota de la asignatura %d para el estudiante %d: ", j + 1, i + 1);
            scanf("%f", &estudiantes[i].notas[j]);
        }
    }

    int opcion;
    int estudianteSeleccionado;
    
    while (1) {
        printf("\nMenu:\n");
        printf("1. Consultar notas\n");
        printf("2. Calcular promedio\n");
        printf("3. Salir\n");
        printf("Elija una opcion: ");
        scanf("%d", &opcion);

        switch (opcion) {
            case 1:
                printf("Ingrese el número de estudiante a consultar: ");
                scanf("%d", &estudianteSeleccionado);
                if (estudianteSeleccionado >= 1 && estudianteSeleccionado <= numEstudiantes) {
                    consultarNotas(estudiantes[estudianteSeleccionado - 1]);
                } else {
                    printf("Estudiante no encontrado.\n");
                }
                break;
            case 2:
                printf("Ingrese el número de estudiante para calcular el promedio: ");
                scanf("%d", &estudianteSeleccionado);
                if (estudianteSeleccionado >= 1 && estudianteSeleccionado <= numEstudiantes) {
                    float promedio = calcularPromedio(estudiantes[estudianteSeleccionado - 1]);
                    printf("Promedio del estudiante %d: %.2f\n", estudianteSeleccionado, promedio);
                } else {
                    printf("Estudiante no encontrado.\n");
                }
                break;
            case 3:
                printf("Saliendo del programa.\n");
                return 0;
            default:
                printf("Opción no válida.\n");
        }
    }

    return 0;
}

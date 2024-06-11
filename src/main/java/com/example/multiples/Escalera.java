package com.example.multiples;

import java.util.Scanner;

public class Escalera {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese el número de escalones:");
        int numeroEscalones = scanner.nextInt();

        dibujarEscalera(numeroEscalones);

        scanner.close();
    }

    public static void dibujarEscalera(int numeroEscalones) {
        if (numeroEscalones > 0) {
            for (int i = 0; i < numeroEscalones; i++) {
                for (int j = 0; j < numeroEscalones - i - 1; j++) {
                    System.out.print(" ");
                }
                System.out.print("_|");
                System.out.println();
            }
        } else if (numeroEscalones < 0) {
            for (int i = 0; i < -numeroEscalones; i++) {
                for (int j = 0; j < i; j++) {
                    System.out.print(" ");
                }
                System.out.print("_|");
                System.out.println();
            }
        } else {
            System.out.println("__");
        }
    }
}


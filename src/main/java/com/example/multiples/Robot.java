package com.example.multiples;

import javafx.application.Application;
import javafx.stage.Stage;

import java.util.Arrays;

public class Robot {
    public static void main(String[] args) {
        int[] pasos = {10, 5, -2};
        int[] coordenadasFinales = coordenadasFinalesRobot(pasos);
        System.out.println("Coordenadas finales: (" + coordenadasFinales[0] + ", " + coordenadasFinales[1] + ")");
    }

    public static int[] coordenadasFinalesRobot(int[] pasos) {
        int x = 0;
        int y = 0;
        boolean ejeY = true;
        for (int paso : pasos) {
            if (ejeY) {
                y += paso;
            } else {
                x += paso;
            }
            ejeY = !ejeY;
        }


        int x_final = (int) Math.round(x * Math.cos(Math.toRadians(90)) - y * Math.sin(Math.toRadians(90)));
        int y_final = (int) Math.round(x * Math.sin(Math.toRadians(90)) + y * Math.cos(Math.toRadians(90)));

        return new int[]{x_final, y_final};
    }
}

